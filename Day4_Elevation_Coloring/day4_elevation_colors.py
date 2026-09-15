import numpy as np
import trimesh
import os

def apply_elevation_colors(mesh, heightmap, normalize=True):
    height, width = heightmap.shape
    heights = heightmap.ravel()
    if normalize:
        heights_norm = (heights - heights.min()) / (heights.max() - heights.min() + 1e-6)
    else:
        heights_norm = heights
    colors = np.zeros((len(heights_norm), 3), dtype=np.uint8)
    colors[:, 0] = (heights_norm * 255).astype(np.uint8)
    colors[:, 1] = ((1 - heights_norm) * 255).astype(np.uint8)
    colors[:, 2] = 128
    mesh.visual.vertex_colors = colors
    return mesh

def main():
    print("=" * 60)
    print("DAY 4: ELEVATION-BASED COLORING")
    print("=" * 60)
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    heightmap = 10 * np.exp(-(X**2 + Y**2) / 5)
    height, width = heightmap.shape
    x_coords = np.arange(width)
    y_coords = np.arange(height)
    X_mesh, Y_mesh = np.meshgrid(x_coords, y_coords)
    vertices = np.column_stack([X_mesh.ravel(), Y_mesh.ravel(), heightmap.ravel()])
    faces = []
    for i in range(height - 1):
        for j in range(width - 1):
            v0 = i * width + j
            v1 = i * width + (j + 1)
            v2 = (i + 1) * width + j
            v3 = (i + 1) * width + (j + 1)
            faces.append([v0, v2, v1])
            faces.append([v1, v2, v3])
    mesh = trimesh.Trimesh(vertices=vertices, faces=np.array(faces))
    os.makedirs('Day4_Elevation_Coloring', exist_ok=True)
    mesh_colored = apply_elevation_colors(mesh.copy(), heightmap)
    mesh_colored.export('Day4_Elevation_Coloring/mesh_colored.obj')
    print("Colored mesh created and saved")
    print("=" * 60)
    print("DAY 4 COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()