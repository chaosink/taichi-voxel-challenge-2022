from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=100)
scene.set_floor(-1000000, (0, 0, 0))
scene.set_background_color((0, 0, 0))

red = vec3(1, 0, 0)
green = vec3(0, 1, 0)
blue = vec3(0, 0, 1)
black = vec3(0, 0, 0)
white = vec3(1, 1, 1)

@ti.func
def draw_voxel(M, p, m, c):
    scene.set_voxel(M @ vec4(p, 1), m, c)

@ti.func
def draw_volume(M, p0, p1, m, c):
    for p in ti.grouped(ti.ndrange((p0[0], p1[0]+1), (p0[1], p1[1]+1), (p0[2], p1[2]+1))):
        draw_voxel(M, p, m, c)

@ti.func
def translation(t):
    return ti.Matrix([[1,0,0,t],[0,1,0,t],[0,0,1,t],[0,0,0,1]])

@ti.kernel
def initialize_voxels():
    S = 4

    M0 = translation((S - 1) // 2)
    l = S - 1
    for i in range(l):
        draw_voxel(M0, (-i, 0, 0), 1, white)
        draw_voxel(M0, ( 0,-i, 0), 1, white)
        draw_voxel(M0, ( 0, 0,-i), 1, white)

    M1 = translation(-(S // 2))
    w = S + 1
    for p in ti.grouped(ti.ndrange((0, w), (0, w))):
        draw_voxel(M1, (  0, p.x, p.y), 1, white)
        draw_voxel(M1, (p.y,   0, p.x), 1, white)
        draw_voxel(M1, (p.x, p.y,   0), 1, white)
    for p in range(0, w - 1):
        draw_voxel(M1, ( 0, p, w), 1, black)
        draw_voxel(M1, ( 0, w, p), 1, black)
        draw_voxel(M1, ( w, 0, p), 1, black)
        draw_voxel(M1, ( p, 0, w), 1, black)
        draw_voxel(M1, ( p, w, 0), 1, black)
        draw_voxel(M1, ( w, p, 0), 1, black)

    s = 3
    draw_volume(ti.Matrix.identity(ti.u32, 4), ( 63, -s, -s), ( 63,  s,  s), 2, red)
    draw_volume(ti.Matrix.identity(ti.u32, 4), ( -s, 63, -s), (  s, 63,  s), 2, green)
    draw_volume(ti.Matrix.identity(ti.u32, 4), ( -s, -s, 63), (  s,  s, 63), 2, blue)

initialize_voxels()

scene.finish()
