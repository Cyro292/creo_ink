import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const routes = [
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
		path: "/drawBoard",
		name: "DrawBoard",
		component: () =>
			import(/* webpackChunkName: "about" */ "../views/DrawBoardView.vue"),
	},
  {
    path: '/Notepadtest',
    name: 'Notepadtest',
    component: () => import(/* webpackChunkName: "about" */ '../views/NotepadView.vue')
  }
];

