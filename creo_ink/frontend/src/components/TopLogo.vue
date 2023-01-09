<template>
	<body>
		<header>
			<router-link to="/">
				<div class="image-logo">
					<img
						src="../assets/logo-transparent.png"
						width="25"
						height="25"
						alt="image-logo"
					/>
				</div>
				<div class="logo">Creo</div>
			</router-link>
		</header>
	</body>
</template>

<script>
export default {
	name: "TopLogo",
};
</script>

<style scoped lang="scss">
.logo {
	font-family: "Gluten", cursive;
	display: flex;
	align-items: center;
	cursor: pointer;
	margin-right: 100px;
}

.logo img {
	margin-right: 0.5rem;
}
header a {
	display: flex;
	text-align: center;
	align-items: center;
	gap: 0.6em;
	text-decoration: none;
	color: var(--text-clr);
}

header {
	/* background-color: #A9DEF9; */
	/* border-radius: .7em; */
	margin: 1em 1em 0 1em;
	/* width: 9rem; */
	/* padding: .3em;  */
}

header:hover {
	cursor: pointer;
}
</style>
