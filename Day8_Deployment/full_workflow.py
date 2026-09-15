import numpy as np
import trimesh
import os
from datetime import datetime

def create_heightmap():
    x = np.linspace(-5, 5, 128)
    y = np.linspace(-5, 5, 128)
    X, Y = np.meshgrid(x, y)
    heightmap = 15 * np.exp(-(X**2 + Y**2) / 8)
    return heightmap

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

def repair_mesh(mesh):
    mesh.merge_vertices()
    mesh.remove_degenerate_faces()
    mesh.remove_unreferenced_vertices()
    return mesh

def save_formats(mesh, output_dir, name="mesh"):
    os.makedirs(output_dir, exist_ok=True)
    mesh.export(os.path.join(output_dir, f"{name}.obj"))
    print(f"Saved: {output_dir}/{name}.obj")

def main():
    print("=" * 70)
    print("DAY 8: COMPLETE DEPLOYMENT WORKFLOW")
    print("=" * 70)
    print(f"Timestamp: {datetime.now().isoformat()}\n")
    output_dir = "Day8_Deployment/output"
    try:
        print("[STEP 1] Creating heightmap...")
        heightmap = create_heightmap()
        print(f"Heightmap created: {heightmap.shape}")
        print("\n[STEP 2] Converting to mesh...")
        mesh = heightmap_to_mesh(heightmap)
        print(f"Mesh created: {len(mesh.vertices)} vertices")
        print("\n[STEP 3] Repairing mesh...")
        mesh = repair_mesh(mesh)
        print("Mesh repaired")
        print("\n[STEP 4] Saving mesh...")
        save_formats(mesh, output_dir, "heightmap")
        print("\n" + "=" * 70)
        print("WORKFLOW SUMMARY")
        print("=" * 70)
        print(f"Status: SUCCESS")
        print(f"Output Directory: {output_dir}")
        print(f"Vertices: {len(mesh.vertices)}")
        print(f"Faces: {len(mesh.faces)}")
        print("\n" + "=" * 70)
        print("DAY 8 COMPLETE")
        print("=" * 70)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()