import { createApp } from 'vue'
import { router } from './router'
import { store } from './vuexStore'
import Button from 'primevue/button';
import Column from 'primevue/column';
import DataTable from 'primevue/datatable';
import Dropdown from 'primevue/dropdown';
import PrimeVue from 'primevue/config';

import App from './App.vue'

import 'primevue/resources/themes/aura-light-green/theme.css'
import './style.css'

// Create and mount app
const app = createApp(App)
app.use(router)
app.use(store)
app.use(PrimeVue)
app.component('Button', Button)
app.component('Column', Column)
app.component('DataTable', DataTable)
app.component('Dropdown', Dropdown)
app.mount('#app')