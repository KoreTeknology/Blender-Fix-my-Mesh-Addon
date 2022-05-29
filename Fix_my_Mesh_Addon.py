# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENCE BLOCK #####


bl_info = {
    "name": "Fix my Mesh",
    "author": "Uriel Deveaud",
    "version": (1, 0, 1),
    "blender": (3, 1, 2),
    "location": "3D View > Header",
    "description": "A single button to fix the 3 common errors on objects",
    "warning": "",
    "category": "Educational",
    }

import bpy
from bpy.types import (
        Operator,
        Header,
        )

# 
class VIEW3D_OT_FixMesh(Operator):
    """Fix Mesh in Object"""
    bl_idname = "opr.fix_mesh"
    bl_label = "Fix my Mesh"
    bl_description = "Check for 3 common errors and fix them"
    bl_options = {'REGISTER', 'UNDO'}
    

    def execute(self, context):
        obj = context.active_object
        if obj.type == "MESH" and obj.mode == "EDIT":
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.remove_doubles()
            bpy.ops.mesh.normals_make_consistent(inside=False)
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            bpy.ops.object.editmode_toggle()
            return {'FINISHED'}
        elif obj.type == "MESH" and obj.mode == "OBJECT":
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.remove_doubles()
            bpy.ops.mesh.normals_make_consistent(inside=False)
            bpy.ops.object.editmode_toggle()
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')
            return {'FINISHED'}
        else:
            print("This is not a mesh")
            return {'FINISHED'}
        
       
def add_fixObject_button(self, context):
    self.layout.operator(VIEW3D_OT_FixMesh.bl_idname,text="",icon='ERROR')        

classes = (
    VIEW3D_OT_FixMesh,
    )

# Register
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_HT_header.append(add_fixObject_button)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_HT_header.remove(add_fixObject_button)

if __name__ == "__main__":
    register()
