<script>
	// @ is an alias to /src
    import Notepad from "@/components/Notepad.vue";

	export default {
		name: "BoardJoinen",
		components: {
            Notepad,
		},
	};
</script>


<template>

	<body>

        <h1><span>Join a new</span> whiteboard!</h1>

        <Notepad
        boardname = 1
        pin = 1
        green = 1
        
        />
    </body>

</template>