# <a name="title">Taichi Voxel Challenge</a>

## RGB Stairs

<p align="center">
<img src="RGB_Stairs.jpg" width="75%"></img>
</p>

## Color Blending

<p align="center">
<img src="Color_Blending.jpg" width="75%"></img>
</p>

## Taichi Logo

<p align="center">
<img src="Taichi_Logo.jpg" width="75%"></img>
</p>

## Penetration

<p align="center">
<img src="Penetration.jpg" width="75%"></img>
</p>

## Lines

<p align="center">
<img src="Lines0.jpg" width="75%"></img>
<img src="Lines1.jpg" width="75%"></img>
<img src="Lines2.jpg" width="75%"></img>
</p>

## Nested Frames

### 2D Sparse/Dense
<p align="center">
<img src="Nested_Frames.2D.Sparse.jpg" width="48%"></img>
<img src="Nested_Frames.2D.Dense.jpg" width="48%"></img>
</p>

### 3D Sparse/Dense
<p align="center">
<img src="Nested_Frames.3D.Sparse.jpg" width="48%"></img>
<img src="Nested_Frames.3D.Dense.jpg" width="48%"></img>
</p>

### 3D Colorful
<p align="center">
<img src="Nested_Frames.3D.Colorful.0.jpg" width="48%"></img>
<img src="Nested_Frames.3D.Colorful.1.jpg" width="48%"></img>
</p>

### 3D Blades
<p align="center">
<img src="Nested_Frames.3D.Blades.jpg" width="32%"></img>
<img src="Nested_Frames.3D.Blades.Colorful.0.jpg" width="32%"></img>
<img src="Nested_Frames.3D.Blades.Colorful.1.jpg" width="32%"></img>
</p>

- - -

We invite you to create your voxel artwork, by putting your [Taichi](https://github.com/taichi-dev/taichi) code in `main.py`!

Rules:

+ You can only import two modules: `taichi` (`pip` installation guide below) and `scene.py` (in the repo).
+ The code in `main.py` cannot exceed 99 lines. Each line cannot exceed 120 characters.

The available APIs are:

+ `scene = Scene(voxel_edges, exposure)`
+ `scene.set_voxel(voxel_id, material, color)`
+ `material, color = scene.get_voxel(voxel_id)`
+ `scene.set_floor(height, color)`
+ `scene.set_directional_light(dir, noise, color)`
+ `scene.set_background_color(color)`

Remember to call `scene.finish()` at last.

**Taichi Lang documentation:** https://docs.taichi-lang.org/

**Modifying files other than `main.py` is not allowed.**


## Installation

Make sure your `pip` is up-to-date:

```bash
pip3 install pip --upgrade
```

Assume you have a Python 3 environment, simply run:

```bash
pip3 install -r requirements.txt
```

to install the dependencies of the voxel renderer.

## Quickstart

```sh
python3 example1.py  # example2/3/.../7/8.py
```

Mouse and keyboard interface:

+ Drag with your left mouse button to rotate the camera.
+ Press `W/A/S/D/Q/E` to move the camera.
+ Press `P` to save a screenshot.

## More examples

<a href="https://github.com/raybobo/taichi-voxel-challenge"><img src="https://github.com/taichi-dev/public_files/blob/master/voxel-challenge/city.jpg" width="45%"></img></a>  <a href="https://github.com/victoriacity/voxel-challenge"><img src="https://github.com/taichi-dev/public_files/blob/master/voxel-challenge/city2.jpg" width="45%"></img></a>
<a href="https://github.com/yuanming-hu/voxel-art"><img src="https://github.com/taichi-dev/public_files/blob/master/voxel-challenge/tree2.jpg" width="45%"></img></a> <a href="https://github.com/neozhaoliang/voxel-challenge"><img src="https://github.com/taichi-dev/public_files/blob/master/voxel-challenge/desktop.jpg" width="45%"></img></a>
<a href="https://github.com/maajor/maajor-voxel-challenge"><img src="https://github.com/taichi-dev/public_files/blob/master/voxel-challenge/earring_girl.jpg" width="45%"></img></a>  <a href="https://github.com/rexwangcc/taichi-voxel-challenge"><img src="https://github.com/taichi-dev/public_files/blob/master/voxel-challenge/pika.jpg" width="45%"></img></a>
<a href="https://github.com/houkensjtu/qbao_voxel_art"><img src="https://github.com/taichi-dev/public_files/blob/master/voxel-challenge/yinyang.jpg" width="45%"></img></a>  <a href="https://github.com/ltt1598/voxel-challenge"><img src="https://github.com/taichi-dev/public_files/blob/master/voxel-challenge/lang.jpg" width="45%"></img></a>

## Show your artwork

Please put your artwork at the beginning of this README file. Replacing the `demo.jpg` file with your creation will do the job.
