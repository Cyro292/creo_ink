<template>
	<div>
		<DrawBoard />
	</div>
</template>

<script>
// @ is an alias to /src
import DrawBoard from "@/components/DrawBoard.vue";
import MsDrawBoard from "msdrawboard";

export default {
	name: "DrawBoardView",
	components: {
		MsDrawBoard,
	},
};
</script>
