import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const routes = [
	{
		path: "/",
		name: "home",
		component: HomeView,
	},
	{
		path: "/login",
		name: "login",
		component: () =>
			import(/* webpackChunkName: "about" */ "../views/LoginView.vue"),
	},
	{
		path: "/signup",
		name: "signup",
		component: () =>
			import(/* webpackChunkName: "about" */ "../views/SignupView.vue"),
	},
	{
		path: "/drawboard",
		name: "drawboard",
		component: () =>
			import(/* webpackChunkName: "about" */ "../views/DrawBoardView.vue"),
	},
	{
		path: "/boardcollection",
		name: "BoardCollection",
		component: () =>
			import(/* webpackChunkName: "about" */ "../views/BoardCollectionView.vue"),
	},
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

export default router;
