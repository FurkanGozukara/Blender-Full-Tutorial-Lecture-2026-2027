"""Original freely reusable starting meshes for Lecture 4, run in background Blender.

These are supplied inputs and reference comparisons. The lecture's terrain, rock,
bake pair and retopology results are made with visible mouse and keyboard actions.

Run with Blender --background --factory-startup --python this_script.py --
--source <Lecture_3_station.blend> --output <new_w04_inputs.blend>.
"""
import argparse
import bpy
import bmesh
import math
import json
import sys
from pathlib import Path
from mathutils import Quaternion

def activate(obj):
    if bpy.context.object and bpy.context.object.mode!='OBJECT':bpy.ops.object.mode_set(mode='OBJECT')
    for o in bpy.context.selected_objects:o.select_set(False)
    obj.hide_set(False);obj.select_set(True);bpy.context.view_layer.objects.active=obj
    return obj


def collection(name):
    c=bpy.data.collections.get(name)
    if c is None:
        c=bpy.data.collections.new(name);bpy.context.scene.collection.children.link(c)
    return c


def move(obj,name):
    c=collection(name)
    for old in list(obj.users_collection):old.objects.unlink(obj)
    c.objects.link(obj)


def material(name,color,roughness=.65):
    m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True
    bsdf=m.node_tree.nodes.get('Principled BSDF');bsdf.inputs['Base Color'].default_value=(*color,1);bsdf.inputs['Roughness'].default_value=roughness
    return m


def sphere(name,radii,location=(0,0,0),subdivisions=4,col='W04_INPUTS'):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=subdivisions,radius=1,location=location)
    o=bpy.context.object;o.name=name
    for v in o.data.vertices:
        for axis in range(3):v.co[axis]*=radii[axis]
    for p in o.data.polygons:p.use_smooth=True
    o.data.use_mirror_x=False;move(o,col)
    return o


def grid(name,size=4.4,steps=32,col='W04_INPUTS'):
    verts=[(-size/2+size*x/steps,-size/2+size*y/steps,0) for y in range(steps+1) for x in range(steps+1)]
    faces=[]
    for y in range(steps):
        for x in range(steps):
            i=y*(steps+1)+x;faces.append((i,i+1,i+steps+2,i+steps+1))
    mesh=bpy.data.meshes.new(name);mesh.from_pydata(verts,[],faces);mesh.update()
    o=bpy.data.objects.new(name,mesh);collection(col).objects.link(o)
    for p in mesh.polygons:p.use_smooth=True
    return o


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',required=True,type=Path)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--report',type=Path)
    args=parser.parse_args(sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else [])
    SOURCE=args.source.resolve()
    out=args.output.resolve()
    if not SOURCE.is_file():parser.error('The Lecture 3 source file does not exist.')
    if out.exists():parser.error('Choose a new output path; existing learner files are preserved.')
    out.parent.mkdir(parents=True,exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(SOURCE))
    for img in bpy.data.images:
        if img.source=='FILE' and img.filepath and not img.packed_file:
            img.filepath=bpy.path.abspath(img.filepath)
            if Path(img.filepath).is_file():img.pack()
    original=set(bpy.data.objects)
    stone=material('W04_Stone_Clay',(.22,.29,.32))
    terrain_mat=material('W04_Terrain_Clay',(.17,.23,.19))
    skin=material('W04_Head_Clay',(.32,.23,.17))
    terrain=grid('GEO_Terrain');terrain.location.z=.002;terrain.data.materials.append(terrain_mat)
    rock=sphere('GEO_Rock',(.39,.33,.43),(1.55,-.55,.36));rock.data.materials.append(stone)
    for stage in range(3):
        o=sphere('REF_Rock_'+['Primary','Secondary','Tertiary'][stage],(.48,.38,.49),((stage-1)*1.2,0,.46),col='W04_FORM_REFERENCE')
        for v in o.data.vertices:
            x,y,z=v.co
            if stage>=1:
                v.co.z=min(z,.34+.17*x)
                v.co.x=min(x,.34+.25*z)
            if stage==2:
                v.co+=v.normal*(.01*math.sin(35*x)*math.cos(33*z))
        o.data.materials.append(stone)
    for method in ['Voxel','Dyntopo','Multires']:
        o=sphere('STUDY_'+method,(.55,.45,.55),subdivisions=3,col='W04_RESOLUTION')
        if method=='Dyntopo':
            bm=bmesh.new();bm.from_mesh(o.data)
            edges=[e for e in bm.edges if all(v.co.z>.12 for v in e.verts)]
            bmesh.ops.subdivide_edges(bm,edges=edges,cuts=2,use_grid_fill=True)
            bm.to_mesh(o.data);bm.free();o.data.update()
        if method=='Multires':
            activate(o);m=o.modifiers.new('Multires','MULTIRES')
            for _ in range(2):bpy.ops.object.multires_subdivide(modifier=m.name)
        if method=='Voxel':o.data.remesh_voxel_size=.14
    color=sphere('STUDY_ColorRemesh',(.55,.45,.55),subdivisions=4,col='W04_COLOR')
    a=color.data.color_attributes.new(name='SculptColor',type='FLOAT_COLOR',domain='POINT')
    for v,c in zip(color.data.vertices,a.data):
        t=(v.co.z+.55)/1.1;c.color=(.08+.65*t,.14+.08*t,.65-.5*t,1)
    color.data.color_attributes.active_color=a;color.data.remesh_voxel_size=.1
    target=sphere('STUDY_ProjectTarget',(.62,.62,.42),(0,0,-.25),col='W04_PROJECT')
    target.data.materials.append(stone)
    sheet=grid('STUDY_ProjectSheet',size=1.4,steps=32,col='W04_PROJECT');sheet.location.z=.23
    sheet.data.materials.append(terrain_mat)
    primitive=sphere('STUDY_PrimitiveStart',(.4,.4,.4),col='W04_PRIMITIVES')
    head=sphere('STUDY_MaleHead',(.43,.35,.57),subdivisions=4,col='W04_HEAD')
    head.data.use_mirror_x=True;head.data.materials.append(skin)
    for side,x in [('L',-.18),('R',.18)]:
        eye=sphere('STUDY_Eye_'+side,(.105,.105,.105),(x,-.29,.13),subdivisions=3,col='W04_HEAD')
    for name,center,width,height,col in [
        ('STUDY_RetopoSeed',(1.55,-.91,.44),.3,.24,'W04_RETOPO'),
        ('STUDY_EyelidSeed',(.105,-.4,.21),.05,.03,'W04_HEAD')]:
        mesh=bpy.data.meshes.new(name)
        mesh.from_pydata([(-width/2,0,-height/2),(width/2,0,-height/2),(width/2,0,height/2),(-width/2,0,height/2)],[],[(0,1,2,3)])
        mesh.update();obj=bpy.data.objects.new(name,mesh);collection(col).objects.link(obj);obj.location=center
        obj.data.materials.append(skin if 'Eyelid' in name else stone)
    for o in bpy.data.objects:
        if o not in original:o.hide_set(True);o.hide_render=True
    # A separate teaching area keeps the organic study clear of station geometry.
    for obj in collection('W04_HEAD').objects:
        obj.location.x-=3;obj.location.z+=1.2
    for name in ['W04_FORM_REFERENCE','W04_RESOLUTION','W04_COLOR','W04_PROJECT','W04_PRIMITIVES','W04_HEAD','W04_RETOPO']:
        collection(name).hide_render=True
    activate(bpy.data.objects['GEO_Platform'])
    for screen in bpy.data.screens:
        for area in screen.areas:
            if area.type=='VIEW_3D':
                s=area.spaces.active;s.show_region_ui=False
                s.region_3d.view_location=(0,0,.85);s.region_3d.view_distance=5.6
    bpy.context.scene.render.resolution_x=3840;bpy.context.scene.render.resolution_y=2160;bpy.context.scene.render.resolution_percentage=100
    bpy.ops.wm.save_as_mainfile(filepath=str(out))
    report={'source':str(SOURCE),'output':str(out),'objects':[{'name':o.name,'vertices':len(o.data.vertices) if o.type=='MESH' else None,'location':list(o.location),'dimensions':list(o.dimensions),'collections':[c.name for c in o.users_collection]} for o in bpy.data.objects if o not in original]}
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True)
        args.report.write_text(json.dumps(report,indent=2),encoding='utf-8')
    print('W04_STUDIES',str(out),len(report['objects']))


if __name__=='__main__':main()
