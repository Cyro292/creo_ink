<script>
	export default {
		name: "Notepad",
		props: ['note', 
				'guest', 
				'log', 
				'sign',
				'prename', 
				'surname',
				'username',
				'email',
				'password',
				'newpassword',
				'confirmpassword',
				'blue',
				'violet',
				'click',
				'green',
				'boardname',
				'pin',],
		methods: {
			submitForm() {
				this.$emit('submit', {
        			email: this.email,
        			username: this.username,
					password: this.password,
        			newpassword: this.newpassword,
        			confirmpassword: this.confirmpassword,
      			})
			}
		}		
	};
</script>

<template>
		
		<body class="hero-bg">

			<h2 v-if="wrong" class="wrong">Invalid e-mail or password</h2>

			<div class="notepad">
				<div class="wire-spiral">
					<div class="wires">
						<div v-for=" in 16" class="wire"></div>
					</div>

					<div class="holes">
						<div v-for=" in 16" class="hole"></div>
					</div>
				</div>

				<h2 v-if="note">{{ note }}</h2>

				<form action="">
					<div class="type-area">

						<div class="name">
							<input v-if="prename"
								type="text"
								placeholder="Prename"
							/>
						</div>

						<div class="name">
							<input v-if="surname"
								type="text"
								placeholder="Surname"
							/>
						</div>
						
						<div class="name">
							<input v-if="username"
								type="text"
								placeholder="Username"
								v-bind="username"
							/>
						</div>

						<div class="name">
							<input v-if=email
								type="email"
								placeholder="E-mail"
								v-bind="email"
							/>
						</div>

						<div class="name">
							<input v-if=password
								type="password"
								placeholder="Password"
								v-bind="password"
							/>
						</div>

						<div class="name">
							<input v-if=newpassword
								type="password"
								placeholder="New Password"
								v-bind="newpassword"
							/>
						</div>

						<div class="name">
							<input v-if=confirmpassword
								type="password"
								placeholder="Confirm Password"
								v-bind="confirmpassword"
							/>
						</div>

						<div class="name" v-if=boardname>
							<h2>Enter the board's name</h2>
							<input 
								type="text"
								placeholder="Name"
							/>
						</div>

						<div class="name" v-if=pin>
							<h2>Enter the board's game pin</h2>
							<input 
								type="text"
								placeholder="Game PIN"
							/>
						</div>
					</div>

					<div class="click-area" v-if="click">
						<div class="remember-me">
							<input type="checkbox" name="remember_me" id="remember_me" />
							<label for="remember-me">Remember-me</label>
						</div>

						<div class="confirmation">
							<router-link to="/resetPassword">Forgot Password</router-link>
						</div>
					</div>
				</form>
					
			</div>
			
			<button v-if=violet class="violetbutton">{{ violet }}</button>
			<button v-if=blue class="bluebutton">{{ blue }}</button>
			<button v-if=green class="greenbutton">Sketch!</button>


			<div v-if="guest" class=footer>

				<div class="confirmation">
					<p>{{ guest }}</p>
					<router-link v-if="log" to=/signup>Sign up here</router-link>
					<router-link v-if=sign to="/login">Log in here</router-link>
				</div>

				<div class="or">
					<div class="line"></div>
					<p>OR</p>
					<div class="line"></div>
				</div>

				<button class="guest">Guest • Log in</button>
			</div>
		</body>
	
</template>

<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Gluten&family=Montserrat&display=swap");

/* !!------------------------ notepad -START ----------------------!! */
/* ------------------------------------------------------------------ */



.notepad {
	font-family: 'Gluten', cursive;
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

h2{
    font-size: 1.0rem;
    color: var(--text-accent);
}

.wrong{
	color: red;
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

.name {
	margin: 0 0 1.4em;
}

.type-area label {
	display: block;
}

.type-area input {
	font-family: 'Gluten', cursive;
	font-size: 80%;
    box-sizing: border-box;
    background-color: var(--accent-clr1); 
    color: var(--text-clr);
    border-radius: .6em;
    width: 100%; 
    height: 2.9em;
    padding: 0 .3rem;
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

/* ----------------------------------------------------------- */
/*!! ----------------- notepad - END ---------------------!! */

.bluebutton {
    background-color: var(--accent-clr1);
    color: var(--text-accent);
    font-family: 'Gluten', cursive;
    font-size: 1.1rem;
    
    border-radius: .7em;
    height: 2.2rem;

    margin: 2em 2em;
    margin-inline: auto;
    padding: 0 2rem;
    
    cursor: pointer; 
    display: block;
    border: none;
}

.greenbutton {
    background-color: rgb(48, 230, 87);
    color: var(--text-accent);
    font-family: 'Gluten', cursive;
    font-size: 1.1rem;
    
    border-radius: .7em;
    height: 2.2rem;

    margin: 2em 2em;
    margin-inline: auto;
    padding: 0 2rem;
    
    cursor: pointer; 
    display: block;
    border: none;
}

.greenbutton:hover, button:focus {
    background-color: rgb(48, 230, 87);
}

.bluebutton:hover, button:focus {
    background-color: var(--accent-clr1);
}

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

.violetbutton {
	width: 80%;
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
