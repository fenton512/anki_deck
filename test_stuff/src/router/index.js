import { createRouter, createWebHashHistory } from 'vue-router';
import WelcomPage from '@/pages/welcomPage.vue';
import GenerSettings from '@/pages/generSetPage.vue';
import Filter from '@/pages/filter.vue';
import FinalPage from '@/pages/finalPage.vue';
import Input from '@/pages/input.vue';
import Tinder from '@/pages/tinder.vue';
import FilterFromText from '@/pages/filterFromText.vue'


const routes = [
  { path: '/', name: 'Welcom', component: WelcomPage },
  { path: '/generSettings', name: 'GenerSettings', component: GenerSettings },
  { path: '/filter', name: 'Filter', component: Filter },
  { path: '/result', name: 'FinalPage', component: FinalPage},
  { path: '/input', name: 'Input', component: Input},
  { path: '/tinder', name: 'Tinder', component: Tinder},,
  { path: '/filterText', name: 'FilterFromText', component: FilterFromText}

];

const router = createRouter({
  history: createWebHashHistory('/anki_deck/'),
  routes
});

export default router;
