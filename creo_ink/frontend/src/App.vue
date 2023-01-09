<template>
	<TopLogo />
	<NavBar />
	<router-view />
</template>

<script>
import TopLogo from "@/components/TopLogo.vue";
import NavBar from "@/components/NavBar.vue";

export default {
	name: "HomeView",
	components: {
		TopLogo,
		NavBar,
	},
};
</script>

<style lang="scss">
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
}

:root {
	--text-clr: black;
	--text-accent: grey;
	--basic-clr: #f2f2f2;
	--accent-clr1: #b5bed2;
	--accent-clr2: #f0cb5c;
}

body {
	font-family: "Gluten", cursive;
	margin: 0;
	background-color: var(--basic-clr);
}
</style>
