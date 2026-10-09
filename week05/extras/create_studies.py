"""Recreate the supplied Lecture 5 studies beside this script; requires Blender 5.2."""
import bpy
import json
import math
import sys
from pathlib import Path
from mathutils import Vector

WORK = Path(__file__).resolve().parent
SOURCE = WORK/'w04_station_v002.blend'
ASSETS = WORK/'generated'
sys.path.insert(0,str(WORK))



def material(name, color, rough=.4, metal=0, **values):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    mat.use_raytrace_refraction = True
    bs = mat.node_tree.nodes.get('Principled BSDF')
    bs.location = (0, 0)
    mat.node_tree.nodes['Material Output'].location = (370, 0)
    bs.inputs['Base Color'].default_value = (*color, 1)
    bs.inputs['Roughness'].default_value = rough
    bs.inputs['Metallic'].default_value = metal
    for key, value in values.items():
        bs.inputs[key.replace('_',' ')].default_value = value
    mat.diffuse_color = (*color, 1)
    return mat


def assign(obj, mat):
    obj.data.materials.clear()
    obj.data.materials.append(mat)


def point(obj, target):
    obj.rotation_euler = (Vector(target)-obj.location).to_track_quat('-Z','Y').to_euler()


def sphere(name, x, mat, scale=(.7,.7,.7)):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=64, ring_count=32, location=(x,0,scale[2]+.02))
    obj=bpy.context.object
    obj.name=name
    obj.scale=scale
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    for p in obj.data.polygons:p.use_smooth=True
    assign(obj,mat)
    return obj


def cube(name, location, scale, mat, bevel=.08):
    bpy.ops.mesh.primitive_cube_add(size=2,location=location)
    obj=bpy.context.object;obj.name=name;obj.scale=scale
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if bevel:
        mod=obj.modifiers.new('Rounded edges','BEVEL');mod.width=bevel;mod.segments=4
        obj.modifiers.new('Weighted face normals','WEIGHTED_NORMAL')
    assign(obj,mat)
    return obj


def caption(text, location, size=.27):
    curve=bpy.data.curves.new('Label '+text,'FONT');curve.body=text
    curve.align_x='CENTER';curve.size=size;curve.extrude=.001
    obj=bpy.data.objects.new('LABEL_'+text,curve);bpy.context.collection.objects.link(obj)
    obj.location=location
    obj.rotation_euler=(math.radians(67),0,0)
    assign(obj,bpy.data.materials['MAT_Label'])
    bpy.context.view_layer.update()
    backdrop=bpy.data.materials.get('MAT_Label_Backdrop')
    if backdrop is None:
        backdrop=material('MAT_Label_Backdrop',(.55,.62,.72))
        ns=backdrop.node_tree.nodes;ns.remove(ns['Principled BSDF'])
        shader=ns.new('ShaderNodeEmission');shader.inputs['Color'].default_value=(.55,.62,.72,1)
        backdrop.node_tree.links.new(shader.outputs[0],ns['Material Output'].inputs['Surface'])
    width=max(size*2,curve.size*sum(.3 if c in 'ilI ' else .6 for c in text))
    plate=cube('LABEL_Backdrop_'+text,(0,0,0),(width*.56+.08,size*.68,.004),backdrop,.035)
    plate.rotation_euler=obj.rotation_euler
    plate.location=obj.location+obj.rotation_euler.to_matrix()@Vector((0,size*.33,-.012))
    plate.visible_shadow=False;obj.visible_shadow=False
    return obj


def settings(scene):
    scene.render.engine='BLENDER_EEVEE'
    scene.eevee.use_raytracing=True
    scene.cycles.device='CPU';scene.cycles.samples=48;scene.cycles.preview_samples=24
    scene.cycles.use_denoising=True;scene.cycles.use_preview_denoising=True
    scene.render.resolution_x=3840;scene.render.resolution_y=2160;scene.render.resolution_percentage=100
    scene.render.image_settings.file_format='PNG'
    scene.display_settings.display_device='sRGB'
    scene.view_settings.view_transform='AgX';scene.view_settings.look='None'
    scene.view_settings.exposure=0;scene.view_settings.gamma=1
    scene['Viewing baseline']='sRGB display | AgX | None | Exposure 0 | Gamma 1'
    scene['Prepared assets']='Original SECourses teaching samples; learner node constructions begin from simple materials.'


def studio(name, width=10):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene=bpy.context.scene;scene.name=name;settings(scene)
    world=bpy.data.worlds.new('World_Neutral');world.use_nodes=True
    world.node_tree.nodes['Background'].inputs['Color'].default_value=(.18,.18,.18,1)
    world.node_tree.nodes['Background'].inputs['Strength'].default_value=.3
    scene.world=world
    label=material('MAT_Label',(.015,.02,.03),.6)
    nodes=label.node_tree.nodes
    nodes.remove(nodes['Principled BSDF'])
    ink=nodes.new('ShaderNodeEmission');ink.inputs['Color'].default_value=(.015,.02,.03,1)
    label.node_tree.links.new(ink.outputs[0],nodes['Material Output'].inputs['Surface'])
    ground=material('MAT_Ground',(.10,.12,.15),.5)
    cube('LAB_Ground',(0,0,-.12),(width*2,15,.1),ground,0)
    bpy.ops.object.light_add(type='AREA',location=(-1,-3.5,5.5))
    light=bpy.context.object;light.name='LAB_Key';light.data.energy=1500;light.data.shape='DISK';light.data.size=3.5
    point(light,(0,0,.6))
    bpy.ops.object.camera_add(location=(0,-11,6.3))
    cam=bpy.context.object;cam.name='LAB_Camera';point(cam,(0,0,.55));cam.data.type='ORTHO';cam.data.ortho_scale=width
    cam.data.passepartout_alpha=1
    scene.camera=cam
    # The prepared bright card is explicit reflected geometry, not an undisclosed second light.
    card=material('MAT_ReflectionCard',(.8,.8,.8),.5,Emission_Color=(.8,.8,.8,1),Emission_Strength=.2)
    card_obj=cube('LAB_ReflectionCard',(-width*.8,1,2.5),(2,.035,2.5),card,0)
    card_obj.rotation_euler.z=math.radians(65)
    return scene


def save(name, active):
    if bpy.context.scene.collection.objects:
        col=bpy.data.collections.new('Study');bpy.context.scene.collection.children.link(col)
        for obj in list(bpy.context.scene.collection.objects):
            col.objects.link(obj);bpy.context.scene.collection.objects.unlink(obj)
    bpy.ops.object.select_all(action='DESELECT')
    obj=bpy.data.objects[active];obj.select_set(True);bpy.context.view_layer.objects.active=obj
    for screen in bpy.data.screens:
        for area in screen.areas:
            if area.type=='VIEW_3D':
                area.spaces.active.region_3d.view_perspective='CAMERA'
                area.spaces.active.region_3d.view_camera_zoom=0
                area.spaces.active.shading.type='MATERIAL'
                area.spaces.active.shading.use_scene_world=True
                area.spaces.active.shading.use_scene_lights=True
            elif area.type=='PROPERTIES':area.spaces.active.context='MATERIAL'
    bpy.ops.wm.save_as_mainfile(filepath=str(ASSETS/name))


def build():
    ASSETS.mkdir(exist_ok=True)
    bpy.ops.wm.open_mainfile(filepath=str(SOURCE))
    settings(bpy.context.scene)
    for obj in bpy.context.scene.objects:
        if obj.hide_get():obj.hide_render=True
        if obj.name.startswith(('STUDY_','RETOPO_','REF_','BAKE_','CUT_','BACKUP_')):
            obj.hide_set(True);obj.hide_render=True
    # All original meshes and the aligned low/high bake pair are preserved.
    save('w05_inputs.blend','GEO_EquipmentHousing')

    studio('W05_FixedLight_Library',10.5)
    mats=[material('MAT_Paint_Reference',(.42,.125,.035),.38),
          material('MAT_Rubber_Reference',(.025,.03,.037),.76),
          material('MAT_Metal_Reference',(.55,.62,.7),.24,1),
          material('MAT_Glass_Reference',(.78,.94,.98),.08,Transmission_Weight=1,IOR=1.45)]
    for x,name,mat in zip([-3.3,-1.1,1.1,3.3],['Paint','Rubber','Metal','Transmission'],mats):
        sphere('SAMPLE_'+name,x,mat)
        caption(name,(x,-1.05,.07),.26)
    save('w05_material_library.blend','SAMPLE_Paint')

    studio('W05_Procedural_Lab',7.3)
    simple=material('MAT_Procedural_Start',(.32,.12,.045),.45)
    control=material('MAT_Constant_Control',(.32,.12,.045),.45)
    sphere('SAMPLE_Work',-1.35,simple,scale=(.95,.95,.95))
    sphere('SAMPLE_Control',1.35,control,scale=(.95,.95,.95))
    caption('Working material',(-1.35,-1.25,.07))
    caption('Constant control',(1.35,-1.25,.07))
    cube('STUDY_Slots',(0,3,1),(.7,.7,.7),simple)
    bpy.data.objects['STUDY_Slots'].hide_set(True);bpy.data.objects['STUDY_Slots'].hide_render=True
    save('w05_procedural_start.blend','SAMPLE_Work')

    studio('W05_ThinSheet_Lab',7.8)
    sheet_mat=material('MAT_ThinSheet_Start',(.08,.3,.028),.38,Subsurface_Weight=1)
    other=sheet_mat.copy();other.name='MAT_ThinSheet_Control'
    for x,name,mat in [(-2.25,'SHEET_Work',sheet_mat),(0,'SHEET_Control',other)]:
        verts=[];faces=[];n=16
        for j in range(n+1):
            for i in range(n+1):
                u=i/n*1.6-.8;v=j/n*1.8
                verts.append((u+x,.23*math.sin(u*2),v+.18))
        for j in range(n):
            for i in range(n):
                k=j*(n+1)+i;faces.append((k,k+1,k+n+2,k+n+1))
        mesh=bpy.data.meshes.new(name);mesh.from_pydata(verts,[],faces);mesh.update()
        obj=bpy.data.objects.new(name,mesh);bpy.context.collection.objects.link(obj);assign(obj,mat)
        for p in mesh.polygons:p.use_smooth=True
    thick=material('MAT_ThickGlass_Start',(.78,.94,.98),.08,Transmission_Weight=1,IOR=1.45)
    cube('SAMPLE_Thick',(2.25,0,1.05),(.65,.42,.87),thick)
    caption('Single sheet',(-2.25,-1,.07),.24)
    caption('Control sheet',(0,-1,.07),.24)
    caption('Closed thick object',(2.25,-1,.07),.24)
    key=bpy.data.objects['LAB_Key'];key.location=(0,2.3,4);point(key,(0,0,1))
    # Keep the reflector from blocking the intentionally chosen backlight.
    bpy.data.objects['LAB_ReflectionCard'].hide_render=True;bpy.data.objects['LAB_ReflectionCard'].hide_set(True)
    save('w05_thinwall_start.blend','SHEET_Work')

    studio('W05_Displacement_Lab',9.5)
    base=material('MAT_Displacement_Start',(.18,.21,.24),.55)
    sphere('SAMPLE_Displacement',0,base,scale=(.95,.95,.95))
    sub=bpy.context.object.modifiers.new('Prepared dense surface','SUBSURF');sub.levels=3;sub.render_levels=3
    sphere('SAMPLE_Bump',2.7,base.copy(),scale=(.95,.95,.95))
    bpy.context.object.active_material.name='MAT_Bump_Control'
    control=bpy.context.object.active_material;nodes=control.node_tree.nodes
    noise=nodes.new('ShaderNodeTexNoise');noise.location=(-500,0)
    bump=nodes.new('ShaderNodeBump');bump.location=(-220,0);bump.inputs['Distance'].default_value=.12
    control.node_tree.links.new(noise.outputs['Fac'],bump.inputs['Height'])
    control.node_tree.links.new(bump.outputs['Normal'],nodes['Principled BSDF'].inputs['Normal'])
    geom=sphere('SAMPLE_Geometry',-2.7,base.copy(),scale=(.95,.95,.95))
    geom.active_material.name='MAT_Geometry_Control'
    from mathutils.noise import noise as coherent_noise
    for v in geom.data.vertices:v.co+=v.normal*(coherent_noise(v.co*4)*.12)
    geom.data.update()
    caption('Mesh relief',(-2.7,-1.25,.07),.24)
    caption('Shader displacement',(0,-1.25,.07),.24)
    caption('Bump shading',(2.7,-1.25,.07),.24)
    save('w05_displacement_start.blend','SAMPLE_Displacement')
    from create_extra_studies import build_extra
    build_extra(globals())
    bpy.ops.wm.open_mainfile(filepath=str(ASSETS/'w05_procedural_start.blend'))
    bpy.data.objects['SAMPLE_Work'].active_material.node_tree.nodes['Principled BSDF'].inputs['Coat Roughness'].default_value=.3
    save('w05_coat_start.blend','SAMPLE_Work')
    print(json.dumps({'status':'built','assets':sorted(p.name for p in ASSETS.glob('*.blend'))}))


if __name__=='__main__':build()
