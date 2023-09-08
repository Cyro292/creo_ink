<template>
	<NavBar />
	<div class="header">
		<h1>Creo.<span>An endless sketchboard.</span></h1>
		<p class="desc">Designed for intuitive brainstorming and fun tinkering.</p>
		<p class="intro">
			Collaborate in <span>real time</span> or brainstrom with our whiteboard.
		</p>
	</div>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/NavBar.vue";

export default {
	name: "Landing-P",
	components: {
		NavBar,
	},
};
</script>

<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Anton&family=Gloria+Hallelujah&family=Gluten&family=Permanent+Marker&family=Roboto+Mono&display=swap");



.header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: fit-content;
  width: fit-content;
  padding: 20px;
  background-color: #b4ffa8;
  border-radius: 20px;
}
</style>
