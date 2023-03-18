//import 'bootstrap/dist/css/bootstrap.css';

import { createApp } from 'vue'
import axios from 'axios';

import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';

createApp(App).use(store).use(router).mount('#app')
