import { defineStore } from 'pinia'

export const updateCanvas = defineStore({
    id: 'updateCanvas',
    state: () => ({
        //CANVAS
        windowW: null,
        windowH: null,
        
        canvas1: null,
        canvas2: null,
        
        canvasObjects: [],
        canvasObjectsBin: [],
        selectedIndex: [],

        ctx1: null,
        ctx2: null,
        rc1: null,
        rc2: null,

        rect: null,
        elps: null,

        mouseIsDown: null,

        posX: null,
        posY: null,
        
        centerX: null,
        centerY: null,

        deltaX: null,
        deltaY: null,

        offLeft: 0,
        offTop: 0,

        //styling
        //strokeClr: do seperate store for color?
        //BackGClr: do seperate store for color?

        roughness: 0.5,
        strokeWidth: 3,
    }),
    actions: {
        undo() {
            var removedElement = this.canvasObjects.pop();
            this.canvasObjectsBin.push(removedElement);

            //update canvas drawing to updated arrays
            this.ctx1.clearRect(0, 0, this.canvas1.width, this.canvas1.height);
            this.canvasObjects.forEach((obj, index) => {
                if (index !== this.selectedObjectIndex) {

                    this.rc1.rectangle(obj.x, obj.y, obj.width, obj.height, {
                        roughness: obj.roughness,
                        fillStyle: obj.fillStyle, //later this.fill when reading out of fillBtn works
                        fill: obj.fill,
                        stroke: obj.stroke,
                        strokeWidth: obj.strokeWidth,
                    });

                }
            });

        },
        redo() {
            var recycledElement = this.canvasObjectsBin.pop();
            this.canvasObjects.push(recycledElement);

            //update canvas drawing to updated arrays
            this.ctx1.clearRect(0, 0, this.canvas1.width, this.canvas1.height);
            this.canvasObjects.forEach((obj, index) => {
                if (index !== this.selectedObjectIndex) {

                    this.rc1.rectangle(obj.x, obj.y, obj.width, obj.height, {
                        roughness: obj.roughness,
                        fillStyle: obj.fillStyle, //later this.fill when reading out of fillBtn works
                        fill: obj.fill,
                        stroke: obj.stroke,
                        strokeWidth: obj.strokeWidth,
                    });

                }
            });
        }
    }
})

