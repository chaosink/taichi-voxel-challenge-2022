from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=1)
scene.set_floor(-1000000, (0, 0, 0))
scene.set_background_color((0, 0, 0))

black = vec3(0, 0, 0)

@ti.func
def valid(p):
    return p.x >= -64 and p.x <= 63 \
       and p.y >= -64 and p.y <= 63 \
       and p.z >= -64 and p.z <= 63

@ti.func
def draw_voxel(M, p, m, c):
    q = M @ vec4(p, 1)
    if valid(q):
        scene.set_voxel(q, m, c)

@ti.func
def translation(x, y, z):
    return ti.Matrix([[1,0,0,x],[0,1,0,y],[0,0,1,z],[0,0,0,1]])

@ti.func
def random_color_normalized():
    return vec3([ti.random() for i in range(3)]).normalized()

@ti.kernel
def initialize_voxels():
    for p in ti.grouped(ti.ndrange((-64, 64), (-64, 64))):
        draw_voxel(translation(p.x, -p.x, 0), (-p.y, 0, p.y), 2, random_color_normalized())
        draw_voxel(translation(p.x,1-p.x, 0), (-p.y, 0, p.y), 1, black)

initialize_voxels()

scene.finish()
