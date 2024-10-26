import { createRouter, createWebHistory } from 'vue-router';
import UsersList from '../views/UserList.vue';
import UserPage from '../views/UserPage.vue';

const routes = [
  { path: '/', name: 'UsersList', component: UsersList },
  { path: '/users/:id', name: 'UserPage', component: UserPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
