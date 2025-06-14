import { createRouter, createWebHistory } from 'vue-router';
import WelcomPage from '@/pages/welcomPage.vue'

const routes = [
  { path: '/', name: 'Welcom', component: WelcomPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;