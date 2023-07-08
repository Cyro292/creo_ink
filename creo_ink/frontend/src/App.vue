<template>
	<NavBar />
	<div class="pad">
		<router-view />
	</div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";

export default {
	name: "HomeView",
	components: {
		NavBar,
	},
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Gluten&family=Montserrat&display=swap");

#app {
	font-family: 'Gluten', cursive;
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
	margin-top: 4em;
	background-color: var(--basic-clr);
}

.pad{
	padding: 3em;
}

:root {
	--text-clr: black;
	--text-accent: grey;
	--basic-clr: #fffbd7;
	--accent-clr1: #a9def9;
	--accent-clr2: #ca72ff;
	--accent-clr3: rgb(74, 222, 74);
	--accent-clr1-dark: #61c1f1;
	--accent-clr2-dark: #b250ef;
	--accent-clr3-dark: rgb(31, 202, 31);
}

</style>
