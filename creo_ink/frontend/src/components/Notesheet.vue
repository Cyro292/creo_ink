<template>
  <div class="paper">
    <div class="pin" @click="hideNotesheet">
      <div class="metal"></div>
      <div class="bottom-circle">
        <div class="x">x</div>
      </div>
    </div>
    <div class="shadow"></div>
    <div class="oc1"></div>
    <div class="oc2"></div>
    <div class="oc3"></div>
    <div class="oc4"></div>
    <p>hää</p>
  </div>
</template>

<script>
export default {
  name: "Notesheet",
  props: [
    'hideNotesheet'
  ],
  methods: {
  }
};
</script>

<style>
  :root {
  --paper-shadow: #e99e9e;
  --paper-color: #ffb0b0;
}

.x{
  transform: rotateY(35deg) rotateX(15deg);
  color: white;
  font-size: 2em;
  margin-top: .1em;
  margin-left: .1em;
}

.paper {
  position: absolute;
  display: flex;
  justify-content: center;
  width: 325px;
  height: 475px;
  background: var(--paper-color);
  border-top-left-radius: 250px 15px;
  border-bottom-left-radius: 30px 115px;
  border-bottom-right-radius: 105px 120px; 
}

.shadow {
  position: absolute;
  display: flex;
  width: 325px;
  top: 350px;
  height: 125px;
  background: var(--paper-shadow);
  border-bottom-left-radius: 30px 115px;
  border-bottom-right-radius: 105px 120px; 
}

.oc1{
  background: var(--paper-color);
  position: absolute;
  width: 125px;
  top: 350px;
  height: 110px;
  border-bottom-left-radius: 105px 205px;
  left: 0px;
}

.oc2{
  background: var(--paper-color);
  position: absolute;
  width: 125px;
  top: 450px;
  height: 25px;
  border-bottom-left-radius: 65px 105px;
  border-top-left-radius: 200px 200px;
  left: 25px;
}

.oc3{
  background: var(--paper-color);
  position: absolute;
  width: 225px;
  top: 350px;
  height: 80px;
  border-bottom-right-radius: 405px 225px;
  right: 0px;
}

.oc4{
  background: var(--paper-color);
  position: absolute;
  width: 175px;
  top: 375px;
  height: 100px;
  border-bottom-right-radius: 275px 220px;
  border-top-right-radius: 200px 200px;
  right: 55px;
}

.paper p {
  margin: auto;
}

.pin {
  --pin-color: #d02627;
  --pin-dark: #9e0608;
  --pin-light: #f45454;

  position: absolute;
  left: 150px;
  width: 60px;
  height: 50px;
}


.metal {
  position: absolute;
  width: 5px;
  height: 20px;
  background: linear-gradient(to right, #808080, 40%, #eae8e8, 50%, #808080);
  border-radius: 0 0 30% 30%;
  transform: rotate(58deg);
  transform-origin: bottom left;
  top: 2px;
  left: 16px;
  border-bottom: 1px solid #808080;
}

.bottom-circle {
  position: absolute;
  right: 15px;
  width: 35px;
  height: 35px;
  border-radius: 50%;
  background-color: var(--pin-color);
  background: var(--pin-color);
  transform: rotateY(35deg) rotateX(15deg);
  top: -5px;
  right: 4px;
}


</style>

  