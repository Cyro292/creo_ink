<script>
    export default {
        name: '#pen',
        mounted() {
            pen.on('click', function(e) {

                //manage active button animation
                dragHand.removeClass("selected");
                pointerMouse.removeClass("selected");
                pen.addClass("selected");
                ereaser.removeClass("selected");
                text.removeClass("selected");
                square.removeClass("selected");
                circle.removeClass("selected");

                //manage cursor animation
                $('#canvas2').addClass("crosshair"); //cursor wird zum crosshair wenn auf canvas ist
                $('#canvas2').removeClass("grab");   // "
                $('#canvas2').removeClass("circleCursor");      
                $('#canvas2').toggleClass("pen");


                // remove other class-names
                $('#canvas2').removeClass("dragHand");
                $('#canvas2').removeClass("pointerMouse");
                $('#canvas2').removeClass("ereaser");
                $('#canvas2').removeClass("text");
                $('#canvas2').removeClass("square");
                $('#canvas2').removeClass("circle");

                console.log($('#canvas2').attr("class")); // jff

            });

        }
    }
</script>