<template>
    <section id="controlCenter">
        
        <section id="primarySection">
            
            <div class="top container">
            
                <DragHand />
                <SelectorBox />
                <Pen />
                <Ereaser />
                <Textfield />
                <Rectangle />
                <Circle />   
                
            </div>    
            <br><br>
            <div class="bottom container">
    
                <button class="btn btn-dark btn-sm arrowLeft"><i class="fa-solid fa-arrow-left"></i></button>
                <button class="btn btn-dark btn-sm arrowRight"><i class="fa-solid fa-arrow-right"></i></button>
                <button class="btn btn-dark btn-sm arrowDown"><i class="fa-solid fa-arrow-down"></i></button>
                <button class="btn btn-dark btn-sm copy"><i class="fa-regular fa-clone"></i></button>
                <button class="btn btn-dark btn-sm trash"><i class="fa-solid fa-trash"></i></button>
            
            </div>
        </section>
        
        <section id="secondarySection">
            
            <div class="color-schemes">
            <ColorSchemes />
            </div>
    
            <div class="opacity">
                <label for="opacity">Opacity:</label>
                <input type="range">
            </div>

        </section>
        
    </section>
</template>

<style scoped>
    #controlCenter {
        margin: 1rem 0 0 1rem; 
        position: absolute;
        background-color: rgb(197, 177, 232);
        padding: 10px;
        border-radius: 1rem;
    }

    #primarySection {
        text-align: center;
    }

    #secondarySection {
        margin-left: 1.5rem;
    }
    .container{
        background-color: rgba(42, 42, 42, 0.422);
        padding: 7px 0;
        border-radius: 1rem;
        display: inline-block;
        position: relative;
        /* z-index: 1000; */
    }

    .btn {
        margin: 0 10px;
        width: 2rem;
    }

    .selected {
        background: rgba(0, 0, 0, .5);
    }

    .color-schemes, .bgType, .opacity {
        text-align: left;
    }

    .none {
        background-color: white;
        color: black;
    }

    .solid {
        background-color: black;
        color: beige;
    }

    .checked {
        background-color: #e25dc7;
    }
    /* .opacity { 
        
    }

    input[type="range"]::-webkit-slider-runnable-track {
        background: #053a5f;
        height:0.5rem;
    }

    input[type="range"]::-webkit-slider-thumb {}*/


</style>

<script> 
import Canvas from './Canvas.vue'
import DragHand from './DragHand.vue'
import SelectorBox from './SelectorBox.vue'
import Pen from './Pen.vue'
import Ereaser from './Ereaser.vue'
import Textfield from './Textfield.vue'
import Rectangle from './Rectangle.vue'
import Circle from './Circle.vue'
import ColorSchemes from './ColorSchemes.vue'



    export default{
        name: 'ButtonCenter',
        components: {
            Canvas,
            DragHand,
            SelectorBox,
            Pen,
            Ereaser,
            Textfield,
            Rectangle,
            Circle,
            ColorSchemes,
        },
        methods: {
            
            defineVars() {
                
                //defining lowerControl buttons
                const arrowLeft = $(".arrow-left");
                const arrowRight = $(".arrow-right");
                const arrowDown = $(".arrow-down");
                const copy = $(".copy");
                const trash = $('.trash');
        
                const cursor = $('.circleCursor');    
                
                // create reference to coordinate-saving-place
                
        
                //define vars outside of function so it is always accessible
                var centerX = null;
                var centerY = null;
        
                var colorStroke = '';
                var colorBg = '';
        
                var deltaX = null;
                var deltaY = null;
        
                var moveX = null;
                var moveY = null;
        
                var offLeft = null;
                var offTop = null;
        
                var posX = null;
                var posY = null;
        
                var radius = null;
                var radiusX = null;
                var radiusY = null;
        
        
                //update offset position
                offLeft = canvas1.offsetLeft;
                offTop = canvas1.offsetTop;
        
                
            },
            canvasListener() {
                //Add Event-Listeners to canvas mouseevents
                $('#canvas2').on('mousedown', mouseDown); 
        
                $('#canvas2').on('mouseup', mouseUp);    
        
                $('#canvas2').on('mousemove', mouseMove);
        
                $('#canvas2').on('click', mouseClick);
            },
            mouseDown(e) {
        
                // define coordinates of execution
                posX = e.clientX;
                posY = e.clientY;

                $('#canvas2').addClass('mouseDown'); //tell other functions that mouse is down -> mouseMove functions whith condition of mouseDown can now be executed

                if ($('#canvas2').hasClass('grab')){   //activate grabbing cursor #dragHand
                    $('#canvas2').removeClass('grab');
                    $('#canvas2').addClass('grabbing');

                } 
                    
            },
            mouseUp(e) {

                $('#canvas2').removeClass('mouseDown');   // tell other functions that mouse is NOT down anymore

                if (!$('#canvas2').hasClass('$(".pointerMouse")')){ //so selector-box doesn't dissapear when releasing mouse
                    ctx2.clearRect(0, 0, canvas2.width, canvas2.height);    //avoids overlaying effect since drawing is displayed on canvas1 and $('#canvas2') until $('#canvas2') is #mouseDown && #mouseMove
                }

                if ($('#canvas2').hasClass('grabbing')) {  //re-activate grab cursor #dragHand
                    $('#canvas2').removeClass('grabbing');
                    $('#canvas2').addClass('grab');

                } else if ($('#canvas2').hasClass('pen')) {   //end line to prevent 'linejumping'
                    ctx1.beginPath();

                } else if ($('#canvas2').hasClass('$(".square")')) {    //transfer rectangle to permanent canvas
                    console.log('triggered');
                    saveRect();
                    resetVar();
                    
                } else if($('#canvas2').hasClass('circle')) {     //transfer ellipse to permanent canvas
                    console.log('triggered');
                    saveEllipse();
                    resetVar();
                } 

            },
            mouseMove(e) {

                if ($('#canvas2').hasClass('grabbing')) {
                    dragCanvas(e);
                } else if ($('#canvas2').hasClass('pointerMouse')) {
                    selectorBox(e);
                    
                } else if($('#canvas2').hasClass('pen')) {
                    drawPen(e);
                
                } else if ($('#canvas2').hasClass('ereaser')) {
                    erease(e);
                    ereaserCursor(e);

                } else if ($('#canvas2').hasClass('square')) {
                    drawRect(e);

                } else if ($('#canvas2').hasClass('circle')) {
                    drawEllipse(e);

                } 

            },
            mouseClick(e) {
                console.log('click at: '+ e.clientX + 'X, ' + e.clientY + 'Y.');

                if ($('#canvas2').hasClass('text')) {
                    drawText(e);
                }
            },
            resetVar() {
                centerX = null;
                centerY = null;

                deltaX = null;
                deltaY = null;
                
                moveX = null;
                moveY = null;

                posX = null;
                posY = null;
                
                radius = null;
                radiusX = null;
                radiusY = null;
            }

        }

    }
</script>