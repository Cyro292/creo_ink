<template>
	<body>
		<header>
			<a href="#">
				<div class="image-logo">
					<img
						src="../assets/logo-transparent.png"
						width="25"
						height="25"
						alt="image-logo"
					/>
				</div>
				<div class="logo">Creo</div>
			</a>
		</header>
    </body>
</template>

<style scoped lang="scss">

    header a {
        display: flex;
        text-align: center;
        align-items: center;
        gap: 0.6em;
        text-decoration: none;
        color: var(--text-clr);
    }

    header {
        /* background-color: #A9DEF9; */
        /* border-radius: .7em; */
        margin: 1em 1em 0 1em;
        /* width: 9rem; */
        /* padding: .3em;  */
    }

    header:hover {
        cursor: pointer;
    }

    .hero-bg {
        text-align: center;
    }

    h1 {
        font-size: 2.5rem;
        margin: 2em 0 1.2em;
    }

    h1 span {
        display: block;
    }

</style>