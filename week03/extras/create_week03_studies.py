"""Create the six original comparison meshes supplied with Blender Lecture 3.

Open the Lecture 2 station in Blender, then run this script in the Scripting
workspace. It adds hidden study objects to COLLECTION_GUIDES; it does not build
or modify the station. Save a new file afterward. The ready-to-use input file
is supplied for learners who prefer to start directly with the lesson.

Original course geometry; this script may be used, adapted and redistributed.
"""
import math
import bpy

def collection(name):
    result = bpy.data.collections.get(name)
    if result is None:
        result = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(result)
    return result

def mesh(name, verts, faces, location=(0,0,0), edges=(), target='COLLECTION_GUIDES'):
    data = bpy.data.meshes.new(name+'_mesh')
    data.from_pydata(verts, edges, faces)
    data.update()
    obj = bpy.data.objects.new(name,data)
    collection(target).objects.link(obj)
    obj.location = location
    return obj

def prepared_studies():
    # Original, freely distributable test geometry, never a hidden station build.
    radii = [.26,.35,.28,.31,.24,.34,.29,.32]
    ring = [(r*math.cos(i*math.tau/8),r*math.sin(i*math.tau/8),0) for i,r in enumerate(radii)]
    mesh('STUDY_PortLoop',ring,[],(-3,0,.6),[(i,(i+1)%8) for i in range(8)])
    heights = [-.06,.02,.05,-.02,.04,-.04,.06,-.03]
    cap = [(.30*math.cos(i*math.tau/8),.30*math.sin(i*math.tau/8),heights[i]) for i in range(8)]
    mesh('STUDY_FlattenCap',cap,[list(range(8))],(-3,1,.6))
    levels = [0,.06,.18,.60]
    tube = [(.20*math.cos(i*math.tau/8),.20*math.sin(i*math.tau/8),z) for z in levels for i in range(8)]
    quads = [(j*8+i,j*8+(i+1)%8,(j+1)*8+(i+1)%8,(j+1)*8+i) for j in range(3) for i in range(8)]
    mesh('STUDY_LoopSpacing',tube,quads,(-3,2,.4))
    corners = [(-.08,-.08),(.08,-.08),(.08,.08),(-.08,.08)]
    bar = [(x,y,z/8) for z in range(9) for x,y in corners]
    faces = [(j*4+i,j*4+(i+1)%4,(j+1)*4+(i+1)%4,(j+1)*4+i) for j in range(8) for i in range(4)]
    faces += [(3,2,1,0),(32,33,34,35)]
    mesh('STUDY_Handle',bar,faces,(-4,0,0))
    ngon=[(.35*math.cos(i*math.tau/6),.35*math.sin(i*math.tau/6),0) for i in range(6)]
    mesh('STUDY_SubdNgon',ngon,[list(range(6))],(-4,1,.5))
    pole=[(-.4,-.4,0),(.4,-.4,0),(.4,.4,0),(-.4,.4,0),(.12,.04,.18)]
    mesh('STUDY_SubdPole',pole,[(0,1,4),(1,2,4),(2,3,4),(3,0,4)],(-4,2,.5))
    for obj in collection('COLLECTION_GUIDES').objects:
        obj.hide_render=True
        obj.hide_set(True)

if __name__ == '__main__':
    expected = ['STUDY_PortLoop', 'STUDY_FlattenCap', 'STUDY_LoopSpacing',
                'STUDY_Handle', 'STUDY_SubdNgon', 'STUDY_SubdPole']
    existing = [name for name in expected if name in bpy.data.objects]
    if existing:
        raise RuntimeError('Study objects already exist; no changes made: ' + ', '.join(existing))
    if bpy.context.object and bpy.context.object.mode != 'OBJECT':
        raise RuntimeError('Switch to Object Mode before adding the studies; no changes made.')
    prepared_studies()
    assert all(name in bpy.data.objects for name in expected)
    print('Created six hidden study meshes in COLLECTION_GUIDES. Reveal a study in the Outliner when needed.')
