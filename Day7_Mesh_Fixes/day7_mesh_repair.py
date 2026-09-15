import numpy as np
import trimesh
import os

def fix_mesh_holes(mesh):
    print("Repairing mesh...")
    mesh.merge_vertices()
    print("Removed duplicate vertices")
    mesh.remove_degenerate_faces()
    print("Removed degenerate faces")
    mesh.remove_unreferenced_vertices()
    print("Cleaned unreferenced vertices")
    return mesh

def main():
    print("=" * 60)
    print("DAY 7: MESH REPAIR AND OPTIMIZATION")
    print("=" * 60)
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    heightmap = 10 * np.exp(-(X**2 + Y**2) / 5)
    height, width = heightmap.shape
    vertices = np.column_stack([X.ravel(), Y.ravel(), heightmap.ravel()])
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
    print(f"Test mesh: {len(mesh.vertices)} vertices, {len(mesh.faces)} faces")
    mesh_repaired = fix_mesh_holes(mesh.copy())
    os.makedirs('Day7_Mesh_Fixes', exist_ok=True)
    mesh_repaired.export('Day7_Mesh_Fixes/mesh_repaired.obj')
    print("Repaired mesh saved")
    print("\n" + "=" * 60)
    print("DAY 7 COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()