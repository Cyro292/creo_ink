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
		path: "/resetPassword",
		name: "resetPassword",
		component: () =>
			import(/* webpackChunkName: "about" */ "../views/ResetPasswordView.vue"),
	},
	{
		path: "/newPassword",
		name: "newPassword",
		component: () =>
			import(/* webpackChunkName: "about" */ "../views/NewPasswordView.vue"),
	},
	{
		path: "/drawboard",
		name: "drawboard",
		component: () =>
			import(/* webpackChunkName: "about" */ "../views/DrawBoardView.vue"),
	},
	{
		path: "/notepadtest",
		name: "Notepadtest",
		component: () =>
			import(/* webpackChunkName: "about" */ "../views/NotepadView.vue"),
	},
	{
		path: "/boardcollection",
		name: "BoardCollection",
		component: () =>
			import(/* webpackChunkName: "about" */ "../views/BoardCollectionView.vue"),
	},
	{
		path: "/joinboard",
		name: "BoardJoinen",
		component: () =>
			import(/* webpackChunkName: "about" */ "../views/BoardJoinenView.vue"),
	},
	{
		path: "/note",
		name: "Note",
		component: () =>
			import(/* webpackChunkName: "about" */ "../views/NoteView.vue"),
	},
	{
		path: "/boardsnew",
		name: "Boards",
		component: () =>
			import(/* webpackChunkName: "about" */ "../views/BoardsNewView.vue"),
	},
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

export default router;
