<template>
    <h1>人間関係図</h1>
    <div id="relation_canvas"></div>
</template>

<script type="module">
import * as THREE from "https://cdn.jsdelivr.net/npm/three@0.164.1/build/three.module.js"

export default {
    name: 'relation_graph',
    methods: {
        main: ()=>{
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera();

            const renderer = new THREE.WebGLRenderer();
            renderer.setSize( 700, 700 );
            renderer.setAnimationLoop( animate );
            document.getElementById("relation_canvas").appendChild( renderer.domElement );

            const geometry = new THREE.BoxGeometry( 1, 1, 1 );
            const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
            const cube = new THREE.Mesh( geometry, material );
            scene.add( cube );

            camera.position.z = 5;

            function animate() {

                cube.rotation.x += 0.01;
                cube.rotation.y += 0.01;

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