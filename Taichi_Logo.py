from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=100000)
scene.set_floor(-4, (1, 1, 1))
scene.set_background_color((0.000001, 0.000001, 0.000001))

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
def draw_spot(M, l, c):
    draw_volume(M, ivec3(-1, 1-l,-1), ivec3( 1, 0, 1), 1, black)
    draw_volume(M, ivec3( 0, 1-l, 0), ivec3( 0, 1, 0), 0, black)
    draw_volume(M, ivec3( 0,   0, 0), ivec3( 0, 0, 0), 2, c)

@ti.kernel
def initialize_voxels():
    for x, z in ti.ndrange((-62, 63), (-62, 63)):
        if x % 2 == 0 and z % 2 == 0:
            draw_spot(translation(x, 63, z), 48, white)
    for x, z in ti.ndrange((-61, 62), (-61, 62)):
        if x % 2 == 0 and z % 2 == 0 \
        and vec2(x,    z   ).norm() < 61 \
        and vec2(x- 4, z-26).norm() > 39 \
        and(vec2(x+ 6, z+38).norm() < 24 or x < 0) \
        or  vec2(x-40, z- 4).norm() < 20 \
        and(vec2(x-32, z+18).norm() > 20 or x > 49) \
        and(vec2(x-44, z-12).norm() < 12 or x > 44):
            draw_spot(translation(x, 63, z), 48, black)

initialize_voxels()

scene.finish()
