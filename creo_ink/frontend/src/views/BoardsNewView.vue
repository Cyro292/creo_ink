<script>
// @ is an alias to /src
import Board from "@/components/BoardNew.vue";


export default {
	name: "BoardsNew",
	components: {
        Board,

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
<div class="container">
    <div class="lcover"></div>
    <div class="rcover"></div>
    <div class="bcover"></div>
    <div class="ocover"></div>
    <div class="lpage2"></div>
    <div class="rpage2"></div>
    <div class="bpage2"></div>
    <div class="lpage1"></div>
    <div class="rpage1"></div>
    <div class="bpage1"></div>
    <div class="frontpage"></div>
    <div class="boards">
            <Board
            v-for="board in boards" 
            :name = board.name
            :changedate = board.changedate
            />
    </div>
</div>
  </template>
  
  <style scoped>


  .rcover{
    height: 70%;
    width: 32%;
    background-color: #6b4d00;
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 200px;
    display: flex;
    position: fixed;
    top:auto;
    bottom: 3%;
    left:18%;
    transform: skew(0, 3deg);
  }
  .lcover{
    height: 70%;
    width: 32%;
    background-color: #6b4d00;
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 200px;
    margin-left: 400px;
    display: flex;
    position: fixed;
    top:auto;
    left: 22%;
   bottom: 3%;
    transform: skew(0, -3deg);
  }
  .ocover{
    width: 160px;
    height: 80px;
    border-radius: 50%;
    background-color: #6b4d00;
    position: fixed;
    bottom: 0.5%;
    left: 44.15%;
  }

  .bcover{
    height: 20%;
    width: 63.25%;
    background-color: #6b4d00;
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 200px;
    margin-left: 400px;
    display: flex;
    position: fixed;
    top:auto;
    left: -9.25%;
    bottom: 2%;
  }

  .lpage1{
    height: 67%;
    width: 30%;
    background-color: #eeeeee;
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 200px;
    display: flex;
    position: fixed;
    top:auto;
    bottom: 5%;
    left:19%;
    transform: skew(0, 1deg);
  }
  .rpage1{
    height: 67%;
    width: 30%;
    background-color: #eeeeee;
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 200px;
    margin-left: 400px;
    display: flex;
    position: fixed;
    top:auto;
    left: 23%;
    bottom: 5%;
    transform: skew(0, -1deg);
  }

  .bpage1{
    height: 20%;
    width: 61.2%;
    background: linear-gradient(to right, 
        #eeeeee 20%,
        #cccccc 35%,
        #b9b9b9 49.5%, 
        #777777 50%,
        #b9b9b9 50.5%,
        #cccccc 65%,
        #eeeeee 80%);
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 200px;
    margin-left: 400px;
    display: flex;
    position: fixed;
    top:auto;
    left: -8.2%;
    bottom: 3.3%;
  }

  .lpage2{
    height: 67%;
    width: 31%;
    background-color: #dddddd;
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 200px;
    display: flex;
    position: fixed;
    top:auto;
    bottom: 5.5%;
    left:18.5%;
    transform: skew(0, 2deg);
  }
  .rpage2{
    height: 67%;
    width: 31%;
    background-color: #dddddd;
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 200px;
    margin-left: 400px;
    display: flex;
    position: fixed;
    top:auto;
    left: 22.5%;
    bottom: 5.5%;
    transform: skew(0, -2deg);
  }

  .bpage2{
    height: 20%;
    width: 62.2%;
    background: linear-gradient(to right, 
        #dddddd 20%,
        #bbbbbb 35%,
        #aaaaaa 49.5%, 
        #777777 50%,
        #aaaaaa 50.5%,
        #bbbbbb 65%,
        #dddddd 80%);
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 200px;
    margin-left: 400px;
    display: flex;
    position: fixed;
    top:auto;
    left: -8.7%;
    bottom: 3%;
  }
  .frontpage{
    height: 68%;
    width: 60%;
    background: linear-gradient(to right, 
        #ffffff 20%,
        #eeeeee 35%,
        #b9b9b9 49.5%, 
        #777777 50%,
        #b9b9b9 50.5%,
        #eeeeee 65%,
        #ffffff 80%);
    justify-content: space-between;
    align-items: flex-end;
    margin-top: 200px;
    margin-left: 400px;
    display: flex;
    position:fixed;
    top:auto;
    left: -7.6%;
    bottom: 3.6%;
  }

  .boards{
    display: flex;
    justify-content:flex-start;
    flex-wrap: wrap;
    text-align: left;
    position: fixed;
    margin: 0 auto;
    width: 60%;
    height: 68%;
    left: 20%;
    overflow-y: auto;
    bottom: 3.6%;
    display: flex;
    flex-wrap: wrap;
  justify-content: flex-start;
  align-items: flex-start;
  }


  </style>
  