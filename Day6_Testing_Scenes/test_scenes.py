import numpy as np
import trimesh
import os

def create_urban_heightmap(size=256):
    heightmap = np.zeros((size, size))
    heightmap[50:100, 50:100] = 30
    heightmap[150:200, 150:200] = 25
    return np.clip(heightmap, 0, 50)

def create_hilly_heightmap(size=256):
    x = np.linspace(-3, 3, size)
    y = np.linspace(-3, 3, size)
    X, Y = np.meshgrid(x, y)
    heightmap = 20 * np.sin(X) * np.cos(Y) + 10
    return np.clip(heightmap, 0, 50)

def create_flat_heightmap(size=256):
    heightmap = np.ones((size, size)) * 10
    return np.clip(heightmap, 0, 20)

def heightmap_to_mesh(heightmap):
    height, width = heightmap.shape
    x = np.arange(width)
    y = np.arange(height)
    X, Y = np.meshgrid(x, y)
    Z = heightmap
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
    return trimesh.Trimesh(vertices=vertices, faces=np.array(faces))

def main():
    print("=" * 60)
    print("DAY 6: TESTING ON MULTIPLE SCENES")
    print("=" * 60)
    os.makedirs('Day6_Testing_Scenes', exist_ok=True)
    print("\n[SCENE 1] Urban Heightmap")
    urban_hm = create_urban_heightmap(256)
    mesh = heightmap_to_mesh(urban_hm)
    mesh.export('Day6_Testing_Scenes/urban_scene.obj')
    print(f"Urban mesh: {len(mesh.vertices)} vertices")
    print("\n[SCENE 2] Hilly Heightmap")
    hilly_hm = create_hilly_heightmap(256)
    mesh = heightmap_to_mesh(hilly_hm)
    mesh.export('Day6_Testing_Scenes/hilly_scene.obj')
    print(f"Hilly mesh: {len(mesh.vertices)} vertices")
    print("\n[SCENE 3] Flat Heightmap")
    flat_hm = create_flat_heightmap(256)
    mesh = heightmap_to_mesh(flat_hm)
    mesh.export('Day6_Testing_Scenes/flat_scene.obj')
    print(f"Flat mesh: {len(mesh.vertices)} vertices")
    print("\n" + "=" * 60)
    print("DAY 6 COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()