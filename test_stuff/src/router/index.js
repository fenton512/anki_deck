import { createRouter, createWebHashHistory } from 'vue-router';
import WelcomPage from '@/pages/welcomPage.vue';
import Filter from '@/pages/filter.vue';
import FinalPage from '@/pages/finalPage.vue';
import Input from '@/pages/input.vue';
import Tinder from '@/pages/tinder.vue';
import FilterFromText from '@/pages/filterFromText.vue';
import FilterList from '@/pages/listFilter.vue';
import Review from '@/pages/review.vue';


const routes = [
  { path: '/', name: 'Welcom', component: WelcomPage },
  { path: '/filter', name: 'Filter', component: Filter },
  { path: '/result', name: 'FinalPage', component: FinalPage},
  { path: '/input', name: 'Input', component: Input},
  { path: '/tinder', name: 'Tinder', component: Tinder},
  { path: '/filterText', name: 'FilterFromText', component: FilterFromText},
  { path: '/filterList', name: 'List', component: FilterList},
  { path: '/review', name: 'Review', component: Review}

];

const router = createRouter({
  history: createWebHashHistory('/anki_deck/'),
  routes
});

export default router;
