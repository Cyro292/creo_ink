<template>
    <button @click="setUpRectangle" class="btn btn-sm square"><i class="fa-regular fa-square"></i></button>
</template>

<script>
    export default {
        name: 'Rectangle',
        moundet() {
            
        },
        methods: {
            setUpRectangle() {
        
                //manage active button animation
                $(".dragHand").removeClass("selected");
                $(".pointerMouse").removeClass("selected");
                $(".pen").removeClass("selected");
                $(".ereaser").removeClass("selected");
                $(".text").removeClass("selected");
                $(".square").addClass("selected");
                $(".circle").removeClass("selected");
    
                //manage cursor animation
                $('#canvas2').addClass("crosshair"); //cursor wird zum crosshair wenn auf canvas ist
                $('#canvas2').removeClass("grab");   // " 
                $('#canvas2').removeClass("circleCursor");     
                $('#canvas2').addClass("square");
    
    
                // remove other class-names
                $('#canvas2').removeClass("dragHand");
                $('#canvas2').removeClass("pointerMouse");
                $('#canvas2').removeClass("pen");
                $('#canvas2').removeClass("ereaser");
                $('#canvas2').removeClass("text");
                $('#canvas2').removeClass("circle");
                
                console.log($('#canvas2').attr("class")); // jff
    
            },
            drawRect(e)  {

                if ($('#canvas2').hasClass('mouseDown')) {

                    //update color
                    colorStroke = $('.color-stroke').value;
                    colorBg = $('.color-bg').value;

                    //calculate travelled distance
                    deltaX = e.clientX - posX;
                    deltaY = e.clientY - posY;

                    console.log(deltaX, deltaY);

                    //draw rectangle

                    // ctx2.lineWidth = 5;
                    // ctx2.lineJoin = 'round';
                    // ctx2.fillStyle = colorBg;
                    // ctx2.strokeStyle = colorStroke;
                    // ctx2.clearRect(0, 0, $('#canvas2').width, $('#canvas2').height);
                    // ctx2.beginPath();
                    // ctx2.fillRect(posX, posY, deltaX, deltaY);           
                    // ctx2.rect(posX, posY, deltaX, deltaY);
                    // ctx2.stroke();

                    ctx2.clearRect(0, 0, canvas2.width, canvas2.height);
                    rc2.rectangle(posX, posY, deltaX, deltaY);

                }
            },
            saveRect() {

                ///bring color of canvas1 and $('#canvas2') in line

                // ctx1.fillStyle = ctx2.fillStyle;    
                // ctx1.strokeStyle = ctx2.strokeStyle;

                // ctx1.lineWidth = ctx2.lineWidth;
                // ctx1.lineJoin = ctx2.lineJoin;

                // ctx1.fillRect(posX, posY, deltaX, deltaY);
                // ctx1.rect(posX, posY, deltaX, deltaY);
                // ctx1.stroke();

                rc1.rectangle(posX - offLeft, posY - offTop, deltaX, deltaY);

                ctx1.beginPath();   //to prevent 'linejumping' in case drawPen() is called afterwards

            }
        }
    }
</script>