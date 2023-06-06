<script>
    export default {
        name: 'SelectorBox',
        mounted() {
            pointerMouse.on('click', function(e) {

                //manage active button animation
                dragHand.removeClass("selected");
                pointerMouse.addClass("selected");
                pen.removeClass("selected");
                ereaser.removeClass("selected");
                text.removeClass("selected");
                square.removeClass("selected");
                circle.removeClass("selected");

                //manage cursor animation
                $('#canvas2').removeClass("crosshair"); //cursor wird zum pointer wenn auf canvas ist
                $('#canvas2').removeClass("grab");      // "
                $('#canvas2').removeClass("circleCursor");      
                $('#canvas2').toggleClass("pointerMouse");


                // remove other class-names

                $('#canvas2').removeClass("dragHand");
                $('#canvas2').removeClass("pen");
                $('#canvas2').removeClass("ereaser");
                $('#canvas2').removeClass("text");
                $('#canvas2').removeClass("square");
                $('#canvas2').removeClass("circle");

                console.log($('#canvas2').attr("class")); // j4f

            });

        }
    }
</script>