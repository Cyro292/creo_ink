<script>
	// @ is an alias to /src
    import Notesheet from "@/components/Notesheet.vue";
    import StickyNote from "@/components/StickyNote.vue";

	export default {
		name: "Login",
		components: {
            Notesheet,
            StickyNote,
		},
	};
</script>

<template>
    <Notesheet/>
    <div class="middle">
        <StickyNote
        text = "Hello"
        color = aqua
        color2 = blue
        /></div>
    
</template>

<style>
.middle{
    margin-left: 70em;
}
</style>