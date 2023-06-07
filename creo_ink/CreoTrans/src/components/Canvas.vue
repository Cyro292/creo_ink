<template>
    <canvas id="canvas1"></canvas>
    <canvas id="canvas2"></canvas>
</template>

<script>

export default {
    name: 'Canvas',

    mounted() {  
        this.baseCanvas();
        console.log('Canvas logging');      
    },

    methods: {
        baseCanvas() {
            var windowW = window.innerWidth;    //!!!  problematic since window-alignment only takes place when refreshing
            var windowH = window.innerHeight;   //!!!!  in case you scale canvas down or up $('#canvas2') doesen't scale accordingly and drawable section on the screen decreases

            //temporary canvas that gets engaged by user
            const canvas2 = document.querySelector('#canvas2');
            const ctx2 = canvas2.getContext('2d');
            const rc2 = rough.canvas(document.querySelector('#canvas2'));
            
            canvas2.width = windowW;
            canvas2.height = windowH;
            
            //permanent canvas that holds all drawings
            const canvas1 = document.querySelector('#canvas1'); 
            const ctx1 = canvas1.getContext('2d');
            const rc1 = rough.canvas(document.querySelector('#canvas1'));
            
            canvas1.width = windowW * 3;
            canvas1.height = windowH * 3;
            
            //align canvas1 in center
            canvas1.style.left = '-1920px';
            canvas1.style.top = '-502px';
        },
        dragCanvas(e) {
    
            //calculate travelled distance
            deltaX = e.clientX - posX;
            deltaY = e.clientY - posY;

            //move canvas  
            canvas1.style.left = (canvas1.offsetLeft + deltaX) + "px";
            canvas1.style.top = (canvas1.offsetTop + deltaY) + "px";
            console.log('offL: '+canvas1.offsetLeft);
            console.log('offT: '+canvas1.offsetTop);
            
            //update position
            posX = e.clientX;
            posY = e.clientY;

            //update offset position
            offLeft = canvas1.offsetLeft;
            offTop = canvas1.offsetTop;

            //limit drag-area
            if (offLeft > 0) {
                canvas1.style.left = 0;

            } if(offLeft < -3840) {
                canvas1.style.left = '-3840px';

            } if (offTop > 0) {
                canvas1.style.top = 0;

            } if (offTop < -1004) {
                canvas1.style.top = '-1004px';
            }
            

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
        top: -1920px;
        left: -502px;
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

    #canvas1 {
        cursor: none;
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