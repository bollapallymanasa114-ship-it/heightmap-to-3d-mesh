import numpy as np
import trimesh
import os

def load_or_create_depth_map(width=512, height=512):
    x = np.linspace(-1, 1, width)
    y = np.linspace(-1, 1, height)
    X, Y = np.meshgrid(x, y)
    depth = 100 * (1 - np.sqrt(X**2 + Y**2))
    depth = np.clip(depth, 0, 255).astype(np.uint8)
    return depth

def create_texture_image(size=(512, 512)):
    from PIL import Image
    texture = Image.new('RGB', size)
    pixels = texture.load()
    for i in range(size[1]):
        for j in range(size[0]):
            r = int(255 * (j / size[0]))
            g = int(255 * (i / size[1]))
            b = 128
            pixels[j, i] = (r, g, b)
    texture.save('sample_texture.png')
    return texture

def depth_to_mesh_with_texture(depth_map, depth_scale=0.1):
    height, width = depth_map.shape
    depth_normalized = depth_map.astype(np.float32) / 255.0
    x = np.arange(width, dtype=np.float32)
    y = np.arange(height, dtype=np.float32)
    X, Y = np.meshgrid(x, y)
    Z = depth_normalized * depth_scale
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
    mesh = trimesh.Trimesh(vertices=vertices, faces=faces, process=False)
    return mesh

def main():
    print("=" * 60)
    print("DAY 2: DEPTH MAP TO TEXTURED MESH")
    print("=" * 60)
    print("\n[STEP 1] Loading depth map...")
    depth_map = load_or_create_depth_map(512, 512)
    print(f"Depth map shape: {depth_map.shape}")
    print("\n[STEP 2] Creating texture...")
    texture = create_texture_image(size=(512, 512))
    print(f"Texture created")
    print("\n[STEP 3] Converting depth to mesh...")
    mesh = depth_to_mesh_with_texture(depth_map, depth_scale=0.1)
    print(f"Mesh vertices: {len(mesh.vertices)}")
    print(f"Mesh faces: {len(mesh.faces)}")
    print("\n[STEP 4] Saving mesh...")
    os.makedirs('Day2_Depth_to_Mesh', exist_ok=True)
    mesh.export('Day2_Depth_to_Mesh/mesh.obj')
    print("Mesh saved")
    print("\n" + "=" * 60)
    print("DAY 2 COMPLETE")
    print("=" * 60)
    return mesh, depth_map, texture

if __name__ == "__main__":
    mesh, depth_map, texture = main()