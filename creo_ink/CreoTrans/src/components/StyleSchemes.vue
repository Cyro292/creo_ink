<template>
    <label for="">Stroke</label>
    <br>
    <button class="clrOne btn"></button>
    <button class="clrTwo btn"></button>
    <button class="clrThree btn"></button>
    <button class="clrFour btn"></button>
    <button class="clrFive btn"></button>

    <br>

    <label for="">Background</label>
    <br>
    <button class="bgOne btn"></button>
    <button class="bgTwo btn"></button>
    <button class="bgThree btn"></button>
    <button class="bgFour btn"></button>
    <button class="bgFive btn"></button>

    <br>

    <label for="">Fill</label>
    <br>
    <button class="fillTrans btn"></button>
    <button class="fillSolid btn"></button>
    <button class="fillDashed1 btn"></button>
    <button class="fillDashed2 btn"></button>

    <br>

    <label for="">Stroke Style</label>
    <br>
    <button class="strokeStyleOne btn"></button>
    <button class="strokeStyleTwo btn"></button>
    <button class="strokeStyleThree btn"></button>
    
</template>

<script>
    export default{
        name: 'ColorSchemes',
        
    }
</script>

<style scoped>
    label {
        font-weight: 600;
        margin-top: .6rem;
    }  

    .btn {
        margin: 8px 7px 0;
        height: 2rem;
        width: 2rem;
        border: solid black 2px;
    }


    /* COLOR */
    .clrOne {
        background-color: blue;
    }

    .clrTwo {
        background-color: purple;
    }

    .clrThree {
        background-color: red;
    }

    .clrFour {
        background-color: yellow;
    }

    .clrFive {
        background-color: green;
    }


    /* BACKGROUND */
    .bgOne {
        background-color: blue;
    }

    .bgTwo {
        background-color: purple;
    }

    .bgThree {
        background-color: red;
    }

    .bgFour {
        background-color: yellow;
    }   

    .bgFive {
        background-color: green;
    }


    /* FILL */
    .fillTrans {
        background-color: grey;
        background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAMUlEQVQ4T2NkYGAQYcAP3uCTZhw1gGGYhAGBZIA/nYDCgBDAm9BGDWAAJyRCgLaBCAAgXwixzAS0pgAAAABJRU5ErkJggg==);
    }

    .fillSolid {
        background: grey;
    }

    .fillDashed1 {
        background: rgb(0,0,0);
        background: linear-gradient(135deg, rgba(0,0,0,1) 0%, rgba(97,134,109,1) 55%, rgba(255,255,255,1) 100%);   
    }

    .fillDashed2 {
        background: rgb(0,0,0);
        background: linear-gradient(90deg, rgba(0,0,0,1) 0%, rgba(97,134,109,1) 55%, rgba(255,255,255,1) 100%);     
    }
</style>    