<script>
	// @ is an alias to /src
    import Notepad from "@/components/Notepad.vue";

	export default {
		name: "SignUp",
		components: {
            Notepad,
		},
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
        username = 1
        email = 1
        password = 1
		violet = "Sign up"
        />
    </body>

</template>