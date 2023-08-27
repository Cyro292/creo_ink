<template>
	<div>
		<DrawBoard />
	</div>
</template>

<script>
// @ is an alias to /src
import DrawBoard from "@/components/DrawBoard.vue";

export default {
	name: "DrawBoardView",
	components: {
		DrawBoard,
	},
};
</script>
