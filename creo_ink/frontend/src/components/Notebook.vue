<script>
	export default {
		name: "Notebook",
		props: [
            'hideNotebook',
            'status',
            'permission',
        ],
        methods:{
            permissionTest(){
                if(this.permission = "Owner"){
                    return true
               
                }else{
                    return false
                }
            }
        }
	};
</script>

<template>
    <div class="cover">
        <div class="paper">
            <button class="x" @click="hideNotebook" >x</button>
            <div class="left">
                <div v-if="status">
                    <button v-if="permissionTest">publish</button>
                </div>
            </div>
            <div class="right">

            </div>
        </div>
    </div>

</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Gluten&family=Montserrat&display=swap");

.x{
    font-size: .8em;
    font-weight: bolder;
    border-radius: 3em;
    background-color: crimson;
    color: white;
    border-color: transparent;
    border-width: .3em;
    border-style: dashed;
    margin-left: 20.6rem;
    margin-top: -1rem;
}

.cover{
    background-color: darkblue;
    border-radius: .5em;
    height: 15rem;
    width: 22rem;
    padding: .15rem;
    margin-left: 30rem;
}

.paper{
    font-family: 'Gluten', cursive;
    background-color: rgb(255, 255, 255);
    border-radius: 0em;
    height: 14.5rem;
    width: 21.5rem;
    margin-top: .25rem;
    margin-left: .25rem;
    background-image: linear-gradient(to right, white 50%, rgb(231, 231, 231) 1%, white,white);
}

.right{
    margin-left: 10rem;
}

.left{
    margin-right: 10rem;
}
</style>