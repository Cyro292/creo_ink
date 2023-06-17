<template>  
    <label for="">Stroke</label>
    <br>
    <button @click="strokeClrManager" class="strokeOne btn strokeClr"></button>
    <button @click="strokeClrManager" class="strokeTwo btn strokeClr"></button>
    <button @click="strokeClrManager" class="strokeThree btn strokeClr"></button>
    <button @click="strokeClrManager" class="strokeFour btn strokeClr"></button>
    <button @click="strokeClrManager" class="strokeFive btn strokeClr"></button>

    <br>

    <label for="">Background</label>
    <br>
    <button @click="bgManager" class="bgOne btn bg"></button>
    <button @click="bgManager" class="bgTwo btn bg"></button>
    <button @click="bgManager" class="bgThree btn bg"></button>
    <button @click="bgManager" class="bgFour btn bg"></button>
    <button @click="bgManager" class="bgFive btn bg"></button>

    <br>

    <label for="">Fill</label>
    <br>
    <button @click="fillManager" class="fillTrans btn fill"></button>
    <button @click="fillManager" class="fillSolid btn fill"></button>
    <button @click="fillManager" class="fillDashed1 btn fill"></button>
    <button @click="fillManager" class="fillDashed2 btn fill"></button>

    <br>

    <label for="">Stroke Style</label>
    <br>
    <button @click="strokeStyleManager" class="strokeStyleOne btn strokeStyle"></button>
    <button @click="strokeStyleManager" class="strokeStyleTwo btn strokeStyle"></button>
    <button @click="strokeStyleManager" class="strokeStyleThree btn strokeStyle"></button>
    
</template>

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
    .strokeOne {
        background-color: rgb(0, 0, 255, 0.8);
    }

    .strokeTwo {
        background-color: purple;
    }

    .strokeThree {
        background-color: red;
    }

    .strokeFour {
        background-color: yellow;
    }

    .strokeFive {
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

    
    .selected {
        border-color: rgb(255, 255, 255);
    }

    /* InPUT FIELD FOR HEX-CODE */
    .hexCode {
        width: 300px;
        margin: 50px auto;
        border: 4px solid #00bfb6;
        border-radius: 1rem;
        padding: 20px;
        text-align: center;
        font-weight: 900;
        color: #00bfb6;
        font-family: arial;
        position: relative;
    }

    .cd:before {
        content: "";
        width: 0px;
        height: 0px;
        position: absolute;
        border-left: 10px solid transparent;
        border-right: 10px solid transparent;
        border-top: 10px solid transparent;
        border-bottom: 10px solid #00bfb6;
        right: 50%;
        top: -23px;
    }
</style>    

<script>
    export default{
        name: 'ColorSchemes',
        data() {
            return {
                activeStrokeClr: null,
                activeBg: null,
                activeFill: null,
                activeStrokeStyle: null,

                elements: null,
                element: null
            }
        },
        methods: {
            strokeClrManager(e) {
                this.activeStrokeClr = e.target.classList[0];
                
                //change :root var
                var stroke = getComputedStyle(document.documentElement).getPropertyValue('--stroke-color');
                
                document.documentElement.style.setProperty('--stroke-color', $('.'+this.activeStrokeClr).css('background-color'));
                console.log('yeas '+stroke);
                
                console.log('activeStroke: '+this.activeStrokeClr);
                
                console.log($('.strokeFour').css('background-color'), $('.'+this.activeStrokeClr).css('background-color'));
                
                
                //manage classes for animation
                this.elements = document.querySelectorAll('.strokeClr');                

                for (let i = 0; i < this.elements.length; i++) {
                    this.element = this.elements[i];
                    this.element.classList.remove('selected');
                }

                $('.'+this.activeStrokeClr).addClass('selected');
            },
            bgManager(e) {
                this.activeBg = e.target.classList[0];
                
                //change :root var                
                document.documentElement.style.setProperty('--background-color', $('.'+this.activeBg).css('background-color'));
                
                console.log('activeBg: '+this.activeStrokeClr);
                
                console.log('activeBg :root: '+ $('.'+this.activeBg).css('background-color'));
                

                //manage classes for animation
                this.elements = document.querySelectorAll('.bg');                
                
                for (let i = 0; i < this.elements.length; i++) {
                    this.element = this.elements[i];
                    this.element.classList.remove('selected');
                }
                
                $('.'+this.activeBg).addClass('selected');
                
                console.log('activeBg: '+this.activeBg);
                
            },
            fillManager(e) {
                this.elements = document.querySelectorAll('.fill');                
                
                for (let i = 0; i < this.elements.length; i++) {
                    this.element = this.elements[i];
                    this.element.classList.remove('selected');
                }

                this.activeFill = e.target.classList[0];
                $('.'+this.activeFill).addClass('selected');
                
                console.log('activeFill: '+this.activeFill);
            },
            strokeStyleManager(e) {
                this.elements = document.querySelectorAll('.strokeStyle');                
                
                for (let i = 0; i < this.elements.length; i++) {
                    this.element = this.elements[i];
                    this.element.classList.remove('selected');
                }

                this.activeStrokeStyle = e.target.classList[0];
                $('.'+this.activeStrokeStyle).addClass('selected');
                
                console.log('activeStrokeStyle: '+this.activeStrokeStyle);
            }
        }        
    }
</script>

