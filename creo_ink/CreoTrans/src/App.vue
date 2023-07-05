<script>
// import $ from "jquery";

import Canvas from './components/Canvas.vue'
import ButtonCenter from './components/Buttoncenter.vue';


export default {
  name:'App',
  components: {
    Canvas,
    ButtonCenter,
  }
}


</script>

<template>
  <Canvas />
  <ButtonCenter />

</template>

<style>
  html {
    zoom: 60%;
  }
</style>


