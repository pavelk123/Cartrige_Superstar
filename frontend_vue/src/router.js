import {createRouter, createWebHashHistory} from 'vue-router';
import HomePage from "./components/HomePage.vue"
import CartrigeDetail from "./components/CartrigeDetail.vue"


export default createRouter({
    history:createWebHashHistory(),
    routes:[
        {path:'/',component:HomePage},
        {path: '/cartriges/:id',component:CartrigeDetail, name:'CartrigeDeatail',props: true },
    ],
})