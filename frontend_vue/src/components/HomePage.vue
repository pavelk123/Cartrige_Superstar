<template>
  
  
    <div class="py-3" >  
    
    <table class="table table-hover table-striped">
        <thead>
            <tr class="table-dark">
                <th scope="col">#</th>
                <th scope="col">Название</th>
                <th scope="col">Модельная серия</th>
                <th scope="col">Количество</th>
                <th scope="col">Последнее обновление</th>
            </tr>
        </thead>
        <tbody>
            <tr 
                v-for="cartrige in cartriges"
                v-bind:key="cartrige.id">
                <th scope="row">{{cartrige.id}}</th>
                <td><router-link  v-bind:to="cartrige.get_absolute_url" ><b>{{cartrige.title}}</b></router-link></td>
                <td>{{cartrige.get_model_series}}</td>
                <td v-if="!cartrige.alert_quantity">{{cartrige.quantity}}</td>
                <td v-else class="text-danger"><b>{{cartrige.quantity}}</b></td>
                <td>{{cartrige.updated}}</td>
            </tr>
        </tbody>
    </table>
    </div>
   


        

</template>

<script>

import axios from 'axios'
export default {
    name: 'HomePage',
    data(){
        return{
            cartriges:[],
            errors:[]
        }
    },
    mounted(){
        this.getCartriges()
    },
    methods:{
        getCartriges(){
            axios.get('/api/v1/catalog/cartrige')
                .then(response=>{
                    this.cartriges= response.data
                })
                .catch(
                    error=>{console.log(error)}
                )
            },

        }
    
};



</script>


