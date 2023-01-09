<script>
// @ is an alias to /src
import TopLogo from "@/components/TopLogo.vue";

export default {
	name: "NewPassword",
	components: {},
};
</script>

<template>
	<body>
		<h1><span>Create new</span> password</h1>

		<body class="hero-bg">
			<div class="notepad">
				<div class="wire-spiral">
					<div class="wires">
						<div v-for=" in 16" class="wire"></div>
					</div>

					<div class="holes">
						<div v-for=" in 16" class="hole"></div>
					</div>
				</div>

				<h2>
					Use 8 or more characters with a mix of letters, numbers & symbols.
				</h2>
				<!-- - passord recommendation checker(show what is not yet fullfilled)-->

				<form mehtod="POST" action="accounts/login">
					<div class="type-area">
						<div class="new-password">
							<input
								type="password"
								placeholder="New Password"
								id="new-password"
							/>
						</div>

						<div class="confirm-password">
							<input
								type="password"
								placeholder="Confirm Password"
								id="confirm-password"
							/>
						</div>
					</div>
				</form>
			</div>

			<button class="log-in">Log in</button>
		</body>
	</body>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Gluten&family=Montserrat&display=swap");

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

header a {
	display: flex;
	text-align: center;
	align-items: center;
	gap: 0.6em;
	text-decoration: none;
	color: var(--text-clr);
}

header {
	margin: 1em 1em 0 1em;
}

header:hover {
	cursor: pointer;
}

.hero-bg {
	text-align: center;
}

h1 {
	font-size: 2.5rem;
	margin: 2em 0 1.2em;
}

h1 span {
	display: block;
}

/* !!------------------------ notepad ↓↓↓↓ ----------------------!! */
/* ------------------------------------------------------------------ */

h2 {
	font-size: 0.8rem;
	color: var(--text-accent);
}

.notepad {
	position: relative;
	background-color: white;
	padding: 2rem 0 2rem 0;
	margin: 3em 1em 1em 1em;

	border-bottom-left-radius: 3em;
	border-bottom-right-radius: 3em;
	border-bottom: solid var(--text-accent) 0.4rem;
	border-right: solid var(--text-accent) 0.3rem;
}

/* ----------------------- WIRE SPIRAL - ↓↓↓↓↓↓↓------------------------ */

.wire-spiral {
	width: 100%;
	position: absolute;
	top: 0;
}

.wires {
	position: absolute;
	top: -0.8rem;
	display: flex;
	justify-content: space-around;
	width: 100%;
	z-index: 1;
}

.wire {
	background-color: var(--text-clr);
	width: 0.3rem;
	height: 1.5rem;
	border-radius: 0.5rem;
}

.holes {
	position: absolute;
	top: 0.25rem;
	display: flex;
	justify-content: space-around;
	width: 100%;
}

.hole {
	border-radius: 45%;
	border: solid 0.15em;
	background-color: white;
	width: 0.4rem;
	height: 0.4rem;
}

-------------------------------- form {
	text-align: left;
	margin: 0 1em 1em 1em;
}

.new-password {
	margin: 1rem 0;
}

.confirm-password {
	margin: 2em 0;
}

.type-area input {
	font-family: "Gluten", cursive;
	box-sizing: border-box;
	background-color: var(--accent-clr1);
	color: var(--text-clr);
	border-radius: 0.5em;
	width: 90%;
	height: 2.3em;
	padding: 0 0.3rem;
}

/* ----------------------------------------------------------- */
/*!! ----------------- notepad - END ---------------------!! */

button {
	background-color: var(--accent-clr1);
	color: var(--text-accent);
	font-family: "Gluten", cursive;
	font-size: 1.1rem;

	border-radius: 0.7em;
	height: 2.2rem;

	margin: 2em 2em;
	margin-inline: auto;
	padding: 0 2rem;

	cursor: pointer;
	display: block;
	border: none;
}

button:hover,
button:focus {
	color: var(--text-clr);
}

@media (min-width: 600px) {
	body {
		background-color: var(--basic-clr);
	}
	.hero-bg {
		margin-top: auto;
		margin-bottom: auto;
		background-color: var(--basic-clr);
		margin-inline: auto;
		max-width: 400px;
	}
}
</style>
