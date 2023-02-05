<script>
// @ is an alias to /src
import TopLogo from "@/components/TopLogo.vue";
import Notepad from "@/components/Notepad.vue";

export default {
	name: "Notepadtest",
	components: {
		Notepad
	},
};
</script>

<template>
	<body>
		<TopLogo />

		<h1><span>Go</span> sketching!</h1>

		<Notepad
			note="Hallo"
			guest="Don't have an account yet?"
			log="1"
			prename="1"
			surname="1"
			click="1"
			blue="Log in"
			violet="Sign up"
		/>
	</body>
</template>

<style>
:root {
	--text-clr: black;
	--text-accent: grey;
	--basic-clr: #fffbd7;
	--accent-clr1: #a9def9;
	--accent-clr2: #ca72ff;
}

body {
	font-family: "Gluten", cursive;
	margin: 0;
	background-color: var(--basic-clr);
}
</style>
