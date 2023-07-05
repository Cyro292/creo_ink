<template>
    <canvas id="canvas1"></canvas>
    <canvas @mousedown="mouseDown" @mouseup="mouseUp" @mousemove="drawManager" id="canvas2"></canvas>
</template>

<script>
import StyleSchemes from './StyleSchemes.vue';
import { updateCanvas } from '../stores/store.js'

export default {
    name: 'Canvas',
    components: {
        StyleSchemes
    },

    data() {
        return {
            //CANVAS
            windowW: null,
            windowH: null,

            canvas1: null,
            canvas2: null,

            canvasObjects: [],

            ctx1: null,
            ctx2: null,
            rc1: null,
            rc2: null,

            rect: null,
            elps: null,

            mouseIsDown: null,

            posX: null,
            posY: null,
            
            centerX: null,
            centerY: null,

            deltaX: null,
            deltaY: null,

            offLeft: 0,
            offTop: 0,

            //styling
            strokeClr: getComputedStyle(document.documentElement).getPropertyValue('--stroke-color'),
            BackGClr: getComputedStyle(document.documentElement).getPropertyValue('--background-color'),

            roughness: 0.5,
            strokeWidth: 3,
            
        }
    },
    
    mounted() {
        
        
        //temporary canvas that gets engaged by user
        this.canvas2 = document.querySelector('#canvas2');
        this.ctx2 = this.canvas2.getContext('2d');
        this.rc2 = rough.canvas(document.querySelector('#canvas2'));
        
        //permanent canvas that holds all drawings
        this.canvas1 = document.querySelector('#canvas1'); 
        this.ctx1 = canvas1.getContext('2d');
        this.rc1 = rough.canvas(document.querySelector('#canvas1'));
        
        //align canvas1 in center
        // this.canvas1.style.left = '-1920px';
        // this.canvas1.style.top = '-502px';
        
        this.refreshWindow();

// -------------------------------------

        //temporary canvas that gets engaged by user
        updateCanvas().canvas2 = document.querySelector('#canvas2');
        updateCanvas().ctx2 = updateCanvas().canvas2.getContext('2d');
        updateCanvas().rc2 = rough.canvas(document.querySelector('#canvas2'));
        
        //permanent canvas that holds all drawings
        updateCanvas().canvas1 = document.querySelector('#canvas1'); 
        updateCanvas().ctx1 = canvas1.getContext('2d');
        updateCanvas().rc1 = rough.canvas(document.querySelector('#canvas1'));
        
        //align canvas1 in center
        // this.canvas1.style.left = '-1920px';
        // this.canvas1.style.top = '-502px';
        
    },
  

    methods: {
        refreshWindow() {
            console.log('window freshed up');
            this.windowW = window.innerWidth;    //!!!  problematic since window-alignment only takes place when refreshing
            this.windowH = window.innerHeight;   //!!!!  in case you scale canvas down or up $('#canvas2') doesen't scale accordingly and drawable section on the screen decreases
            
            this.canvas2.width = this.windowW;
            this.canvas2.height = this.windowH;
            
            this.canvas1.width = this.windowW;// * 3;
            this.canvas1.height = this.windowH;// * 3;
        },

        mouseDown(e) {
            this.mouseIsDown = 1;
            this.posX = e.clientX;
            this.posY = e.clientY;
            console.log('posX: ' + this.posX + ', posY: ' + this.posY);
        },
        mouseUp () {
            
            if ($('#canvas2').hasClass('square')) {
                this.saveRect();
                
                } else if ($('#canvas2').hasClass('circle')) {
                this.saveEllipse();
                
            }

            this.ctx1.beginPath();

            this.ctx2.clearRect(0, 0, this.canvas2.width, this.canvas2.height);
            this.mouseIsDown = null;
        },
        drawManager(e) {

            if(this.mouseIsDown) {
                
                if ($('#canvas2').hasClass('grab')) {
                    this.dragCanvas(e);

                } else if ($('#canvas2').hasClass('pointerMouse')) {
                    this.selectorBox(e);
                    
                } else if($('#canvas2').hasClass('pen')) {
                    this.drawPen(e);
                
                } else if ($('#canvas2').hasClass('ereaser')) {
                    this.erease(e);
                    this.ereaserCursor(e);

                } else if ($('#canvas2').hasClass('square')) {
                    this.drawRect(e);

                } else if ($('#canvas2').hasClass('circle')) {
                    this.drawEllipse(e);

                } 
            }
        },
        dragCanvas(e) {
    
            //calculate travelled distance
            this.deltaX = e.clientX - this.posX;
            this.deltaY = e.clientY - this.posY;

            //move canvas  
            this.canvas1.style.left = ($('#canvas1').offsetLeft + this.deltaX) + "px";
            this.canvas1.style.top = ($('#canvas1').offsetTop + this.deltaY) + "px";
            console.log('offL: '+ $('#canvas1').offsetLeft);
            console.log('offT: '+ $('#canvas1').offsetTop);
            
            //update position
            this.posX = e.clientX;
            this.posY = e.clientY;

            //update offset position
            this.offLeft = $('#canvas1').offsetLeft;
            this.offTop = $('#canvas1').offsetTop;

            //limit drag-area
            if (this.offLeft > 0) {
                $('#canvas1').style.left = 0;

            } if(this.offLeft < -3840) {
                $('#canvas1').style.left = '-3840px';

            } if (this.offTop > 0) {
                $('#canvas1').style.top = 0;

            } if (this.offTop < -1004) {
                $('#canvas1').style.top = '-1004px';
            }
            

        },
        selectorBox(e) {
        
            //calculate travelled distance
            this.deltaX = e.clientX - this.posX;
            this.deltaY = e.clientY - this.posY;

            console.log(this.deltaX, this.deltaY);

            //draw rectangle
            this.ctx2.lineWidth = 2;
            this.ctx2.strokeStyle = "#ff0000";
            this.ctx2.clearRect(0, 0, this.canvas2.width, this.canvas2.height);
            this.ctx2.beginPath();
            this.ctx2.setLineDash([5, 5]);
            this.ctx2.rect(this.posX, this.posY, this.deltaX, this.deltaY); 
            this.ctx2.stroke(); 
        },
        drawPen(e) {
        
            //update color
            this.strokeClr = getComputedStyle(document.documentElement).getPropertyValue('--stroke-color');
            this.BackGClr = getComputedStyle(document.documentElement).getPropertyValue('--background-color');


            //draw Pen-line
            this.ctx1.lineWidth = this.lineWidth;
            this.ctx1.lineCap ='round';
            this.ctx1.strokeStyle = this.strokeClr;

            this.ctx1.lineTo(e.clientX-this.offLeft, e.clientY-this.offTop)
            this.ctx1.stroke();    
            this.ctx1.beginPath();
            this.ctx1.moveTo(e.clientX-this.offLeft, e.clientY-this.offTop);
        },
        ereaser(e) {

            //calculate travelled distance
            deltaX = e.clientX - posX;
            deltaY = e.clientY - posY;

            ctx2.clearRect(posX, posY, deltaX, deltaY)

            posX = e.clientX;
            posY = e.clientY;

            ctx2.clearRect(e.clientX, e.clientY, 4, 4);
            ctx2.beginPath();
            ctx2.setLineDash([]);
            ctx2.arc(e.clientX, e.clientX, 2, 0, 180);
            ctx2.stroke();
        },
        text(e) {
            
            var t = document.createTextNode("this is a test");


            // create new textarea element with its attributes

            var input = document.createElement('textarea');
            input.name = 'newText';
            input.id = 'text';
            input.cols = 80;
            input.rows = 0;
            input.style.left = posX + "px";
            input.style.top = posY + "px";

            // add the text node to the newly created div
            input.appendChild(t);
            document.body.appendChild(input);

        },  
        drawRect(e)  {
            //update color
            this.strokeClr = getComputedStyle(document.documentElement).getPropertyValue('--stroke-color');
            this.BackGClr = getComputedStyle(document.documentElement).getPropertyValue('--background-color');

            //calculate travelled distance
            this.deltaX = e.clientX - this.posX;
            this.deltaY = e.clientY - this.posY;

            //draw rectangle            
            this.ctx2.clearRect(0, 0, this.canvas2.width, this.canvas2.height);
            this.rc2.rectangle(this.posX, this.posY, this.deltaX, this.deltaY, {
                roughness: this.roughness,
                fillStyle: 'solid', //later this.fill when reading out of fillBtn works
                fill: this.BackGClr,
                stroke: this.strokeClr,
                strokeWidth: 3,
            });

            // this.rc2.draw(this.rect);
            
            
            console.log('this.ctx2.fillStyle: '+this.ctx2.fillStyle, this.BackGClr);
            console.log('this.ctx2.strokeStyle: '+this.ctx2.strokeStyle, this.strokeClr);
        },
        saveRect() {


            // ctx1.lineJoin = ctx2.lineJoin;

            // ctx1.rect(posX, posY, deltaX, deltaY);
            // ctx1.stroke();
            
            console.log('rect saved');
            this.rc1.rectangle(this.posX - this.offLeft, this.posY - this.offTop, this.deltaX, this.deltaY, {
                roughness: this.roughness,
                fillStyle: 'solid', //later this.fill when reading out of fillBtn works
                fill: this.BackGClr,
                stroke: this.strokeClr,
                strokeWidth: 3,
            });

            const newRect = {
                name: 'rect',
                x: this.posX,
                y: this.posY,
                width: this.deltaX,
                height: this.deltaY,
                roughness: this.roughness,
                fillStyle: this.fillStyle,
                fill: this.BackGClr,
                stroke: this.strokeClr,
                strokeWidth: this.strokeWidth
            };

            updateCanvas().canvasObjects.push(newRect); //add new obj to array
            console.log(updateCanvas().canvasObjects);

            // access prop in object: this.canvasObjects[this.canvasObjects.length-1].fill;
            
            this.ctx1.beginPath();   //to prevent 'linejumping' in case drawPen() is called afterwards

            this.resetVar();
            
        },
        drawEllipse(e) {

            //update color
            this.strokeClr = getComputedStyle(document.documentElement).getPropertyValue('--stroke-color');
            this.BackGClr = getComputedStyle(document.documentElement).getPropertyValue('--background-color');

            //calculate travelled distance
            this.deltaX = e.clientX - this.posX;
            this.deltaY = e.clientY - this.posY;

            //calculate center
            this.centerX = this.posX + (this.deltaX / 2);
            this.centerY = this.posY + (this.deltaY / 2);

            //calculate horizonatal(x) and vertical(y) radius -> Math.sqrt; Math.pow to only return positive values
            this.radiusX = Math.sqrt(Math.pow((this.deltaX), 2)); //if not rough divide deltaX (inside purple brackets) with two
            this.radiusY = Math.sqrt(Math.pow((this.deltaY), 2)); //if not rough divide deltaX (inside purple brackets) with two

            console.log(this.radiusX, this.radiusY);

            this.ctx2.clearRect(0, 0, this.canvas2.width, this.canvas2.height);
            this.rc2.ellipse(this.centerX, this.centerY, this.radiusX, this.radiusY, {
                roughness: this.roughness / 2,
                fillStyle: 'solid', //later this.fill when reading out of fillBtn works
                fill: this.BackGClr,
                stroke: this.strokeClr,
                strokeWidth: 3,
            });
        },
        saveEllipse() {
            console.log('circle saved');

            this.rc1.ellipse(this.centerX - this.offLeft, this.centerY - this.offTop, this.radiusX, this.radiusY, {
                roughness: this.roughness,
                fillStyle: 'solid', //later this.fill when reading out of fillBtn works
                fill: this.BackGClr,
                stroke: this.strokeClr,
                strokeWidth: 3,
            });

            const newElipse = {
                name: 'ellipse',
                x: this.centerX,
                y: this.centerY,
                radiusX: this.radiusX,
                radiusY: this.radiusY,
                roughness: this.roughness,
                fillStyle: this.fillStyle,
                fill: this.BackGClr,
                stroke: this.strokeClr,
                strokeWidth: this.strokeWidth
            };
            this.canvasObjects.push(newElipse); //add new obj to array
            //update :root

            this.ctx1.beginPath();   //to prevent 'linejumping' in case drawPen() is called afterwards

            this.resetVar();
        },
        getActiveClr(activeClr) {
            console.log('In Canvas: '+activeClr);
        },
        resetVar() {
            this.centerX = null;
            this.centerY = null;

            this.deltaX = null;
            this.deltaY = null;
            
            this.moveX = null;
            this.moveY = null;

            this.posX = null;
            this.posY = null;
            
            this.radius = null;
            this.radiusX = null;
            this.radiusY = null;
        }

    }

}

</script>

<style>
    #canvas2{
        position: absolute;
        top: 0;
        left: 0;
    }

    #canvas1{
        position: absolute;
        top: 0;
        left: 0;

        /* top: -1920px; */
        /* left: -502px; */
        
        cursor: none;
    }

    .circleCursor {
        /* visibility: visible; */
        cursor: auto;
        position: absolute;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background-color: rgba(255, 255, 255, 0.5);
        border: 1px solid black;
        transform: translate(-50%, -50%);
    }


    .crosshair {
        cursor: crosshair;
    }

    .grab {
        cursor: move;
        cursor: grab;
    }

    .grabbing {
        cursor: grabbing;
    }
</style>