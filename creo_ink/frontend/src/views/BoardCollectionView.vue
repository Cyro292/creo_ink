<script>
// @ is an alias to /src
import BoardIcon from "@/components/BoardIcon.vue";
import Notesheet from "@/components/Notesheet.vue";

export default {
	name: "BoardCollection",
	components: {
        BoardNew,

    },
    data () {
        return {
            boards: [
            {"id":1, "permission":"Owner", "name": "Creo", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":1, "permission":"Owner", "name": "Creo", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":1, "permission":"Owner", "name": "Creo", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":1, "permission":"Owner", "name": "Creo", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":1, "permission":"Owner", "name": "Creo", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":1, "permission":"Owner", "name": "Creo", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":1, "permission":"Owner", "name": "Creo", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":1, "permission":"Owner", "name": "Creo", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":1, "permission":"Owner", "name": "Creo", "amountofusers":1, "changedate":"1.1.2023"},
            ],
            visibleNotesheet : false,
            BookLeft : 0,
            BookTop : 0,
            index: 0,
            username : "Sketcher77",


    }
    },
    methods: {
        showNotesheet(){
            this.visibleNotesheet = true;
        },
        hideNotesheet(){
            this.visibleNotesheet = false;
        },
    }
};
</script>

<template>

    <h1>Hello {{ username }}</h1>
    <div class="settings" v-if="visibleNotesheet" >
        <Notesheet
        :hideNotesheet = "hideNotesheet"
        />
    </div> 
    <div class="container"  :class="{ 'container-with-notesheet': visibleNotesheet }">
    <button @click="showNotesheet" class="erstellen"><div class="erstellentext" >Create new whiteboard</div></button>
    <Board
        v-for="board in boards" 
        :name = board.name
        :permission = board.permission
        :amountofusers = board.amountofusers
        :changedate = board.changedate
        :showNotebook = "showNotebook"
        :index = board.id
        :setIndex = "setIndex"
        :showNotesheet = "showNotesheet"
        :users = board.amountofusers 
    />
    

    </div>
   
    
</template>

<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Gluten&family=Montserrat&display=swap");
   
    .settings{
        position: fixed;
        right: 25rem;
        top: 14rem;
        transform: scale(120%);
    }

.erstellen {
        font-family: 'Gluten', cursive;
        color: var(--text-accent);
        font-size: 1.5rem;
        text-align: center;
        border-radius: .8em;
        cursor: pointer;
        display: block;
        width: 14rem;
        height: 13rem;
        border-color: var(--text-accent);
        border-width: .3em;
        border-style: dashed;
        background-color: transparent;
        margin-right: 5.2em;
    }

    .erstellentext{
        font-size: 1.4rem;
    }
    .erstellentext:hover{
        font-size: 1.6rem;
    }
    .blatt{
        position: absolute;
    }

    h1{
        color: black;
        font-family: 'Gluten', cursive;
        font-size: 3.4rem;
        text-align: left;
        margin: 3rem;
    }

    .container{
        display: flex;
        justify-content:flex-start;
        flex-wrap: wrap;
        text-align: left;
        margin-right: -10rem;
    }

     .container-with-notesheet {
    margin-right: 10rem;
  }
</style>