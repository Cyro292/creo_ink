<template>
    <button @click="setUpPen" class="btn btn-sm pen"><i class="fa-solid fa-pen"></i></button>
</template>

<script>
    export default {
        name: 'pen',
        mounted() {
            
        },
        methods: {
            setUpPen() {
            
                //manage active button animation
                $(".dragHand").removeClass("selected");
                $(".pointerMouse").removeClass("selected");
                $(".pen").addClass("selected");
                $(".ereaser").removeClass("selected");
                $(".text").removeClass("selected");
                $(".square").removeClass("selected");
                $(".circle").removeClass("selected");
        
                //manage cursor animation
                $('#canvas2').addClass("crosshair"); //cursor wird zum crosshair wenn auf canvas ist
                $('#canvas2').removeClass("grab");   // "
                $('#canvas2').removeClass("circleCursor");      
                $('#canvas2').addClass("pen");
        
        
                // remove other class-names
                $('#canvas2').removeClass("dragHand");
                $('#canvas2').removeClass("pointerMouse");
                $('#canvas2').removeClass("ereaser");
                $('#canvas2').removeClass("text");
                $('#canvas2').removeClass("square");
                $('#canvas2').removeClass("circle");
        
                console.log($('#canvas2').attr("class")); // jff
        
                   
            },
            drawPen(e) {

                if ($('#canvas2').hasClass('mouseDown')) {

                    //update color
                    colorStroke = $('.color-stroke').value; 

                    //draw Pen-line
                    ctx1.lineWidth = 3;
                    ctx1.lineCap ='round';
                    ctx1.strokeStyle = colorStroke;

                    ctx1.lineTo(e.clientX-offLeft, e.clientY-offTop)
                    ctx1.stroke();    
                    ctx1.beginPath();
                    ctx1.moveTo(e.clientX-offLeft, e.clientY-offTop);
                    
                }
            }
        }
    }
</script>