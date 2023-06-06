<script>
    export default {
        name: 'Ereaser',
        mounted() {
            ereaser.on('click', function(e) {

                // canvas.addClass("none"); //cursor wird zum kreis wenn auf canvas ist 
                                    //-> https://dev.to/mattmarquise/how-to-create-a-custom-circular-cursor-for-your-website-4i7p


                //manage active button animation
                dragHand.removeClass("selected");
                pointerMouse.removeClass("selected");
                pen.removeClass("selected");
                ereaser.addClass("selected");
                text.removeClass("selected");
                square.removeClass("selected");
                circle.removeClass("selected");

                //manage cursor animation
                $('#canvas2').removeClass("grab"); 
                $('#canvas2').removeClass('crosshair');     // "      
                $('#canvas2').toggleClass("ereaser");


                // remove other class-names
                $('#canvas2').removeClass("dragHand");
                $('#canvas2').removeClass("pointerMouse");
                $('#canvas2').removeClass("pen");
                $('#canvas2').removeClass("text");
                $('#canvas2').removeClass("square");
                $('#canvas2').removeClass("circle");

                console.log($('#canvas2').attr("class")); // jff

            });

        }
    }
</script>