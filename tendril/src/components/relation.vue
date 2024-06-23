<template>
    <h1>人間関係図</h1>
    <div id="relation_canvas"></div>
</template>

<script type="module">
import * as THREE from "https://cdn.jsdelivr.net/npm/three@0.164.1/build/three.module.js"

export default {
    name: 'relation_graph',
    props: ["relation_data"],
    methods: {
        main(){
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera();

            const renderer = new THREE.WebGLRenderer();
            renderer.setSize( 700, 700 );
            renderer.setAnimationLoop( animate );
            document.getElementById("relation_canvas").appendChild( renderer.domElement );

            
            var cubes = []
            for(var i=0;i<this.relation_data.length;i++){
                var geometry = new THREE.BoxGeometry( 0.3, 0.3, 0.3 );
                var material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
                var cube = new THREE.Mesh( geometry, material )
                cubes.push(cube);
                cube.position.set(this.relation_data[i][0],this.relation_data[i][1],this.relation_data[i][2]);
                console.log(this.relation_data[i][0],this.relation_data[i][1],this.relation_data[i][2])
                scene.add(cube);
            }

            // camera.position.z = 10;
            var now_camera_rad = 0;

            function animate() {
                now_camera_rad+=0.01
                camera.position.x = Math.sin(now_camera_rad)*5;
                camera.position.z = Math.cos(now_camera_rad)*5;
                camera.lookAt(new THREE.Vector3(0, 0, 0));
                renderer.render( scene, camera );

            }
        }
    },
    mounted() {
        this.main()
    }
}
</script>

<style scoped>
canvas{
    margin:auto 0;
}
</style>