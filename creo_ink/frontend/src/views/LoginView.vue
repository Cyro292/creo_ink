<script>
// @ is an alias to /src
import TopLogo from "@/components/TopLogo.vue";
import NavBar from "@/components/NavBar.vue";

export default {
	name: "Login",
	components: {},
};
</script>

<template>
	<body>
		<h1><span>Go</span> sketching!</h1>

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

				<form action="">
					<div class="type-area">
						<div class="email">
							<input
								type="password"
								placeholder="E-mail"
								name="email-ad"
								id="email-ad"
							/>
						</div>

						<div class="password">
							<input
								type="password"
								placeholder="Password"
								name="password"
								id="password"
							/>
						</div>
					</div>

					<div class="click-area">
						<div class="remember-me">
							<input type="checkbox" name="remember_me" id="remember_me" />
							<label for="remember-me">Remember-me</label>
						</div>

						<div class="confirmation">
							<router-link to="/resetPassword">Forgot Password</router-link>
						</div>
					</div>
				</form>
				<button class="login">Login</button>
			</div>

			<div class="footer">
				<div class="confirmation">
					<p>Don't have an account yet?</p>
					<router-link to="/signup">Sign up here</router-link>
				</div>

				<div class="or">
					<div class="line"></div>
					<p>OR</p>
					<div class="line"></div>
				</div>

				<button class="guest">Guest • Log in</button>
			</div>
		</body>
	</body>
</template>

<style></style>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Gluten&family=Montserrat&display=swap");

/* !!------------------------ notepad -START ----------------------!! */
/* ------------------------------------------------------------------ */

.notepad {
	position: relative;
	background-color: white;
	padding: 2rem 0 3.5rem 0;
	border-bottom-left-radius: 3em;
	border-bottom-right-radius: 3em;
	margin: 3em 1em 1em 1em;
	/* border-left: solid grey .3rem; */
	border-bottom: solid var(--text-accent) 0.4rem;
	border-right: solid var(--text-accent) 0.3rem;
}

/* ------------------------ type-area ---------------------- */

/* ----------------------- WIRE SPIRAL - START------------------------ */

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

/* -----------------------WIRE SPIRAL - END ------------------- */

form {
	text-align: left;
	margin: 0 1em 1em 1em;
}

.password {
	margin: 1em 0;
}

.type-area label {
	display: block;
}

.type-area input {
	box-sizing: border-box;
	/* border: 1.5px solid #D0F4DE; */
	background-color: var(--accent-clr1);
	border-radius: 0.5em;
	width: 100%;
	height: 2.3em;
}

/* ------------------------ click-area ---------------------- */

.click-area {
	display: flex;
	align-items: center;
	justify-content: space-around;
}

.remember-me {
	color: var(--text-accent);
}

.forgot-pwd {
	text-decoration: none;
	color: black;
	font-weight: 600;
}

.forgot-pwd:hover {
	text-decoration: underline;
}

.login {
	width: 90%;
	background-color: var(--accent-clr2);
	color: white;
}

/* ----------------------------------------------------------- */
/*!! ----------------- notepad - END ---------------------!! */

button {
	font-family: "Gluten", cursive;
	font-size: 1.1rem;
	border-radius: 0.7em;
	height: 2.2rem;
	margin-top: 2em;
	margin-inline: auto;
	margin-bottom: 2em;
	cursor: pointer;
	display: block;
	border: none;
}

.log-in {
	width: 90%;
	background-color: var(--accent-clr2);
	color: white;
}

button:hover,
button:focus {
	background-color: var(--accent-clr2);
	color: black;
}

.confirmation {
	display: flex;
	align-items: center;
	justify-content: center;
	gap: 1.4rem;
}

.confirmation p {
	color: var(--text-accent);
}

.confirmation a {
	text-decoration: none;
	font-weight: 600;
	color: black;
}

.confirmation a:hover {
	text-decoration: underline;
}

.or {
	display: flex;
	align-items: center;
	justify-content: center;
	gap: 1rem;
}

.or p {
	color: var(--text-accent);
}

.line {
	background-color: var(--text-accent);
	width: 30%;
	height: 0.3rem;
	border-radius: 0.7rem;
	flex-shrink: 0;
}

.guest {
	padding: 0.5rem 1rem;
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
