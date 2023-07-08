<script>
	export default {
		name: "StickyNote",
		props: [
            'text',
            'color',
            'color2',
            'permission',
            'users',
        ],
        data() {
            return {
            showKnick: false,
            }
        },
        methods:{
           
        }
};
</script>

<template>
<div>
   
    <div class="arrow">
    <div class="container" @mouseenter="showKnick = true" @mouseleave="showKnick = false">
      <div v-if="!showKnick" class="arrowbody" v-bind:style="{ backgroundColor: color }" ></div>
      <div v-if="showKnick" class="arrowknick" v-bind:style="{ backgroundColor: color2 }"></div>
      <div v-if="showKnick" class="arrowknick1" v-bind:style="{ backgroundColor: color }"></div>
      <div v-if="showKnick" class="arrowknick2" v-bind:style="{ backgroundColor: color }"></div>
    </div>
    <div class="containertop" @mouseenter="showKnick = true" @mouseleave="showKnick = false">
        <div class="arrowtop" v-bind:style="{ backgroundColor: color }"></div>
    </div> 
    </div>
    <div class="text">{{ text }} {{ permission }} {{ users }}</div>
</div>
</template>
  

<style scoped>
.arrow{
    opacity: 60%;
}
.text{
    color: var(--text-clr);
    width: 9em;
    height: 3.2em;
    text-align: center;
    margin-left: -2.5em;
    font-size: xx-large;
    margin-top: .3rem;
}
.arrowtop{
    transform: skew(35deg);
    border-radius: .4rem;
    height: 3rem;
    width: 3.75rem;
}

.arrowbody{
    color: var(--text-clr);
    height: 3.2rem;
    width: 9rem;
}

.arrowknick{
    height: 3.2rem;
    width: 9rem;
    border-bottom-right-radius: 3em 1.3em;
    margin-top: 0rem;
}

.arrowknick1{
    height: 2.2rem;
    width: 1.7rem;
    border-bottom-right-radius: 2em 1em;
    border-bottom-left-radius: 2em 1em;
    margin-top: -3.2rem;
    margin-left: 7.3rem;
}

.arrowknick2{
    height: 3.2rem;
    width: 8rem;
    border-bottom-right-radius: 3em 1.3em;
    margin-top: -2.2rem;
}

.containertop {
   transform: rotate(-25deg);
   margin-top: -5.6rem;
   margin-left: -2.5rem;
}

</style>
