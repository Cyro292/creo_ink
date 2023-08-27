<script>
	// @ is an alias to /src
    import Notepad from "@/components/Notepad.vue";

	export default {
		name: "Login",
		components: {
            Notepad,
		},
	};
</script>


<template>

	<body>

        <h1><span>Go</span> sketching!</h1>

        <Notepad
        guest = "Don't have an account yet?"
        log = 1
        click = 1
		violet = "Log in"
        email = 1
        password = 1
        />
    </body>

</template>