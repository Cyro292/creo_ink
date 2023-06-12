<template>
    <button @click="setUpText" class="btn btn-sm text"><i class="fa-solid fa-heading"></i></button>
</template>

<script>
    export default {
        name: 'Textfield',
        mounted() {
            
        },
        methods: {
            setUpText() {
        
                //manage active button animation
                $(".dragHand").removeClass("selected");
                $(".pointerMouse").removeClass("selected");
                $(".pen").removeClass("selected");
                $(".ereaser").removeClass("selected");
                $(".text").addClass("selected");
                $(".square").removeClass("selected");
                $(".circle").removeClass("selected");
    
                //manage cursor animation
                $('#canvas2').addClass("crosshair"); //cursor wird zum crosshair wenn auf canvas ist
                $('#canvas2').removeClass("grab");   // " 
                $('#canvas2').removeClass("circleCursor");     
                $('#canvas2').addClass("text");
    
    
                // remove other class-names
                $('#canvas2').removeClass("dragHand");
                $('#canvas2').removeClass("pointerMouse");
                $('#canvas2').removeClass("pen");
                $('#canvas2').removeClass("ereaser");
                $('#canvas2').removeClass("square");
                $('#canvas2').removeClass("circle");
    
                console.log($('#canvas2').attr("class")); // jff
                    
            },
        }
    }
</script>