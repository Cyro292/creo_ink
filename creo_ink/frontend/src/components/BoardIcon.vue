<script>

import StickyNote from "@/components/StickyNote.vue";

	export default {
		name: "BoardIcon",
		props: [
            'permission',
            'amountofusers',
            'name',
            'changedate',
            'index',
            'setIndex',
            'showNotesheet',
            'users'
        ],
        components:{
            StickyNote,
        },
        methods: {

        }
	};
</script>

<template>
    <div>
    <div class="vorschau"></div>
    <div class="above" @click="showNotesheet">
        <StickyNote
        text = "Users: "
        color = aqua
        color2 = "accent"
        />
    </div>
    <div class="middel" @click="showNotesheet">
        <StickyNote
        text = "Hello"
        color = aqua
        color2 = blue
        />
    </div>
    <div class="below" @click="showNotesheet">
        <StickyNote
        text = "Hello"
        color = aqua
        color2 = blue
        />
    </div>
    <h3>{{name}}</h3>
    <h4>recent change: {{ changedate }}</h4>
    </div>
</template>

<style>

.above{
    margin-top: -14rem;
    margin-left: 12rem;
    transform: rotate(-12deg) scale(83%);
    margin-right: -3rem;
}

.middel{
    margin-top: -3rem;
    margin-left: 12rem;
    transform: rotate(-3deg) scale(83%);
    margin-right: -3rem;
}

.below{
    margin-top: -3rem;
    margin-left: 12rem;
    transform: rotate(7deg) scale(83%);
    margin-right: -3rem;
}

h3{
    font-family: "Gluten", cursive;
    font-size: 2.0rem;
    color: var(--text-clr);
    width: 20rem;
    text-align: left;
    margin-top: -.5em;
    margin-left: 0em;
}

h4{
    font-family: "Gluten", cursive;
    font-size: .9rem;
    color: var(--text-accent);
    width: 19rem;
    text-align: left;
    margin-top: -1.7em;
    margin-left: 0em;
    margin-bottom: 3rem;
}

.vorschau {
	border-radius: .8em;
	cursor: pointer;
	display: block;
    width: 14rem;
    height: 13rem;
    border-color: rgb(96, 96, 96);
    border-width: .1em;
    border-style: solid;
    background-color: white;
    margin-left: -0rem;
}
</style>