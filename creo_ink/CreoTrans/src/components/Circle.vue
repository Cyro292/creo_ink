<template>
    <button @click="setUpCircle"  class="btn btn-sm circle"><i class="fa-regular fa-circle"></i></button>
</template>

<script>
    export default {
        name: 'Circle',
        mounted() {
            
        },
        methods: {
            setUpCircle() {
            
                //manage active button animation
                $(".dragHand").removeClass("selected");
                $(".pointerMouse").removeClass("selected");
                $(".pen").removeClass("selected");
                $(".ereaser").removeClass("selected");
                $(".text").removeClass("selected");
                $(".square").removeClass("selected");
                $(".circle").addClass("selected");

                //manage cursor animation
                $('#canvas2').addClass("crosshair"); //cursor wird zum crosshair wenn auf canvas ist
                $('#canvas2').removeClass("grab");   // " 
                $('#canvas2').removeClass("circleCursor");     
                $('#canvas2').addClass("circle");


                // remove other class-names
                $('#canvas2').removeClass("dragHand");
                $('#canvas2').removeClass("pointerMouse");
                $('#canvas2').removeClass("pen");
                $('#canvas2').removeClass("ereaser");
                $('#canvas2').removeClass("text");
                $('#canvas2').removeClass(".square");
                
                console.log($('#canvas2').attr("class")); // jff

            },
            drawEllipse(e) {

                if ($('#canvas2').hasClass('mouseDown')) {
                    
                    //update color
                    colorStroke = $('.color-stroke').value;
                    
                    //calculate travelled distance
                    deltaX = e.clientX - posX;
                    deltaY = e.clientY - posY;

                    //calculate center
                    centerX = posX + (deltaX / 2);
                    centerY = posY + (deltaY / 2);

                    //calculate horizonatal(x) and vertical(y) radius -> Math.sqrt; Math.pow to only return positive values
                    radiusX = Math.sqrt(Math.pow((deltaX), 2)); //if not rough divide deltaX (inside purple brackets) with two
                    radiusY = Math.sqrt(Math.pow((deltaY), 2)); //if not rough divide deltaX (inside purple brackets) with two

                    console.log(radiusX, radiusY);

                    ///draw rectangle

                    // ctx2.lineWidth = 3;
                    // ctx2.strokeStyle = colorStroke;
                    // ctx2.clearRect(0, 0, $('#canvas2').width, $('#canvas2').height);
                    // ctx2.beginPath();
                    // ctx2.setLineDash([]);
                    // ctx2.ellipse(centerX, centerY, radiusX, radiusY, 0, 0, 180);
                    // ctx2.stroke();     
                    
                    ctx2.clearRect(0, 0, canvas2.width, canvas2.height);
                    rc2.ellipse(centerX, centerY, radiusX, radiusY);
                }

            },
            saveEllipse() {
                console.log('X: '+centerX + '+' + offLeft);
                console.log('Y: '+centerY + '+' + offTop);

                // ctx1.beginPath();
                // ctx1.strokeStyle = ctx2.strokeStyle;    //bring color of $('#canvas2') and canvas1 in line
                // ctx1.lineWidth = ctx2.lineWidth;    //bring lineWidth of $('#canvas2') and canvas1 in line
                // ctx1.ellipse(centerX + offLeft, centerY + offTop, radiusX, radiusY, 0, 0, 180);
                // ctx1.stroke();

                rc1.ellipse(centerX - offLeft, centerY - offTop, radiusX, radiusY);

                ctx1.beginPath();   //to prevent 'linejumping' in case drawPen() is called afterwards
            }
        }
    }
</script>