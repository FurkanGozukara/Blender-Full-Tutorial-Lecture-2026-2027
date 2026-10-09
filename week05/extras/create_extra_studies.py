"""Authored supplied examples, separate from all filmed learner construction."""
import bpy
import json
from mathutils import Vector


def build_extra(helpers):
    globals().update({k:helpers[k] for k in ('ASSETS','WORK','studio','material','assign','cube','sphere','caption','save','point')})
    bpy.ops.wm.open_mainfile(filepath=str(ASSETS/'w05_procedural_start.blend'))
    nodes=bpy.data.objects['SAMPLE_Work'].active_material.node_tree.nodes
    nodes.remove(nodes['Principled BSDF'])
    save('w05_nodes_start.blend','SAMPLE_Work')

    studio('W05_Face_Slots',6)
    paint=material('MAT_Slot_Paint',(.42,.125,.035),.38)
    material('MAT_Slot_Dark',(.02,.025,.03),.7).use_fake_user=True
    cube('STUDY_Slots',(0,0,1),(.9,.8,.95),paint)
    caption('One mesh, two material slots',(0,-1.4,.07))
    save('w05_slots_start.blend','STUDY_Slots')

    scene=studio('W05_Linear_Color',7.3);scene.render.engine='CYCLES'
    scene.cycles.samples=32;scene.cycles.use_denoising=True
    emitter=material('MAT_Emitter',(.8,.25,.07),.4,Emission_Color=(1,.22,.025,1),Emission_Strength=5)
    sphere('SAMPLE_Emitter',-1.35,emitter,scale=(.95,.95,.95))
    sphere('SAMPLE_Matte',1.35,material('MAT_Matte',(.18,.18,.18),.7),scale=(.95,.95,.95))
    caption('Scene-linear emission',(-1.35,-1.25,.07),.23)
    caption('Matte control',(1.35,-1.25,.07),.23)
    save('w05_color_start.blend','SAMPLE_Emitter')

    # The corresponding images are baked from the source node graph, not guessed.
    scene=studio('W05_Procedural_Image_Methods',7.3)
    source=material('MAT_Procedural_Source',(.2,.3,.25),.5)
    a=cube('SAMPLE_Procedural',(-1.35,0,.85),(.9,.28,.83),source,.06)
    nodes=source.node_tree.nodes;links=source.node_tree.links
    tc=nodes.new('ShaderNodeTexCoord');tc.location=(-850,0)
    noise=nodes.new('ShaderNodeTexNoise');noise.location=(-620,0);noise.inputs['Scale'].default_value=4
    ramp=nodes.new('ShaderNodeValToRGB');ramp.location=(-360,120)
    ramp.color_ramp.elements[0].color=(.08,.12,.09,1);ramp.color_ramp.elements[1].color=(.28,.36,.30,1)
    remap=nodes.new('ShaderNodeMapRange');remap.location=(-330,-220)
    remap.inputs['To Min'].default_value=.35;remap.inputs['To Max'].default_value=.6
    links.new(tc.outputs['UV'],noise.inputs['Vector']);links.new(noise.outputs['Fac'],ramp.inputs['Fac'])
    links.new(noise.outputs['Fac'],remap.inputs['Value'])
    links.new(ramp.outputs['Color'],nodes['Principled BSDF'].inputs['Base Color'])
    links.new(remap.outputs['Result'],nodes['Principled BSDF'].inputs['Roughness'])
    # Smart UV is an authored starting asset; Week 6 teaches the actual operation.
    bpy.ops.object.mode_set(mode='EDIT');bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.uv.smart_project(island_margin=.035);bpy.ops.object.mode_set(mode='OBJECT')
    maps=ASSETS/'textures';maps.mkdir(exist_ok=True)
    scene.render.engine='CYCLES';scene.cycles.samples=1
    scene.cycles.device='CPU';scene.render.bake.margin=16
    output=nodes['Material Output'];bs=nodes['Principled BSDF']
    emit=nodes.new('ShaderNodeEmission');target=nodes.new('ShaderNodeTexImage')
    images={}
    for role,socket in [('color',ramp.outputs['Color']),('roughness',remap.outputs['Result'])]:
        img=bpy.data.images.new('W05_Surface_'+role,1024,1024,alpha=False)
        img.colorspace_settings.name='sRGB' if role=='color' else 'Non-Color'
        target.image=img;nodes.active=target
        links.new(socket,emit.inputs['Color']);links.new(emit.outputs[0],output.inputs['Surface'])
        bpy.ops.object.bake(type='EMIT')
        img.filepath_raw=str(maps/f'w05_surface_{role}.png');img.file_format='PNG';img.save()
        images[role]=img
    nodes.remove(target);nodes.remove(emit);links.new(bs.outputs[0],output.inputs['Surface'])
    image_mat=material('MAT_Image_Result',(.2,.3,.25),.5)
    b=a.copy();b.data=a.data.copy();b.name='SAMPLE_Images';b.location.x=1.35
    bpy.context.collection.objects.link(b);assign(b,image_mat)
    n=image_mat.node_tree.nodes;l=image_mat.node_tree.links
    for role,socket,y in [('color','Base Color',130),('roughness','Roughness',-210)]:
        node=n.new('ShaderNodeTexImage');node.name='Image Color' if role=='color' else 'Image Roughness'
        node.label=node.name;node.image=images[role];node.location=(-340,y)
        l.new(node.outputs['Color'],n['Principled BSDF'].inputs[socket])
    caption('Procedural source',(-1.35,-1.25,.07),.24)
    caption('Saved image maps',(1.35,-1.25,.07),.24)
    scene.render.engine='BLENDER_EEVEE'
    save('w05_image_maps_start.blend','SAMPLE_Images')
    map_paths=[str(v.filepath_raw) for v in images.values()]

    # Render our own original reference in isolation, then show it as an image.
    scene=studio('W05_Original_Reference_Render',3.4)
    reference=material('MAT_Reference_Surface',(.165,.216,.187),.5)
    obj=cube('REFERENCE_Source',(0,0,.95),(.9,.28,.9),reference,.06)
    n=reference.node_tree.nodes;l=reference.node_tree.links
    noise=n.new('ShaderNodeTexNoise');noise.inputs['Scale'].default_value=4
    remap=n.new('ShaderNodeMapRange');remap.inputs['To Min'].default_value=.35;remap.inputs['To Max'].default_value=.6
    l.new(noise.outputs['Fac'],remap.inputs['Value']);l.new(remap.outputs['Result'],n['Principled BSDF'].inputs['Roughness'])
    scene.render.resolution_x=1400;scene.render.resolution_y=1400
    reference_path=maps/'w05_original_surface_reference.png'
    scene.render.filepath=str(reference_path);bpy.ops.render.render(write_still=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(ASSETS/'w05_reference_source.blend'))
    scene=studio('W05_Reference_Recreation',7.3)
    cube('SAMPLE_Work',(-1.35,0,.95),(.9,.28,.9),material('MAT_Reference_Work',(.3,.3,.3),.45),.06)
    bpy.ops.mesh.primitive_plane_add(size=2,location=(1.4,0,1.2))
    card=bpy.context.object;card.name='REF_Surface';card.scale=(1.1,1.1,1.1)
    card.rotation_euler=(scene.camera.location-card.location).to_track_quat('Z','Y').to_euler()
    mat=material('MAT_Reference_Image',(.5,.5,.5));n=mat.node_tree.nodes;n.remove(n['Principled BSDF'])
    tex=n.new('ShaderNodeTexImage');tex.image=bpy.data.images.load(str(reference_path))
    emit=n.new('ShaderNodeEmission');mat.node_tree.links.new(tex.outputs['Color'],emit.inputs['Color'])
    mat.node_tree.links.new(emit.outputs[0],n['Material Output'].inputs['Surface']);assign(card,mat)
    caption('Working material',(-1.35,-1.25,.07),.24);caption('Original reference',(1.4,-1.25,.07),.24)
    save('w05_reference_start.blend','SAMPLE_Work')
    (ASSETS/'prepared_examples.json').write_text(json.dumps({'author':'SECourses','method':'Original Blender geometry and node materials; EMIT-baked corresponding maps','reference':str(reference_path),'maps':map_paths},indent=2))
