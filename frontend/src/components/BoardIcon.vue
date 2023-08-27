<script>
	export default {
		name: "BoardIcon",
		props: [
            'permission',
            'amountofusers',
            'name',
            'changedate',
            'showNotebook',
            'showNotebookstatus',
            'index',
            'setIndex',
        ]
	};
</script>

<template>
    <button class="vorschau"></button>
    <button v-if="published" class="green" >published</button>
    <button v-if="!published" @click="showNotebook" class="red">private</button>
    <button class="aqua">{{ permission }}</button>
    <button class="violet" >Users: {{ amountofusers }}</button>
    <h3>{{name}}</h3>
    <h4>recent change: {{ changedate }}</h4>
</template>

<style>

h3{
    font-family: "Gluten", cursive;
    font-size: 2.0rem;
    color: var(--text-clr);
    width: 20rem;
    text-align: left;
    margin-top: 7.4em;
    margin-left: -9.7em;
}

h4{
    font-family: "Gluten", cursive;
    font-size: .9rem;
    color: var(--text-accent);
    width: 19rem;
    text-align: left;
    margin-top: 19em;
    margin-left: -21em;
}

.vorschau {
	border-radius: .8em;
	cursor: pointer;
	display: block;
    width: 15rem;
    height: 14rem;
    border-color: rgb(96, 96, 96);
    border-width: .1em;
    border-style: solid;
    background-color: white;
}

.green{
    font-family: "Gluten", cursive;
	font-size: 1.5em;
    text-align: right;
    width: 9rem;
    height: 4rem;
    cursor: pointer;
    display: block;
    border-color: rgb(0, 0, 0);
    border-width: 0;
    border-style: none;
    background-color: transparent;
    background-image: url('../assets/kleber-grün.png');
    background-size: contain;	
    transform: rotate(12deg);
    margin-top: 5em;
    margin-left: -3.5em;
}

.green:hover{
    background-image: url('../assets/kleber-hover-grün.png');
}

.red{
    font-family: "Gluten", cursive;
	font-size: 1.5em;
    text-align: center;
    width: 9rem;
    height: 4rem;
    cursor: pointer;
    display: block;
    border-color: rgb(0, 0, 0);
    border-width: 0;
    border-style: none;
    background-color: transparent;
    background-image: url('../assets/kleber-rot.png');
    background-size: contain;	
    transform: rotate(16deg);
    margin-top: 5em;
    margin-left: -3.5em;
}

.red:hover{
    background-image: url('../assets/kleber-hover-rot.png');
}

.violet{
    font-family: "Gluten", cursive;
	font-size: 1.5em;
    text-align: right;
    width: 9rem;
    height: 4rem;
    cursor: pointer;
    display: block;
    border-color: rgb(0, 0, 0);
    border-width: 0;
    border-style: none;
    background-color: transparent;
    background-image: url('../assets/kleber-lila.png');
    background-size: contain;	
    transform: rotate(-12deg);
    margin-top: 0em;
    margin-left: -7.3em;
}

.violet:hover{
    background-image: url('../assets/kleber-hover-lila.png');
}

.aqua{
    font-family: "Gluten", cursive;
	font-size: 1.5em;
    text-align: right;
    width: 9rem;
    height: 4rem;
    cursor: pointer;
    display: block;
    border-color: rgb(0, 0, 0);
    border-width: 0;
    border-style: none;
    background-color: transparent;
    background-image: url('../assets/kleber-türkis.png');
    background-size: contain;	
    transform: rotate(-2deg);
    margin-top: 2.3em;
    margin-left: -5.4em;
}

.aqua:hover{
    background-image: url('../assets/kleber-hover-türkis.png');
}

</style>