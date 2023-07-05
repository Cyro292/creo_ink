<template>
    <button @click="setUpCircle"  class="btn btn-sm circle"><i class="fa-regular fa-circle fa-xs"></i></button>
</template>

<script>
    export default {
        name: 'Circle',
    
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
                $('#canvas2').removeClass("square");
                
                console.log($('#canvas2').attr("class")); // jff

            },
            
        }
    }
</script>