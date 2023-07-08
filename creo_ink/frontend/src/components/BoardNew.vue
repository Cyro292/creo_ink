<script>


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
            
        },
        methods: {

        }
	};
</script>

<template>
    <div class="container">
    <div class="vorschau"></div>
   
    <h3>{{name}}</h3>
    <h4>changed: {{ changedate }}</h4>
    </div>

</template>

<style>

container{
   margin: 5rem;
}
h3{
    font-family: "Gluten", cursive;
    font-size: 2.0rem;
    color: var(--text-clr);
    width: 13rem;
    text-align: center;
    margin-top: .2em;
    margin-left: 0em;
}

h4{
    font-family: "Gluten", cursive;
    font-size: .9rem;
    color: var(--text-accent);
    width: 11rem;
    text-align: center;
    margin-top: -2em;
    margin-left: 2em;
    margin-bottom: 3rem;
}

.vorschau {
	border-radius: .8em;
	cursor: pointer;
	display: block;
    width: 8rem;
    height: 7rem;
    border-color: rgb(96, 96, 96);
    border-width: .1em;
    border-style: solid;
    background-color: rgb(255, 255, 255);
    margin-left: 3.4rem;
    box-shadow: 0px 5px 2px 2px rgba(0, 0, 0, 0.2);
}
</style>