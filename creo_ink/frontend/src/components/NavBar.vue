<template>
	<nav>
		<ul class="nav__list">
			<li>
				<router-link to="/"><b>Home</b> </router-link>
			</li>
			<!-- <li><router-link to="/" tag="#WIC">What is Creo</router-link></li>
			<li><router-link to="/" tag="#about_us">About Us</router-link></li> -->
			<li>
				<router-link to="/login">Login</router-link>
			</li>
		</ul>
	</nav>
</template>

<script>
export default {
	name: "NavBar",
	components: {},
};
</script>

<style scoped lang="scss">
nav {
	display: flex;
	align-items: center;
	padding: 30px 3%;
	margin-bottom: 20px;
	background: var(--accent-clr1);
}

.nav__list a {
	font-weight: 400;
	color: var(--text-accent);
}

a {
	font-family: "Roboto Mono", monospace;
	text-decoration: none;
	color: var(--text-clr);
}

.nav__list {
	display: inline-block;
	list-style: none;
}

.nav__list li {
	display: inline-block;
	padding: 0px 20px;
}

.nav__list a:hover {
	color: var(--text-clr);
}
</style>
