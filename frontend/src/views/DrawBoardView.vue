<template>
	<div class="drawboard">
		<ExcalidrawVue></ExcalidrawVue>
	</div>
</template>
<script>
import { applyReactInVue } from "veaury";
import { Excalidraw } from "@excalidraw/excalidraw";

export default {
	components: {
		ExcalidrawVue: applyReactInVue(Excalidraw),
	},
};
</script>

<style>
.drawboard {
	width: 100vw;
	height: 100vh;
}
</style>
