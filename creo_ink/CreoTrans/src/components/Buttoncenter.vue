<template>
    <section id="controlCenter">
        
        <section id="primarySection">
            
            <div class="top container">
            
                <Drag-Hand />
                <Selector-Box />
                <Pen />
                <Ereaser />
                <Textfield />
                <Rectangle />
                <Circle />
                
            </div>    
            <br><br>
            <div class="bottom container">
    
                <button @click="undo" class="btn btn-dark btn-sm arrowLeft"><i class="fa-solid fa-arrow-left"></i></button>
                <button @click="redo" class="btn btn-dark btn-sm arrowRight"><i class="fa-solid fa-arrow-right"></i></button>
                <button class="btn btn-dark btn-sm arrowDown"><i class="fa-solid fa-arrow-down"></i></button>
                <button class="btn btn-dark btn-sm copy"><i class="fa-regular fa-clone"></i></button>
                <button class="btn btn-dark btn-sm trash"><i class="fa-solid fa-trash"></i></button>
            
            </div>
        </section>
        
        <section id="secondarySection">
            
            <div class="style-schemes">
                <StyleSchemes />
            </div>
    
            <div class="opacity">
                <label for="opacity">Opacity:</label>
                <input @click="getOpactiy" class='opacity_range' type="range" value="1" step="0.1" min="1" max="3">
            </div>

        </section>
        
    </section>
</template>


<style scoped>
    #controlCenter {
        margin: 1rem 0 0 1rem; 
        position: absolute;
        background-color: rgb(197, 177, 232);
        padding: 10px;
        border-radius: 1rem;
    }

    #primarySection {
        text-align: center;
    }

    #secondarySection {
        margin-left: 1.5rem;
    }
    .container{
        background-color: rgba(42, 42, 42, 0.422);
        padding: 7px 0;
        border-radius: 1rem;
        display: inline-block;
        position: relative;
        /* z-index: 1000; */
    }

    .btn {
        margin: 0 10px;
        width: 2rem;
    }

    .selected {
        background: rgba(0, 0, 0, .5);
    }

    .color-schemes, .bgType, .opacity {
        text-align: left;
    }

    .none {
        background-color: white;
        color: black;
    }

    .solid {
        background-color: black;
        color: beige;
    }

    .checked {
        background-color: #e25dc7;
    }
    /* .opacity { 
        
    }

    input[type="range"]::-webkit-slider-runnable-track {
        background: #053a5f;
        height:0.5rem;
    }

    input[type="range"]::-webkit-slider-thumb {}*/


</style>

<script> 
    import DragHand from './DragHand.vue'
    import SelectorBox from './SelectorBox.vue'
    import Pen from './Pen.vue'
    import Ereaser from './Ereaser.vue'
    import Textfield from './Textfield.vue'
    import Rectangle from './Rectangle.vue'
    import Circle from './Circle.vue'
    import StyleSchemes from './StyleSchemes.vue'
    import { updateCanvas } from '../stores/store.js'



    export default{
        name: 'ButtonCenter',
        components: {
            DragHand,
            SelectorBox,
            Pen,
            Ereaser,
            Textfield,
            Rectangle,
            Circle,
            StyleSchemes,
        },
        data() {
            return {
                counter: 0,
            };
        },
        methods: {
            getOpactiy() {
                console.log($('opacity_range'));
            },
            defineVars() {
                
                //defining lowerControl buttons
                const arrowLeft = $(".arrow-left");
                const arrowRight = $(".arrow-right");
                const arrowDown = $(".arrow-down");
                const copy = $(".copy");
                const trash = $('.trash');
        
                const cursor = $('.circleCursor');    
                
                // create reference to coordinate-saving-place
        
        
                //update offset position
                offLeft = canvas1.offsetLeft;
                offTop = canvas1.offsetTop;
        
                
            },
            undo() {
                if (updateCanvas().canvasObjects.length > 0) {
                    updateCanvas().undo();
                }
            },
            redo() {
                if (updateCanvas().canvasObjectsBin.length > 0) {
                    updateCanvas().redo();
                }
            }

        }

    }
</script>