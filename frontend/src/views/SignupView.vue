<template>
	<NavBar />
	<OpenUpWrapper>
		<h2 class="text-center">Create an Account</h2>
		<form @submit.prevent="signup">
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
				<input
					v-model="confirmPassword"
					type="password"
					class="form-control"
					id="confirmPassword"
					required
					placeholder="confirm password"
				/>
			</div>
			<router-link to="/login"
				>Already have an account? Log in here!</router-link
			>
			<div class="text-danger" v-if="errorMessage">{{ errorMessage }}</div>
			<button type="submit" class="btn btn-primary">Sign Up</button>
		</form>
		<h2>&nbsp;</h2>
	</OpenUpWrapper>
</template>

<script>
import axios from "axios";
import OpenUpWrapper from "../components/OpenUpWrapper.vue";
import NavBar from "@/components/NavBar.vue";

export default {
	data() {
		return {
			email: "",
			password: "",
			errorMessage: "",
			animationActive: false,
		};
	},
	components: {
		OpenUpWrapper,
		NavBar,
	},

	methods: {
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

.background {
	background: #333;
}

input {
	width: 100%;
	min-width: 300px;
	padding: 15px;
	margin: 5px;
	border-radius: 1px;
	border: 1px solid #ccc;
	font-family: inherit;
}

.text-danger {
	text-align: center;
}
</style>
