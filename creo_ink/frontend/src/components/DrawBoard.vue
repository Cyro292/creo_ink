<template>
	<vue-drawing-canvas ref="VueCanvasDrawing" line-join="round" width="1000" />
</template>

<script>
import VueDrawingCanvas from "vue-drawing-canvas";

export default {
	name: "DrawBoard",
	components: {
		VueDrawingCanvas,
	},
};
</script>
