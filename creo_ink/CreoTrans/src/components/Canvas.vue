<template>
    <canvas id="canvas1"></canvas>
    <canvas id="canvas2"></canvas>
</template>

<script>

export default {
    name: 'Canvas',

    mounted() {
        var windowW = window.innerWidth;    //!!!  problematic since window-alignment only takes place when refreshing
        var windowH = window.innerHeight;   //!!!!  in case you scale canvas down or up $('#canvas2') doesen't scale accordingly and drawable section on the screen decreases

        //temporary canvas that gets engaged by user
        const canvas2 = document.querySelector('#canvas2');
        const ctx2 = canvas2.getContext('2d');
        const rc2 = rough.canvas(document.querySelector('#canvas2'));
        
        canvas2.width = windowW;
        canvas2.height = windowH;
        
        //permanent canvas that holds all drawings
        const canvas1 = document.querySelector('#canvas1'); 
        const ctx1 = canvas1.getContext('2d');
        const rc1 = rough.canvas(document.querySelector('#canvas1'));
        
        canvas1.width = windowW * 3;
        canvas1.height = windowH * 3;
        
        //align canvas1 in center
        canvas1.style.left = '-1920px';
        canvas1.style.top = '-502px';

        
        //Add Event-Listeners to canvas mouseevents
        $('#canvas2').on('mousedown', mouseDown); 

        $('#canvas2').on('mouseup', mouseUp);    

        $('#canvas2').on('mousemove', mouseMove);

        $('#canvas2').on('click', mouseClick);
        
    }

}

</script>

<style scoped>
    #canvas2{
        position: absolute;
        top: 0;
        left: 0;
    }

    #canvas1{
        position: absolute;
        top: -1920px;
        left: -502px;
    }
</style>