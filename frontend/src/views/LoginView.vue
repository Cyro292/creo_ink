<template>
	<div class="background">
		<div class="container" :class="{ active: animationActive }">
			<div class="top"></div>
			<div class="bottom"></div>
			<div class="center">
				<h2 class="text-center">Please Sign In</h2>
				<form @submit.prevent="login">
					<div class="form-group">
						<input
							v-model="email"
							type="email"
							class="form-control"
							id="email"
							required
							placeholder="name@example.com"
							@focus="toggleAnimation"
						/>
						<input
							v-model="password"
							type="password"
							class="form-control"
							id="password"
							required
							placeholder="password"
							@focus="toggleAnimation"
						/>
					</div>
					<router-link to="/signup"
						>Don't have an account? Sign up here!</router-link
					>
					<div class="text-danger" v-if="errorMessage">{{ errorMessage }}</div>
					<button type="submit" class="btn btn-primary">Login</button>
				</form>
				<h2>&nbsp;</h2>
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";

export default {
	data() {
		return {
			email: "",
			password: "",
			errorMessage: "",
			animationActive: false,
		};
	},

	methods: {
		toggleAnimation() {
			this.animationActive = true;
		},
		async login() {
			console.log(this.email, this.password);
			try {
				const response = await axios.post("/api/login/", {
					email: this.email,
					password: this.password,
				});

				const { access, refresh } = response.data;
				// You can store the access and refresh tokens in your app's state or localStorage

				console.log("Access Token:", access);
				console.log("Refresh Token:", refresh);

				// Perform any other actions after successful login
			} catch (error) {
				console.error("Login Error:", error);
				this.errorMessage = "Login failed. Please check your credentials.";
				// Handle login error
			}
		},
	},
};
</script>

<style scoped lang="scss">
/* Add your styles here */
@import url("~bootstrap/dist/css/bootstrap.css");

@import url("https://fonts.googleapis.com/css?family=Raleway:400,700");

*,
*:before,
*:after {
	box-sizing: border-box;
}

.background {
	background: #333;
}

.container {
	position: relative; /* Change to relative */
	width: 100%;
	min-height: 100vh; /* Use min-height to ensure container covers the entire screen */
	display: flex;
	align-items: center;
	justify-content: center;
	overflow: hidden;
	background: linear-gradient(
		to bottom right,
		#ffeaa7,
		#fdcbf1
	); /* Gradient background */
	border-radius: 10px;
	box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Add a soft shadow */
	transition: background-color 0.3s, box-shadow 0.3s; /* Transition effects */

	&:hover,
	&.container.active {
		.top,
		.bottom {
			&:before,
			&:after {
				margin-left: 300px;
				transform-origin: -300px 50%;
				transition-delay: 0s;
			}
		}

		.center {
			opacity: 1;
			transition-delay: 0.2s;
		}
	}
}

.top,
.bottom {
	&:before,
	&:after {
		content: "";
		display: block;
		position: absolute;
		width: 200vmax;
		height: 200vmax;
		top: 50%;
		left: 50%;
		margin-top: -100vmax;
		transform-origin: 0 50%;
		transition: all 0.5s cubic-bezier(0.445, 0.05, 0, 1);
		z-index: 10;
		opacity: 0.65;
		transition-delay: 0.2s;
	}
}

.top {
	&:before {
		transform: rotate(45deg);
		background: #e46569;
	}
	&:after {
		transform: rotate(135deg);
		background: #ecaf81;
	}
}

.bottom {
	&:before {
		transform: rotate(-45deg);
		background: #60b8d4;
	}
	&:after {
		transform: rotate(-135deg);
		background: #3745b5;
	}
}

.center {
	position: absolute;
	width: 400px;
	height: 400px;
	top: 50%;
	left: 50%;
	margin-left: -200px;
	margin-top: -200px;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	padding: 30px;
	opacity: 0;
	transition: all 0.5s cubic-bezier(0.445, 0.05, 0, 1);
	transition-delay: 0s;
	color: #333;

	input {
		width: 100%;
		min-width: 300px;
		padding: 15px;
		margin: 5px;
		border-radius: 1px;
		border: 1px solid #ccc;
		font-family: inherit;
	}
}

.text-danger {
	text-align: center;
}
</style>
