import { createRouter, createWebHistory } from 'vue-router';
import WelcomPage from '@/pages/welcomPage.vue'
import GenerSettings from '@/pages/generSetPage.vue'
import PasteTextPage from '@/pages/pasteTextPage.vue';
const routes = [
  { path: '/', name: 'Welcom', component: WelcomPage },
  { path: '/generSettings', name: 'GenerSettings', component:GenerSettings},
  {path: '/pasteText', name:'PasteText', component: PasteTextPage},
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;