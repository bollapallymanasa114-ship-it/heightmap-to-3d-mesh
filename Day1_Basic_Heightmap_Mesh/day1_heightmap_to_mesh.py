import numpy as np
import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_dummy_heightmap(width=100, height=100, scale=1.0):
    x = np.linspace(-5, 5, width)
    y = np.linspace(-5, 5, height)
    X, Y = np.meshgrid(x, y)
    heightmap = scale * np.exp(-(X**2 + Y**2) / 5)
    return heightmap

def heightmap_to_mesh(heightmap, scale_z=1.0):
    height, width = heightmap.shape
    x = np.arange(width)
    y = np.arange(height)
    X, Y = np.meshgrid(x, y)
    Z = heightmap * scale_z
    vertices = np.column_stack([X.ravel(), Y.ravel(), Z.ravel()])
    faces = []
    for i in range(height - 1):
        for j in range(width - 1):
            v0 = i * width + j
            v1 = i * width + (j + 1)
            v2 = (i + 1) * width + j
            v3 = (i + 1) * width + (j + 1)
            faces.append([v0, v2, v1])
            faces.append([v1, v2, v3])
    faces = np.array(faces)
    mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
    return mesh

def visualize_heightmap(heightmap):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    height, width = heightmap.shape
    x = np.arange(width)
    y = np.arange(height)
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, heightmap, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Height')
    ax.set_title('Heightmap Visualization')
    plt.show()

def main():
    print("=" * 60)
    print("DAY 1: BASIC HEIGHTMAP TO MESH CONVERSION")
    print("=" * 60)
    print("\n[STEP 1] Creating dummy heightmap...")
    heightmap = create_dummy_heightmap(width=100, height=100, scale=10)
    print(f"Heightmap shape: {heightmap.shape}")
    print("\n[STEP 2] Converting heightmap to mesh...")
    mesh = heightmap_to_mesh(heightmap, scale_z=1.0)
    print(f"Mesh vertices: {len(mesh.vertices)}")
    print(f"Mesh faces: {len(mesh.faces)}")
    print("\n[STEP 3] Saving mesh...")
    mesh.export('day1_heightmap_mesh.obj')
    print("Mesh saved as 'day1_heightmap_mesh.obj'")
    print("\n" + "=" * 60)
    print("DAY 1 COMPLETE")
    print("=" * 60)
    return mesh, heightmap

if __name__ == "__main__":
    mesh, heightmap = main()