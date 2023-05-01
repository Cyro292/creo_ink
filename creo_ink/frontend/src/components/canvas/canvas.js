// Definitions

var windowW = window.innerWidth;    //!!!  problematic since window-alignment only takes place when refreshing
var windowH = window.innerHeight;   //!!!!  in case you scale canvas down or up canvas2 doesen't scale accordingly and drawable section on the screen decreases

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




// ------------------- Drawing section ----------------


//defining all buttons as variables

const dragHand = document.querySelector(".dragHand");
const pointerMouse = document.querySelector(".pointerMouse");
const pen = document.querySelector(".pen");
const ereaser = document.querySelector(".ereaser");
const text = document.querySelector(".text");
const square = document.querySelector(".square");
const circle = document.querySelector(".circle");
const arrowLeft = document.querySelector(".arrow-left");
const arrowRight = document.querySelector(".arrow-right");
const arrowDown = document.querySelector(".arrow-down");
const copy = document.querySelector(".copy");
const trash = document.querySelector('.trash');



//adding Eventlistener to each toolbar-buttons with its callback function

dragHand.addEventListener('click', function(e) {

    //manage active button animation
    dragHand.classList.add("selected");
    pointerMouse.classList.remove("selected");
    pen.classList.remove("selected");
    ereaser.classList.remove("selected");
    text.classList.remove("selected");
    square.classList.remove("selected");
    circle.classList.remove("selected");
    
    canvas2.classList.add("grab"); //cursor wird zu grab (fallback: move) wenn er auf canvas ist
    canvas2.classList.remove('crosshair');


    // remove other class-names
    canvas2.classList.remove("pointerMouse");
    canvas2.classList.remove("pen");
    canvas2.classList.remove("ereaser");
    canvas2.classList.remove("text");
    canvas2.classList.remove("square");
    canvas2.classList.remove("circle");
    
    

    console.log(canvas2.classList); // jff

});

pointerMouse.addEventListener('click', function(e) {

    //manage active button animation
    dragHand.classList.remove("selected");
    pointerMouse.classList.add("selected");
    pen.classList.remove("selected");
    ereaser.classList.remove("selected");
    text.classList.remove("selected");
    square.classList.remove("selected");
    circle.classList.remove("selected");

    //manage cursor animation
    canvas2.classList.remove("crosshair"); //cursor wird zum pointer wenn auf canvas ist
    canvas2.classList.remove("grab");      // "      
    canvas2.classList.toggle("pointerMouse");


    // remove other class-names

    canvas2.classList.remove("dragHand");
    canvas2.classList.remove("pen");
    canvas2.classList.remove("ereaser");
    canvas2.classList.remove("text");
    canvas2.classList.remove("square");
    canvas2.classList.remove("circle");
    
    console.log(canvas2.classList); // jff

});

pen.addEventListener('click', function(e) {

    //manage active button animation
    dragHand.classList.remove("selected");
    pointerMouse.classList.remove("selected");
    pen.classList.add("selected");
    ereaser.classList.remove("selected");
    text.classList.remove("selected");
    square.classList.remove("selected");
    circle.classList.remove("selected");

    //manage cursor animation
    canvas2.classList.add("crosshair"); //cursor wird zum crosshair wenn auf canvas ist
    canvas2.classList.remove("grab");   // "      
    canvas2.classList.toggle("pen");


    // remove other class-names
    canvas2.classList.remove("dragHand");
    canvas2.classList.remove("pointerMouse");
    canvas2.classList.remove("ereaser");
    canvas2.classList.remove("text");
    canvas2.classList.remove("square");
    canvas2.classList.remove("circle");
    
    console.log(canvas2.classList); // jff

});

ereaser.addEventListener('click', function(e) {

    // canvas.classList.add("none"); //cursor wird zum kreis wenn auf canvas ist 
                        //-> https://dev.to/mattmarquise/how-to-create-a-custom-circular-cursor-for-your-website-4i7p
    
    
    //manage active button animation
    dragHand.classList.remove("selected");
    pointerMouse.classList.remove("selected");
    pen.classList.remove("selected");
    ereaser.classList.add("selected");
    text.classList.remove("selected");
    square.classList.remove("selected");
    circle.classList.remove("selected");

    //manage cursor animation
    canvas2.classList.remove("grab"); 
    canvas2.classList.remove('crosshair');     // "      
    canvas2.classList.toggle("ereaser");


    // remove other class-names
    canvas2.classList.remove("dragHand");
    canvas2.classList.remove("pointerMouse");
    canvas2.classList.remove("pen");
    canvas2.classList.remove("text");
    canvas2.classList.remove("square");
    canvas2.classList.remove("circle");
    
    console.log(canvas2.classList); // jff

});

text.addEventListener('click', function(e) {

    //manage active button animation
    dragHand.classList.remove("selected");
    pointerMouse.classList.remove("selected");
    pen.classList.remove("selected");
    ereaser.classList.remove("selected");
    text.classList.add("selected");
    square.classList.remove("selected");
    circle.classList.remove("selected");

    //manage cursor animation
    canvas2.classList.add("crosshair"); //cursor wird zum crosshair wenn auf canvas ist
    canvas2.classList.remove("grab");   // "      
    canvas2.classList.toggle("text");


    // remove other class-names
    canvas2.classList.remove("dragHand");
    canvas2.classList.remove("pointerMouse");
    canvas2.classList.remove("pen");
    canvas2.classList.remove("ereaser");
    canvas2.classList.remove("square");
    canvas2.classList.remove("circle");
    
    console.log(canvas2.classList); // jff

});


square.addEventListener('click', function(e) {
    
    //manage active button animation
    dragHand.classList.remove("selected");
    pointerMouse.classList.remove("selected");
    pen.classList.remove("selected");
    ereaser.classList.remove("selected");
    text.classList.remove("selected");
    square.classList.add("selected");
    circle.classList.remove("selected");

    //manage cursor animation
    canvas2.classList.add("crosshair"); //cursor wird zum crosshair wenn auf canvas ist
    canvas2.classList.remove("grab");   // "      
    canvas2.classList.toggle("square");


    // remove other class-names
    canvas2.classList.remove("dragHand");
    canvas2.classList.remove("pointerMouse");
    canvas2.classList.remove("pen");
    canvas2.classList.remove("ereaser");
    canvas2.classList.remove("text");
    canvas2.classList.remove("circle");
    
    console.log(canvas2.classList); // jff

});


circle.addEventListener('click', function(e) {
    
    //manage active button animation
    dragHand.classList.remove("selected");
    pointerMouse.classList.remove("selected");
    pen.classList.remove("selected");
    ereaser.classList.remove("selected");
    text.classList.remove("selected");
    square.classList.remove("selected");
    circle.classList.add("selected");

    //manage cursor animation
    canvas2.classList.add("crosshair"); //cursor wird zum crosshair wenn auf canvas ist
    canvas2.classList.remove("grab");   // "      
    canvas2.classList.toggle("circle");


    // remove other class-names
    canvas2.classList.remove("dragHand");
    canvas2.classList.remove("pointerMouse");
    canvas2.classList.remove("pen");
    canvas2.classList.remove("ereaser");
    canvas2.classList.remove("text");
    canvas2.classList.remove("square");
    
    console.log(canvas2.classList); // jff

});



//add Eventlistener with its callback function to actionbar

trash.addEventListener('click', function() {

    //clear permanent canvas (canvas1)
    ctx1.clearRect(0, 0, canvas1.width, canvas1.height);
});







//-----------------  canvas -----------


//Add Event-Listeners to canvas mouseevents
canvas2.addEventListener('mousedown', mouseDown); 

canvas2.addEventListener('mouseup', mouseUp);    

canvas2.addEventListener('mousemove', mouseMove);

canvas2.addEventListener('click', mouseClick);   
    



// create reference to coordinate-saving-place

//define vars outside of function so it is always accessible
var centerX = null;
var centerY = null;

var colorStroke = '';
var colorBg = '';

var deltaX = null;
var deltaY = null;

var moveX = null;
var moveY = null;

var offLeft = null;
var offTop = null;

var posX = null;
var posY = null;

var radius = null;
var radiusX = null;
var radiusY = null;


//update offset position
offLeft = canvas1.offsetLeft;
offTop = canvas1.offsetTop;

// EventListener-functions

function mouseDown(e) {

    // define coordinates of execution
    posX = e.clientX;
    posY = e.clientY;

    canvas2.classList.add('mouseDown'); //tell other functions that mouse is down -> mouseMove functions whith condition of mouseDown can now be executed

    if (canvas2.classList.value.includes('grab') == true){   //activate grabbing cursor #dragHand
        canvas2.classList.remove('grab');
        canvas2.classList.add('grabbing');

    } 
        
}


function mouseUp(e) {

    canvas2.classList.remove('mouseDown');   // tell other functions that mouse is NOT down anymore

    if (canvas2.classList.value.includes('pointerMouse') == false){ //so selector-box doesn't dissapear when releasing mouse
        ctx2.clearRect(0, 0, canvas2.width, canvas2.height);    //avoids overlaying effect since drawing is displayed on canvas1 and canvas2 until canvas2 is #mouseDown && #mouseMove
    }

    if (canvas2.classList.value.includes('grabbing') == true) {  //re-activate grab cursor #dragHand
        canvas2.classList.remove('grabbing');
        canvas2.classList.add('grab');

    } else if (canvas2.classList.value.includes('pen') == true) {   //end line to prevent 'linejumping'
        ctx1.beginPath();

    } else if (canvas2.classList.value.includes('square') == true) {    //transfer rectangle to permanent canvas
        console.log('triggered');
        saveRect();
        
    } else if(canvas2.classList.value.includes('circle') == true) {     //transfer ellipse to permanent canvas
        console.log('triggered');
        saveEllipse();
    } 

}

function mouseMove(e) {

    if (canvas2.classList.value.includes('grabbing') == true) {
        dragCanvas(e);
    } else if (canvas2.classList.value.includes('pointerMouse') == true) {
        selectorBox(e);
        
    } else if(canvas2.classList.value.includes('pen') == true) {
        drawPen(e);
    
    } else if (canvas2.classList.value.includes('ereaser') == true) {
        erease(e);

    } else if (canvas2.classList.value.includes('square') == true) {
        drawRect(e);

    } else if (canvas2.classList.value.includes('circle') == true) {
        drawEllipse(e);

    } 
    
}

function mouseClick(e) {
    console.log('click at: '+ e.clientX + 'X, ' + e.clientY + 'Y.');

    if (canvas2.classList.value.includes('text') == true) {
        drawText(e);
    }
}


///Canvas_Draw-functions

function dragCanvas(e) {
    
    //calculate travelled distance
    deltaX = e.clientX - posX;
    deltaY = e.clientY - posY;

    //move canvas  
    canvas1.style.left = (canvas1.offsetLeft + deltaX) + "px";
	canvas1.style.top = (canvas1.offsetTop + deltaY) + "px";
    console.log('offL: '+canvas1.offsetLeft);
    console.log('offT: '+canvas1.offsetTop);
    
    //update position
    posX = e.clientX;
    posY = e.clientY;

    //update offset position
    offLeft = canvas1.offsetLeft;
    offTop = canvas1.offsetTop;

    //limit drag-area
    if (offLeft > 0) {
        canvas1.style.left = 0;

    } if(offLeft < -3840) {
        canvas1.style.left = '-3840px';

    } if (offTop > 0) {
        canvas1.style.top = 0;

    } if (offTop < -1004) {
        canvas1.style.top = '-1004px';
    }
    

}

function selectorBox(e) {

    if (canvas2.classList.value.includes('mouseDown') == true) {

        //calculate travelled distance
        deltaX = e.clientX - posX;
        deltaY = e.clientY - posY;

        console.log(deltaX, deltaY);

        //draw rectangle
        ctx2.lineWidth = 2;
        ctx2.strokeStyle = "#ff0000";
        ctx2.clearRect(0, 0, canvas2.width, canvas2.height);
        ctx2.beginPath();
        ctx2.setLineDash([5, 5]);
        ctx2.rect(posX, posY, deltaX, deltaY); 
        ctx2.stroke(); 
        
    }

}

function drawPen(e) {

    if (canvas2.classList.value.includes('mouseDown') == true) {

        //update color
        colorStroke = document.querySelector('.color-stroke').value; 

        //draw Pen-line
        ctx1.lineWidth = 3;
        ctx1.lineCap ='round';
        ctx1.strokeStyle = colorStroke;

        ctx1.lineTo(e.clientX-offLeft, e.clientY-offTop)
        ctx1.stroke();    
        ctx1.beginPath();
        ctx1.moveTo(e.clientX-offLeft, e.clientY-offTop);
        
    }
}

function drawText(e) {

    var t = document.createTextNode("this is a test");
    
    
    // create new textarea element with its attributes
    
    var input = document.createElement('textarea');
    input.name = 'newText';
    input.id = 'text';
    input.cols = 80;
    input.rows = 0;
    input.style.left = posX + "px";
    input.style.top = posY + "px";

    // add the text node to the newly created div
    input.appendChild(t);
    document.body.appendChild(input);
    
}

function drawRect(e)  {

    if (canvas2.classList.value.includes('mouseDown') == true) {

        //update color
        colorStroke = document.querySelector('.color-stroke').value;
        colorBg = document.querySelector('.color-bg').value;

        //calculate travelled distance
        deltaX = e.clientX - posX;
        deltaY = e.clientY - posY;

        console.log(deltaX, deltaY);

        //draw rectangle

        // ctx2.lineWidth = 5;
        // ctx2.lineJoin = 'round';
        // ctx2.fillStyle = colorBg;
        // ctx2.strokeStyle = colorStroke;
        // ctx2.clearRect(0, 0, canvas2.width, canvas2.height);
        // ctx2.beginPath();
    	// ctx2.fillRect(posX, posY, deltaX, deltaY);           
        // ctx2.rect(posX, posY, deltaX, deltaY);
        // ctx2.stroke();

        ctx2.clearRect(0, 0, canvas2.width, canvas2.height);
        rc2.rectangle(posX, posY, deltaX, deltaY);

    }
}



function drawEllipse(e) {

    if (canvas2.classList.value.includes('mouseDown') == true) {
        
        //update color
        colorStroke = document.querySelector('.color-stroke').value;
        
        //calculate travelled distance
        deltaX = e.clientX - posX;
        deltaY = e.clientY - posY;

        //calculate center
        centerX = posX + (deltaX / 2);
        centerY = posY + (deltaY / 2);

        //calculate horizonatal(x) and vertical(y) radius -> Math.sqrt; Math.pow to only return positive values
        radiusX = Math.sqrt(Math.pow((deltaX), 2)); //if not rough divide deltaX (inside purple brackets) with two
        radiusY = Math.sqrt(Math.pow((deltaY), 2)); //if not rough divide deltaX (inside purple brackets) with two

        console.log(radiusX, radiusY);

        ///draw rectangle

        // ctx2.lineWidth = 3;
        // ctx2.strokeStyle = colorStroke;
        // ctx2.clearRect(0, 0, canvas2.width, canvas2.height);
        // ctx2.beginPath();
        // ctx2.setLineDash([]);
        // ctx2.ellipse(centerX, centerY, radiusX, radiusY, 0, 0, 180);
        // ctx2.stroke();     
        
        ctx2.clearRect(0, 0, canvas2.width, canvas2.height);
        rc2.ellipse(centerX, centerY, radiusX, radiusY);
    }

}

function saveRect() {

    ///bring color of canvas1 and canvas2 in line

    // ctx1.fillStyle = ctx2.fillStyle;    
    // ctx1.strokeStyle = ctx2.strokeStyle;

    // ctx1.lineWidth = ctx2.lineWidth;
    // ctx1.lineJoin = ctx2.lineJoin;

    // ctx1.fillRect(posX, posY, deltaX, deltaY);
    // ctx1.rect(posX, posY, deltaX, deltaY);
    // ctx1.stroke();

    rc1.rectangle(posX - offLeft, posY - offTop, deltaX, deltaY);

    ctx1.beginPath();   //to prevent 'linejumping' in case drawPen() is called afterwards

}


function saveEllipse() {
    console.log('X: '+centerX + '+' + offLeft);
    console.log('Y: '+centerY + '+' + offTop);

    // ctx1.beginPath();
    // ctx1.strokeStyle = ctx2.strokeStyle;    //bring color of canvas2 and canvas1 in line
    // ctx1.lineWidth = ctx2.lineWidth;    //bring lineWidth of canvas2 and canvas1 in line
    // ctx1.ellipse(centerX + offLeft, centerY + offTop, radiusX, radiusY, 0, 0, 180);
    // ctx1.stroke();

    rc1.ellipse(centerX - offLeft, centerY - offTop, radiusX, radiusY);

    ctx1.beginPath();   //to prevent 'linejumping' in case drawPen() is called afterwards
}



function erease(e) {

    if (canvas2.classList.value.includes('mouseDown') == true) {

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