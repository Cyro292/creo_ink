<template>
	<nav class="navbar">
		<li class="logo">
			<router-link to="/">
				<div class="image-logo">
					<img
						src="../assets/logo-transparent-gelb.png"
						width="25"
						height="25"
						alt="image-logo"
					/>
				</div>
				<div class="text-logo">Creo</div>
			</router-link>
		</li>

		<ul class="nav-links">
			<div class="menu">
				<li class="home"><router-link to="/">Home</router-link></li>
				<li class="boards">
					<router-link to="/drawboard">Sketchboard</router-link>
				</li>
				<li class="boards">
					<router-link to="/joinboard">Join Board</router-link>
				</li>
				<li class="boards">
					<router-link to="/boardcollection">Your Boards</router-link>
				</li>
				<li class="login"><router-link to="/login">Login</router-link></li>
			</div>
		</ul>
	</nav>
</template>

<script>
import TopLogo from "@/components/TopLogo.vue";

export default {
	name: "NavBar",
	components: {
		TopLogo,
	},
};
</script>

<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Gluten&family=Montserrat&display=swap");

* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}

a {
	text-decoration: none;
}

li {
	list-style: none;
}

.text-logo {
	font-family: "Gluten", cursive;
	font-size: 0.7em;
	display: flex;
	align-items: center;
	cursor: pointer;
	margin-right: 100px;
	color: var(--basic-clr);
}

.logo img {
	height: 0.9em;
	width: 0.9em;
}
.logo a {
	display: flex;
	text-align: center;
	align-items: center;
	gap: 0.6em;
	text-decoration: none;
}

.logo:hover {
	cursor: pointer;
}

.navbar {
	font-family: "Gluten", cursive;
	position: fixed;
	top: 0px;
	width: 100%;
	opacity: 82%;
	display: flex;
	align-items: center;
	justify-content: space-between;
	padding: 20px;
	background-color: rgb(0, 0, 0);
	color: var(--basic-clr);
	z-index: 10;
}

.nav-links a {
	color: var(--basic-clr);
}

.logo {
	font-size: 32px;
}

.menu {
	display: flex;
	gap: 1em;
	font-size: 1.1em;
}

.nav-links a:hover {
	font-size: larger;
}

.menu li {
	line-height: 1.5em;
	padding: 5px 14px;
	text-align: center;
}

.home {
	width: 4em;
}

.boards {
	width: 9em;
}

.login {
	width: 4.8em;
}
</style>
