from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=10000)
scene.set_floor(-1, (1, 1, 1))
scene.set_background_color((0.000001, 0.000001, 0.000001))

red = vec3(1, 0, 0)
green = vec3(0, 1, 0)
blue = vec3(0, 0, 1)
black = vec3(0, 0, 0)
white = vec3(1, 1, 1)

@ti.func
def draw_volume(M, p0, p1, m, c):
    for p in ti.grouped(ti.ndrange((p0.x, p1.x+1), (p0.y, p1.y+1), (p0.z, p1.z+1))):
        scene.set_voxel(M @ vec4(p, 1), m, c)

@ti.func
def translation(x, y, z):
    return ti.Matrix([[1, 0, 0, x],[0, 1, 0, y],[0, 0, 1, z],[0, 0, 0, 1]])

@ti.func
def random_color_normalized():
    return vec3([ti.random() for i in range(3)]).normalized()

@ti.func
def draw_spot(M, l, c):
    draw_volume(M, ivec3(-1, 1-l,-1), ivec3( 1, 0, 1), 1, black)
    draw_volume(M, ivec3( 0, 1-l, 0), ivec3( 0, 1, 0), 0, black)
    draw_volume(M, ivec3( 0,   0, 0), ivec3( 0, 0, 0), 2, c)

@ti.kernel
def initialize_voxels():
    for x, z in ti.ndrange((-62, 63), (-62, 63)):
        if x % 2 == 0 and z % 2 == 0:
            draw_spot(translation(x, 63, z), 32, random_color_normalized())

initialize_voxels()

scene.finish()
