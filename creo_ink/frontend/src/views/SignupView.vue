<script>
	// @ is an alias to /src
    import Notepad from "@/components/Notepad.vue";
import axios from "axios";

	export default {
		name: "SignUp",

        data() {
            return {
                email: '',
                username: '',
                newpassword: '',
                confirmpassword: '',
            }
        },
		components: {
            Notepad,
		},
        methods: {
            submit(data) {
                axios.post('/rest-auth/registration/', data)
                    .then(response => {
                        // handle successful registration
                        console.log(response)
                    })
                    .catch(error => {
                        // handle registration error
                        console.log(error)
                    })
                }
            }
	};
</script>


<template>

	<body>

        <h1>Welcome!</h1>

        <Notepad
        guest = "Don't have an account yet?"
        sign = 1
        prename = 1
        surname = 1
        v-bind:username = "username"
        v-bind:email = "email"
        v-bind:newpassword = "newpassword"
        v-bind:confirmpassword = "newpassword"
		violet = "Sign up"
        />
    </body>

</template>