<template>
	<div class="drawboard">
		<ExcalidrawVue />
	</div>
</template>

<script>
import { applyPureReactInVue } from "veaury";
import ExcalidrawIntegration from "@/components/ExcalidrawIntegration.jsx";

export default {
	components: {
		ExcalidrawVue: applyPureReactInVue(ExcalidrawIntegration),
	},
};
</script>

<style>
.drawboard {
	top: 0px;
	left: 0px;
	width: 100vw;
	height: 100vh;
	position: static;
}
</style>
