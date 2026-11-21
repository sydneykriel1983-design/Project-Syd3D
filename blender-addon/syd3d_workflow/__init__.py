Attempting to perform the InitializeDefaultDrives operation on the 'FileSystem' provider failed.
# SPDX-License-Identifier: GPL-3.0-or-later
"""Syd3D modeling workflow for Blender.

This extension orchestrates Blender's native modeling tools and adds a Syd3D
workspace menu. It does not include code from third-party Blender add-ons.
"""

bl_info = {
    "name": "Syd3D Workflow",
    "author": "Project Syd3D",
    "version": (0, 1, 0),
    "blender": (5, 3, 0),
    "location": "3D View > Sidebar > Syd3D",
    "description": "A Blender-first modeling workflow for Project Syd3D",
    "category": "3D View",
}

import bpy
from bpy.props import EnumProperty, FloatProperty, IntProperty


def _active_mesh(context):
    obj = context.view_layer.objects.active
    return obj if obj and obj.type == "MESH" else None


def _ensure_edit_mesh(context):
    obj = _active_mesh(context)
    if obj is None:
        return False
    if obj.mode != "EDIT":
        bpy.ops.object.mode_set(mode="EDIT")
    return True


def _set_box_select():
    """Keep LMB drag assigned to Blender's box selection tool."""
    wm = bpy.context.window_manager
    if wm is None:
        return None
    for window in wm.windows:
        for area in window.screen.areas:
            if area.type != "VIEW_3D":
                continue
            region = next((r for r in area.regions if r.type == "WINDOW"), None)
            if region is None:
                continue
            try:
                with bpy.context.temp_override(window=window, area=area, region=region):
                    bpy.ops.wm.tool_set_by_id(name="builtin.select_box")
            except (RuntimeError, TypeError):
                pass
    return None


class SYD3D_OT_select_box(bpy.types.Operator):
    bl_idname = "syd3d.select_box"
    bl_label = "Box Select"
    bl_description = "Use left-click drag for box selection; navigate with Blender's middle mouse controls"

    def execute(self, context):
        if context.area and context.area.type == "VIEW_3D":
            bpy.ops.wm.tool_set_by_id(name="builtin.select_box")
            self.report({"INFO"}, "Box Select active · middle mouse navigates")
            return {"FINISHED"}
        _set_box_select()
        return {"FINISHED"}


class SYD3D_OT_component_mode(bpy.types.Operator):
    bl_idname = "syd3d.component_mode"
    bl_label = "Component Selection"
    bl_options = {"REGISTER", "UNDO"}
    mode: EnumProperty(items=[("VERT", "Vertex", ""), ("EDGE", "Edge", ""), ("FACE", "Face", "")])

    def execute(self, context):
        if _active_mesh(context) is None:
            self.report({"WARNING"}, "Select a mesh object first")
            return {"CANCELLED"}
        if context.object.mode != "EDIT":
            bpy.ops.object.mode_set(mode="EDIT")
        bpy.ops.mesh.select_mode(type=self.mode)
        return {"FINISHED"}


class SYD3D_OT_move(bpy.types.Operator):
    bl_idname = "syd3d.move"
    bl_label = "Move"
    bl_description = "Blender move: drag freely or press X, Y, or Z to constrain; click or Enter confirms"

    def execute(self, context):
        if context.object is None:
            self.report({"WARNING"}, "Select an object or mesh components first")
            return {"CANCELLED"}
        bpy.ops.transform.translate("INVOKE_DEFAULT")
        return {"FINISHED"}


class SYD3D_OT_scale(bpy.types.Operator):
    bl_idname = "syd3d.scale"
    bl_label = "Scale"
    bl_description = "Blender scale: drag freely or press X, Y, or Z to constrain; type a factor"

    def execute(self, context):
        if context.object is None:
            self.report({"WARNING"}, "Select an object or mesh components first")
            return {"CANCELLED"}
        bpy.ops.transform.resize("INVOKE_DEFAULT")
        return {"FINISHED"}


class SYD3D_OT_bevel_interactive(bpy.types.Operator):
    bl_idname = "syd3d.bevel_interactive"
    bl_label = "Interactive Bevel"
    bl_description = "Native Blender bevel: move the mouse for width, scroll for segments, type a value, click to apply"

    def execute(self, context):
        if not _ensure_edit_mesh(context):
            self.report({"WARNING"}, "Select a mesh object first")
            return {"CANCELLED"}
        affect = "VERTICES" if context.tool_settings.mesh_select_mode[0] else "EDGES"
        bpy.ops.mesh.bevel("INVOKE_DEFAULT", offset_type="OFFSET", segments=1, affect=affect)
        return {"FINISHED"}


class SYD3D_OT_bevel_numeric(bpy.types.Operator):
    bl_idname = "syd3d.bevel_numeric"
    bl_label = "Apply Numeric Bevel"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        if not _ensure_edit_mesh(context):
            self.report({"WARNING"}, "Select a mesh object first")
            return {"CANCELLED"}
        scene = context.scene
        affect = "VERTICES" if context.tool_settings.mesh_select_mode[0] else "EDGES"
        bpy.ops.mesh.bevel(
            offset_type="OFFSET",
            offset=scene.syd3d_bevel_width,
            segments=scene.syd3d_bevel_segments,
            affect=affect,
        )
        return {"FINISHED"}


class SYD3D_OT_boolean(bpy.types.Operator):
    bl_idname = "syd3d.boolean"
    bl_label = "Boolean"
    bl_options = {"REGISTER", "UNDO"}
    operation: EnumProperty(items=[("DIFFERENCE", "Difference", "Subtract selected cutters"), ("UNION", "Union", "Join volumes"), ("INTERSECT", "Intersect", "Keep the overlap")])

    def execute(self, context):
        target = context.view_layer.objects.active
        cutters = [obj for obj in context.selected_objects if obj != target and obj.type == "MESH"]
        if target is None or target.type != "MESH" or not cutters:
            self.report({"WARNING"}, "Select a target mesh, then one or more cutter meshes; keep the target active")
            return {"CANCELLED"}
        for cutter in cutters:
            modifier = target.modifiers.new(name=f"Syd3D {self.operation.title()}", type="BOOLEAN")
            modifier.operation = self.operation
            modifier.solver = "EXACT"
            modifier.object = cutter
        return {"FINISHED"}


class SYD3D_OT_add_nurbs(bpy.types.Operator):
    bl_idname = "syd3d.add_nurbs"
    bl_label = "Add NURBS Geometry"
    bl_options = {"REGISTER", "UNDO"}
    kind: EnumProperty(items=[("SURFACE", "NURBS Surface", ""), ("CURVE", "NURBS Curve", "")])

    def execute(self, context):
        if self.kind == "SURFACE":
            bpy.ops.surface.primitive_nurbs_surface_surface_add()
        else:
            bpy.ops.curve.primitive_nurbs_curve_add()
        return {"FINISHED"}


class VIEW3D_MT_syd3d(bpy.types.Menu):
    bl_label = "Syd3D"
    bl_idname = "VIEW3D_MT_syd3d"

    def draw(self, context):
        layout = self.layout
        layout.operator("syd3d.select_box", icon="BORDER_RECT")
        layout.separator()
        layout.operator("syd3d.move", icon="TRANSFORM_MOVE")
        layout.operator("syd3d.scale", icon="TRANSFORM_SCALE")
        layout.operator("syd3d.bevel_interactive", icon="MOD_BEVEL")
        layout.separator()
        layout.operator("syd3d.add_nurbs", text="Add NURBS Surface", icon="SURFACE_NCURVE").kind = "SURFACE"
        layout.operator("syd3d.add_nurbs", text="Add NURBS Curve", icon="CURVE_NCURVE").kind = "CURVE"


class VIEW3D_PT_syd3d(bpy.types.Panel):
    bl_label = "Syd3D"
    bl_idname = "VIEW3D_PT_syd3d"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Syd3D"

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator("syd3d.select_box", text="Box Select", icon="BORDER_RECT")
        row = layout.row(align=True)
        row.operator("syd3d.component_mode", text="Vert").mode = "VERT"
        row.operator("syd3d.component_mode", text="Edge").mode = "EDGE"
        row.operator("syd3d.component_mode", text="Face").mode = "FACE"
        row = layout.row(align=True)
        row.operator("syd3d.move", icon="TRANSFORM_MOVE")
        row.operator("syd3d.scale", icon="TRANSFORM_SCALE")
        layout.operator("syd3d.bevel_interactive", icon="MOD_BEVEL")
        box = layout.box()
        box.label(text="Numeric Bevel")
        box.prop(context.scene, "syd3d_bevel_width", text="Width")
        box.prop(context.scene, "syd3d_bevel_segments", text="Segments")
        box.operator("syd3d.bevel_numeric", text="Apply Bevel")
        box = layout.box()
        box.label(text="Booleans", icon="MOD_BOOLEAN")
        row = box.row(align=True)
        for op in ("DIFFERENCE", "UNION", "INTERSECT"):
            button = row.operator("syd3d.boolean", text=op.title())
            button.operation = op
        box = layout.box()
        box.label(text="NURBS", icon="SURFACE_NCURVE")
        box.operator("syd3d.add_nurbs", text="Surface").kind = "SURFACE"
        box.operator("syd3d.add_nurbs", text="Curve").kind = "CURVE"
        layout.label(text="Blender mesh transforms and bevel are native.")
        layout.label(text="NURBS surfaces are not solid B-reps.")


classes = (
    SYD3D_OT_select_box,
    SYD3D_OT_component_mode,
    SYD3D_OT_move,
    SYD3D_OT_scale,
    SYD3D_OT_bevel_interactive,
    SYD3D_OT_bevel_numeric,
    SYD3D_OT_boolean,
    SYD3D_OT_add_nurbs,
    VIEW3D_MT_syd3d,
    VIEW3D_PT_syd3d,
)


def _draw_view3d_menu(self, context):
    self.layout.menu("VIEW3D_MT_syd3d", text="Syd3D")


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.syd3d_bevel_width = FloatProperty(name="Bevel Width", default=0.1, min=0.0001, soft_max=10.0, precision=3, unit="LENGTH")
    bpy.types.Scene.syd3d_bevel_segments = IntProperty(name="Segments", default=3, min=1, max=64)
    bpy.types.VIEW3D_MT_view.append(_draw_view3d_menu)
    bpy.app.timers.register(_set_box_select, first_interval=1.0)


def unregister():
    bpy.types.VIEW3D_MT_view.remove(_draw_view3d_menu)
    del bpy.types.Scene.syd3d_bevel_width
    del bpy.types.Scene.syd3d_bevel_segments
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()

