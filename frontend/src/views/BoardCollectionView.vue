<script>
// @ is an alias to /src
import BoardIcon from "@/components/BoardIcon.vue";
import Notebook from "@/components/Notebook.vue";

export default {
	name: "BoardCollection",
	components: {
        BoardIcon,
        Notebook,
    },
    data () {
        return {
            boards: [
            {"id":1, "permission":"Owner", "name": "Jugend Forscht", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":2, "permission":"Owner", "name": "Jugend Forscht", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":3, "permission":"Owner", "name": "Jugend Forscht", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":4, "permission":"Owner", "name": "Jugend Forscht", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":5, "permission":"Owner", "name": "Jugend Forscht", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":6, "permission":"Owner", "name": "Jugend Forscht", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":7, "permission":"Owner", "name": "Jugend Forscht", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":8, "permission":"Owner", "name": "Jugend Forscht", "amountofusers":1, "changedate":"1.1.2023"},
            {"id":9, "permission":"Owner", "name": "Jugend Forscht", "amountofusers":1, "changedate":"1.1.2023"},
            ],
            visibleNotebook : false,
            BookLeft : 0,
            BookTop : 0,
            index: 0,
            username : "Sketcher77",
            three: [
                {},
                {},
                {},
            ],


    }
        

    },
    methods: {
        showNotebook(event){
            this.visibleNotebook = true;
            this.bookLeft = event.clientX + 'px';
            this.bookTop = event.clientY + 'px';
        },
        hideNotebook(){
            this.visibleNotebook = false;
        },
        showNotebookstatus(event){
            this.visibleNotebook = true;
            this.bookLeft = event.clientX + 'px';
            this.bookTop = event.clientY + 'px';
        },
        showNotebookpermission(event){
            this.visibleNotebook = true;
            this.bookLeft = event.clientX + 'px';
            this.bookTop = event.clientY + 'px';
        },
        showNotebookusers(event){
            this.visibleNotebook = true;
            this.bookLeft = event.clientX + 'px';
            this.bookTop = event.clientY + 'px';
        },
        publish(){
            published != published
        },
        setIndex(id){
            this.index = id
        }
    }
};
</script>

<template>

    <h1>Hello {{ username }}</h1>
    <div class="container">
    <button @click="showNotebook" class="erstellen">Create new whiteboard</button>
    <BoardIcon 
        v-for="board in boards" 
        :name = board.name
        :permission = board.permission
        :amountofusers = board.amountofusers
        :changedate = board.changedate
        :showNotebook = "showNotebook"
        :index = board.id
        :setIndex = "setIndex"
    />
    

    </div>
    <div :style="{ display: visibleNotebook ? 'block' : 'none', left: bookLeft, top: bookTop }" class="book">
        <Notebook
            :hideNotebook = "hideNotebook"
            status = 1
            permission = 'Owner'

        />
    </div>
    
</template>

<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Gluten&family=Montserrat&display=swap");
    .erstellen {
        font-family: 'Gluten', cursive;
        color: var(--text-accent);
        font-size: 1.4em;
        text-align: center;
        border-radius: .8em;
        cursor: pointer;
        display: block;
        width: 15rem;
        height: 14rem;
        border-color: var(--text-accent);
        border-width: .3em;
        border-style: dashed;
        background-color: transparent;
        margin-right: 4.2em;
    }

    .transparent{
    width: 15rem;
    height: 14rem;
    background-color: transparent;
    margin-right: 4.2em;
    margin-left: 4.4em;
    border-color: transparent;
    border-width: .3em;
    border-style: dashed;
    }
    .book{
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
        justify-content:space-evenly;
        flex-wrap: wrap;
    }
</style>