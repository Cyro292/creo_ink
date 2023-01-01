<script>
// @ is an alias to /src
import TopLogo from "@/components/TopLogo.vue";
import NavBar from "@/components/NavBar.vue";

export default {
	name: "HomeView",
	components: {
	},
};
</script>

<template>
	<body>

		<div class="header">
			<h1>Creo.<span>An endless sketchboard.</span></h1>
			<p class="desc">
				Designed for intuitive brainstorming and fun tinkering.
			</p>
			<p class="intro">
				Collaborate in <span>real time</span> or brainstrom with our whiteboard.
			</p>
		</div>

		<div class="sub-header">
			<ul>
				<div class="marker c"></div>
				<h3>Collarborative</h3>
			</ul>
			<ul>
				<div class="marker w"></div>
				<h3>Whiteboard</h3>
			</ul>
		</div>

		<div class="schemes">
			<div class="collaborative">
				<div class="room-container">
					<div class="room-A">
						Room-A
						<li></li>
					</div>
					<div class="room-B">
						Room-B
						<li></li>
					</div>
					<div class="room-C">
						Room-C
						<li></li>
					</div>
					<div class="room-D">
						Room-D
						<li></li>
					</div>
				</div>
			</div>

			<div class="whiteboard"></div>
		</div>

		<div class="WIC" id="WIC">
			<div class="underline"></div>
			<h2>What is Creo?</h2>
			<p>
				Lorem ipsum dolor sit amet consectetur adipisicing elit. Cumque sapiente
				quasi pariatur cum expedita iure, ut nesciunt praesentium quos ratione,
				incidunt eos! Inventore iure quae odit perspiciatis totam, nemo, aliquid
				officia tenetur quidem quod amet natus sed ducimus? Minima qui,
				repudiandae quidem minus voluptatibus velit ducimus voluptate aperiam
				harum deserunt molestias eaque soluta nulla consequuntur sunt incidunt
				maiores quaerat omnis iste sed. Eligendi reprehenderit facere delectus
				necessitatibus quibusdam repellendus laborum corporis quisquam vitae
				cupiditate nobis fugit repellat blanditiis, adipisci culpa veritatis
				ratione, praesentium at. Dolorum praesentium cupiditate non voluptatibus
				magni laboriosam ducimus ab? Id, corporis! Explicabo porro illo iusto
				aspernatur!
			</p>
		</div>
		<div class="about_us" id="about_us">
			<div class="underline"></div>
			<h2>About us</h2>
			<p>
				Lorem ipsum dolor, sit amet consectetur adipisicing elit. Sint fuga
				repellat iusto accusantium provident earum cupiditate, accusamus
				recusandae pariatur magni, dolore reiciendis, veritatis quam culpa.
				Voluptas expedita, dignissimos aperiam ipsam aliquam quam quibusdam
				nobis. Aliquam nobis officia illum accusamus similique voluptatem, minus
				esse cupiditate numquam ipsa, quisquam molestias qui. Odio tempora eaque
				nemo est vero! Id laudantium nulla, soluta ducimus architecto modi!
				Iusto labore adipisci libero nisi eaque reprehenderit eius doloribus
				laudantium blanditiis cum sunt dolore porro corrupti exercitationem
				itaque, quasi tempore architecto aut maxime, reiciendis illum a quidem
				optio? Sunt dolorem nisi, quaerat beatae error corrupti itaque rerum
				repudiandae!
			</p>
		</div>
	</body>
</template>

<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Anton&family=Gloria+Hallelujah&family=Gluten&family=Permanent+Marker&family=Roboto+Mono&display=swap");
:root {
	--text-clr: black;
	--text-accent: grey;
	--accent-clr1: #ffdca8;
	--accent-clr2: #d0f4de;
	--accent-clr3: #ffaaaa;
	--accent-clr4: #a9def9;
	--accent-clr5: #b4ffa8;
	--accent-clr6: #fffbd7;
}

*,
*::before,
*::after {
	box-sizing: border-box;
	margin: 0;
	padding: 0;
}

body {
	font-family: "Gloria Hallelujah", cursive;
}

/*---------------------nav bar↓↓↓2♣↓------------------------------------*/

/*-----------------------------------------------*/

.header {
	text-align: center;
}

h1 span {
	display: block;
}

.desc {
	font-size: 0.8rem;
}

.intro {
	margin: 4rem 0 6rem 0;
}

/*-------------------------------------- ↓↓↓ midht ↓↓↓------------------------------------------*/

.schemes,
.sub-header {
	justify-content: space-around;
	display: flex;
}

h3 {
	margin-bottom: 1rem;
	margin-left: 0.2rem;
}

.sub-header ul {
	padding: 0;
	position: relative;
}

.marker {
	position: absolute;
	top: 30%;
	z-index: -1;
	border-radius: 0.5rem;
}

.marker.c {
	background-color: var(--accent-clr2);
	width: 9rem;
	height: 1rem;
	transform: rotate(-1.5deg);
}

.marker.w {
	background-color: var(--accent-clr3);
	width: 6.8rem;
	height: 1rem;
	transform: rotate(2deg);
}
.collaborative,
.whiteboard {
	position: relative;
	text-align: center;
	border: solid 0.1rem;
	border-radius: 1.2rem;
	margin-bottom: 2rem;
}

.collaborative {
	padding: 3rem 1rem 1rem 1rem;
}

.whiteboard {
	padding: 1rem 12rem;
}

.room-container {
	display: grid;
	grid-template-columns: 200px 200px;
	grid-template-rows: 125px 125px;
	grid-gap: 10px;
}

.room-A,
.room-B,
.room-C,
.room-D {
	border-radius: 5%;
	position: relative;
}

.room-A {
	background-color: var(--accent-clr1);
}

.room-B {
	background-color: var(--accent-clr5);
}

.room-C {
	background-color: var(--accent-clr3);
}

.room-D {
	background-color: var(--accent-clr4);
}

.room-container li {
	position: absolute;
	background-color: white;
	list-style-type: none;
	width: 100%;
	height: 0.08rem;
	top: 20%;
}
/* --------------------------------------------------------------------------------------------------------------------------------------------*/

.WIC,
.about_us {
	font-family: "Permanent Marker", cursive;
	width: 60%;
}

.WIC p,
.about_us p {
	margin-left: 1rem;
	padding: 0 3rem 1rem 1rem;
}

h2 {
	padding: 1rem 0 0 1.4rem;
}

.WIC {
	background-color: var(--accent-clr5);
	border-radius: 0 6rem 6rem 0;

	/*border: solid var(--accent-clr3);     -> darken element für clr einbauen*/
}

.about_us {
	margin-top: 2rem;
	float: right;
	background-color: var(--accent-clr6);
	border-radius: 4rem 0 0 4rem;

	/*border: solid var(--accent-clr1);     -> darken element für clr einbauen*/
}

/*.underline{
    display: -> ???! sodass nicht als block identifizeirt und keinen Platz verbarucht
    position: relative;
    top: 5rem;
    width: 40%;
    height: 2rem;
    background-color: var(--accent-clr3);
}*/
</style>
