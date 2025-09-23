import { createRouter, createWebHashHistory } from 'vue-router'
import Lessons from '@/Lessons.vue'
import Home from '@/Home.vue'
import TimeTable from '@/TimeTable.vue'

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/', component: Home},
    {path: '/lessons', component: Lessons},
    {path: '/timetable', component: TimeTable}
  ],
})

export default router
