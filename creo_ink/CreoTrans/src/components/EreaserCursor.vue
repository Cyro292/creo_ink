<template>
    
</template>

<script>
    export default {
        name: 'EreaserCursor',
        methods: {
            ereaserCursor(e) {
                console.log('works');

                $('#canvas2').addClass("circleCursor");

                cursor.style.left = e.pageX + "px",
                cursor.style.top = e.pageY + "px";
            }
        }
    }
</script>