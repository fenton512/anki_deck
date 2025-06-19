import { createRouter, createWebHashHistory } from 'vue-router';
import WelcomPage from '@/pages/welcomPage.vue';
import GenerSettings from '@/pages/generSetPage.vue';
import PasteTextPage from '@/pages/pasteTextPage.vue';
import FinalPage from '@/pages/finalPage.vue';

const routes = [
  { path: '/', name: 'Welcom', component: WelcomPage },
  { path: '/generSettings', name: 'GenerSettings', component: GenerSettings },
  { path: '/pasteText', name: 'PasteText', component: PasteTextPage },
  { path: '/result', name: 'FinalPage', component: FinalPage}
];

const router = createRouter({
  history: createWebHashHistory('/anki_deck/'),
  routes
});

export default router;
