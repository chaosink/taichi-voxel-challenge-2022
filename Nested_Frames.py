from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=1)
scene.set_floor(-1000000, (1, 1, 1))
scene.set_background_color((0, 0, 0))

black = vec3(0, 0, 0)
white = vec3(1, 1, 1)

@ti.func
def draw_voxel(M, p, m, c):
    for x, y, z in ti.ndrange((0, 2), (0, 2), (0, 2)):
        P = M @ vec4(vec3(p) + vec3(x, y, z) * 0.5 - 0.25, 1)
        C = c                        # use specified color
        # C = abs(P / 64) ** 1.2       # use spatial color 0
        # C = (1 - abs(P / 64)) ** 0.8 # use spatial color 1
        scene.set_voxel(P, m, C)

@ti.func
def draw_frame(M, m, c):
    for i in range(-64, 64):
        draw_voxel(M, (  i,-64,-64), m, c)
        draw_voxel(M, (  i, 63, 63), m, c)
        draw_voxel(M, (  i,-64, 63), m, c)
        draw_voxel(M, (  i, 63,-64), m, c)

        draw_voxel(M, (-64,  i,-64), m, c)
        draw_voxel(M, ( 63,  i, 63), m, c)
        draw_voxel(M, (-64,  i, 63), m, c)
        draw_voxel(M, ( 63,  i,-64), m, c)

        draw_voxel(M, (-64,-64,  i), m, c)
        draw_voxel(M, ( 63, 63,  i), m, c)
        draw_voxel(M, (-64, 63,  i), m, c)
        draw_voxel(M, ( 63,-64,  i), m, c)

@ti.func
def draw_cube(M, m, c):
    for x, y, z in ti.ndrange((-64, 64), (-64, 64), (-64, 64)):
        draw_voxel(M, (x, y, z), m, c)

@ti.func
def scale(x, y, z):
    return ti.Matrix([[x,0,0,0],[0,y,0,0],[0,0,z,0],[0,0,0,1]])

@ti.func
def rotation(axis, r):
    v = vec3(axis).normalized()
    a = ti.cos(r/2)
    b, c, d = -v*ti.sin(r/2)
    aa, bb, cc, dd = a*a, b*b, c*c, d*d
    bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
    return ti.Matrix([[aa+bb-cc-dd,   2*(bc+ad),   2*(bd-ac), 0],
                      [  2*(bc-ad), aa+cc-bb-dd,   2*(cd+ab), 0],
                      [  2*(bd+ac),   2*(cd-ab), aa+dd-bb-cc, 0],
                      [          0,           0,           0, 1]])

@ti.func
def random_color_normalized():
    return vec3([ti.random() for i in range(3)]).normalized()

@ti.kernel
def initialize_voxels():
    # s = 0.95 # sparse
    s = 0.99 # dense
    r = ti.atan2(0.5-ti.sqrt(2*s*s-1)*0.5, 0.5+ti.sqrt(2*s*s-1)*0.5)
    M = ti.Matrix.identity(float, 4)
    S = [(1,s,s), (s,1,s), (s,s,1)]
    V = [(1,0,0), (0,1,0), (0,0,1)]

    # 3D
    l = 200
    # l = 50
    ti.loop_config(serialize=True)
    for i in range(l):
        for j in ti.static(range(3)):
            c = ((i*3+0) / l / 3) ** 0.8
            C = mix(black, white, c)
            draw_frame(M, 2, C)
            M = scale(*S[j]) @ rotation(V[j], r) @ M

    # 2D
    # l = ti.log(1/128) / ti.log(s)
    # # l = 50
    # ti.loop_config(serialize=True)
    # for i in range(l):
    #     c = (i / l) ** 0.8
    #     C = mix(black, white, c)
    #     draw_frame(M, 2, C)
    #     M = scale(*S[1]) @ rotation(V[1], r) @ M

    draw_cube(M, 2, white)

initialize_voxels()
scene.finish()
