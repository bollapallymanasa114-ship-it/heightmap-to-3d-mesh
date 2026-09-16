const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
camera.position.z = 50;
const geometry = new THREE.BufferGeometry();
const vertices = [];
for (let i = -50; i < 50; i += 2) {
    for (let j = -50; j < 50; j += 2) {
        vertices.push(i, j, Math.sin(i/10) * Math.cos(j/10) * 10);
    }
}
geometry.setAttribute('position', new THREE.BufferAttribute(new Float32Array(vertices), 3));
const material = new THREE.PointsMaterial({ color: 0x0088ff, size: 0.5 });
const mesh = new THREE.Points(geometry, material);
scene.add(mesh);
function animate() {
    requestAnimationFrame(animate);
    mesh.rotation.x += 0.001;
    mesh.rotation.y += 0.001;
    renderer.render(scene, camera);
}
animate();
