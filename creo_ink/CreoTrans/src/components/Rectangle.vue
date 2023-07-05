<template>
    <button @click="setUpRectangle" class="btn btn-sm square"><i class="fa-regular fa-square fa-xs"></i></button>
</template>

<script>
    export default {
        name: 'Rectangle',
            
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
            
        }
    }
</script>