<script>
// @ is an alias to /src

export default {
	name: "ResetPasword",
	components: {},
};
</script>

<template>
	<body>
		<body class="hero-bg">
			<h1><span>Reset your</span> password</h1>

			<div class="notepad">
				<h3>
					Enter your email and we'll send you instructions on how to reset your
					password.
				</h3>

				<form action="">
					<div class="type-area">
						<div class="field_1">
							<input
								type="email"
								placeholder="Enter e-mail"
								name="input"
								id="email-id"
							/>
						</div>
					</div>
				</form>

				<button class="send">Send</button>
			</div>
		</body>
	</body>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Gluten&family=Montserrat&display=swap");

* {
	font-family: "Gluten", cursive;
	margin: 0;
	background-color: var(--basic-clr);
	box-sizing: border-box;
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

.notepad {
	text-align: center;
}

h3 {
	font-weight: 200;
	font-size: 1rem;
}

form {
	margin: 0 1em 1em 1em;
}

.type-area input {
	box-sizing: border-box;
	background-color: transparent;

	border: solid var(--accent-clr1) 0.3rem;
	border-radius: 0.5em;
	width: 90%;
	height: 2.5em;
}

.field_1 {
	margin-top: 1rem;
}

/* ----------------------------------------------------------- */
/*!! ----------------- notepad - END ---------------------!! */

button {
	background-color: var(--accent-clr2);
	color: white;
	font-family: "Gluten", cursive;
	font-size: 1.1rem;
	text-align: center;

	border-radius: 0.7em;
	height: 2.2rem;

	margin: 2rem 0;

	padding: 5px 50px;

	cursor: pointer;
	border: none;
}

button:hover,
button:focus {
	color: black;
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
