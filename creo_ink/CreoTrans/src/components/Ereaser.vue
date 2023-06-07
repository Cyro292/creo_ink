<template>
    <button @click="setUpEreaser"  class="btn btn-sm ereaser"><i class="fa-solid fa-eraser"></i></button>
</template>

<script>

    import EreaserCursor from './EreaserCursor.vue';
    export default {
        name: 'Ereaser',
        components: {
            EreaserCursor,
        },
        mounted() {
            
        },
        methods: {
            setUpEreaser() {

                
    
                // canvas.addClass("none"); //cursor wird zum kreis wenn auf canvas ist 
                                    //-> https://dev.to/mattmarquise/how-to-create-a-custom-circular-cursor-for-your-website-4i7p
    
    
                //manage active button animation
                $(".dragHand").removeClass("selected");
                $(".pointerMouse").removeClass("selected");
                $(".pen").removeClass("selected");
                $(".ereaser").addClass("selected");
                $(".text").removeClass("selected");
                $(".square").removeClass("selected");
                $(".circle").removeClass("selected");
    
                //manage cursor animation
                $('#canvas2').removeClass("grab"); 
                $('#canvas2').removeClass('crosshair');     // "      
                $('#canvas2').addClass("ereaser");
    
    
                // remove other class-names
                $('#canvas2').removeClass("dragHand");
                $('#canvas2').removeClass("pointerMouse");
                $('#canvas2').removeClass("pen");
                $('#canvas2').removeClass("text");
                $('#canvas2').removeClass("square");
                $('#canvas2').removeClass("circle");
    
                console.log($('#canvas2').attr("class")); // jff                
            },
            erease(e) {

                if ($('#canvas2').hasClass('mouseDown')) {

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


                    
                }
            }
        }
    }
</script>