<template>
    <button @click="setUpDragHand" class="btn btn-sm dragHand"><i class="fa-regular fa-hand"></i></button>
</template>

<script>
    export default {
        name: 'DragHand',
    
        methods: {
            setUpDragHand() {
                //manage active button animation
                $(".dragHand").addClass("selected");
                $(".pointerMouse").removeClass("selected");
                $(".pen").removeClass("selected");
                $(".ereaser").removeClass("selected");
                $(".text").removeClass("selected");
                $(".square").removeClass("selected");
                $(".circle").removeClass("selected");

                $('#canvas2').addClass("grab"); //cursor wird zu grab (fallback: move) wenn er auf canvas ist
                $('#canvas2').removeClass('crosshair');
                $('#canvas2').removeClass("circleCursor");

                // remove other class-names
                $('#canvas2').removeClass("pointerMouse");
                $('#canvas2').removeClass("pen");
                $('#canvas2').removeClass("ereaser");
                $('#canvas2').removeClass("text");
                $('#canvas2').removeClass("square");
                $('#canvas2').removeClass("circle");



                console.log($('#canvas2').attr("class")); // jff                
            }
        }
    }

</script>