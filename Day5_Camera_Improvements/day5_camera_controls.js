class CameraManager {
    constructor() {
        this.presets = {
            overview: { x: 80, y: 80, z: 80 },
            topdown: { x: 0, y: 120, z: 0 },
            sideview: { x: 120, y: 40, z: 0 }
        };
    }
}
window.CameraManager = CameraManager;