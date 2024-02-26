import { createRouter, createWebHashHistory } from 'vue-router'
import FirmInformation from './components/FirmInfo.vue'
import InvestorInfo from './components/InvestorInfo.vue' 
import PathNotFound from './components/PathNotFound.vue'

// Create routes
const routes = [
    { path: '/', component: FirmInformation},
    { path: '/investors/:investor_id', component: InvestorInfo },
    { path: '/:pathMatch(.*)*', component: PathNotFound }
]

export const router = createRouter({
    history: createWebHashHistory(),
    routes: routes
})