import { createApp, } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'
import router from './router'
import Axios from 'axios'


Axios.defaults.baseURL = 'http://127.0.0.1:8000/'

const app= createApp(App);
app.use(router,Axios);

app.mount('#app');
import 'bootstrap/dist/js/bootstrap.js'


