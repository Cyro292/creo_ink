<template>
    <button @click="setUpSelector" class="btn btn-sm pointerMouse"><i class="fa-solid fa-arrow-pointer"></i></button>
</template>

<script>
    export default {
        name: 'SelectorBox',
        mounted() {
        },
        methods: {
            setUpSelector() {

                //manage active button animation
                $(".dragHand").removeClass("selected");
                $(".pointerMouse").addClass("selected");
                $(".pen").removeClass("selected");
                $(".ereaser").removeClass("selected");
                $(".text").removeClass("selected");
                $(".square").removeClass("selected");
                $(".circle").removeClass("selected");

                //manage cursor animation
                $('#canvas2').removeClass("crosshair"); //cursor wird zum pointer wenn auf canvas ist
                $('#canvas2').removeClass("grab");      // "
                $('#canvas2').removeClass("circleCursor");      
                $('#canvas2').addClass("pointerMouse");


                // remove other class-names

                $('#canvas2').removeClass("dragHand");
                $('#canvas2').removeClass("pen");
                $('#canvas2').removeClass("ereaser");
                $('#canvas2').removeClass("text");
                $('#canvas2').removeClass("square");
                $('#canvas2').removeClass("circle");

                console.log($('#canvas2').attr("class")); // j4f

            },
            selectorBox(e) {

                if ($('#canvas2').hasClass('mouseDown')) {

                    //calculate travelled distance
                    deltaX = e.clientX - posX;
                    deltaY = e.clientY - posY;

                    console.log(deltaX, deltaY);

                    //draw rectangle
                    ctx2.lineWidth = 2;
                    ctx2.strokeStyle = "#ff0000";
                    ctx2.clearRect(0, 0, canvas2.width, canvas2.height);
                    ctx2.beginPath();
                    ctx2.setLineDash([5, 5]);
                    ctx2.rect(posX, posY, deltaX, deltaY); 
                    ctx2.stroke(); 
                    
                }

            }

        }
    }
</script>