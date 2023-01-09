<script>
	// @ is an alias to /src
    import Notepad from "@/components/Notepad.vue";

	export default {
		name: "NewPasswordn",
		components: {
            Notepad,
		},
	};
</script>


<template>

	<body>

        <h1><span>Create new</span> password</h1>

        <Notepad
        note = "Use 8 or more characters with a mix of letters, numbers & symbols."
        confirmpassword = 1
        newpassword = 1
		blue = "Log in"
        />
    </body>

</template>