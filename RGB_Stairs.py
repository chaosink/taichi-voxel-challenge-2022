from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=500)
scene.set_floor(-1000000, (0, 0, 0))
scene.set_background_color((0.0001, 0.0001, 0.0001))

red = vec3(1, 0, 0)
green = vec3(0, 1, 0)
blue = vec3(0, 0, 1)
white = vec3(1, 1, 1)

@ti.func
def draw_volume(p0, p1, m, c):
    for p in ti.grouped(ti.ndrange((p0.x, p1.x+1), (p0.y, p1.y+1), (p0.z, p1.z+1))):
        scene.set_voxel(p, m, c)

@ti.func
def draw_tetrahedron(p, r, m, c):
    for o in ti.grouped(ti.ndrange((0, r+1), (0, r+1), (0, r+1))):
        if o.sum() < r:
           scene.set_voxel(p + o, m, c)

@ti.kernel
def initialize_voxels():
    draw_tetrahedron(vec3(0, 0, 0), 7, 1, white)

    s = 3
    draw_volume(ivec3( 63, -s, -s), ivec3( 63,  s,  s), 2, red)
    draw_volume(ivec3( -s, 63, -s), ivec3(  s, 63,  s), 2, green)
    draw_volume(ivec3( -s, -s, 63), ivec3(  s,  s, 63), 2, blue)

initialize_voxels()

scene.finish()
