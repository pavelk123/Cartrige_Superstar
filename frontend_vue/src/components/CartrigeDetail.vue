<template>
<div class="container mt-5 mb-5">
    <div class="row d-flex justify-content-center">
        <div class="col">
            <div class="card">
                <div class="row">
                    <div class="col">
                        <div class="images p-3">
                            <div class="text-center p-4"> <img id="main-image" src="https://skolkos.ru/wp-content/uploads/2016/10/laser6011.jpg" width="250" /> </div>
                            
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="product p-4">
                            <div class="d-flex justify-content-between align-items-center">
                                <div class="d-flex align-items-center"> <i class="fa fa-long-arrow-left"></i>  </div> <i class="fa fa-shopping-cart text-muted"></i>
                            </div>
                            <div class="mt-4 mb-3"> <span class="text-uppercase text-muted brand">Название</span>
                                <h5 class="text-uppercase">{{cartrige.title}}</h5>

                            </div>
                            <div class="mt-4 mb-3"> <span class="text-uppercase text-muted brand">Модельная серия</span>
                                <h5 class="text">{{cartrige.get_model_series}}</h5>

                            </div>
                            <div class="mt-4 mb-3"> <span class="text-uppercase text-muted brand">Количество:</span>
                                <b v-if="!cartrige.alert_quantity">{{cartrige.quantity}}</b>
                                <b class="text-danger" v-else>{{cartrige.quantity}} (Недостаточно)</b> 
                            </div>
                            <div class="cart mt-4 align-items-center"> <button class="btn btn-danger text-uppercase mr-2 px-4">Выдать</button> <i class="fa fa-heart text-muted"></i> <i class="fa fa-share-alt text-muted"></i> </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="py-3" >  
    <p class="text-center"><b>Совместимые принтеры</b></p>
    <table class="table table-hover table-striped">
        
        <thead>
            
            <tr class="table-danger">
                <th scope="col">#</th>
                <th scope="col">Ярлык</th>
                <th scope="col">Модель</th>
                <th scope="col">Место</th>
                
            </tr>
        </thead>
        <tbody>
            
            <tr 
                v-for="printer in printers"
                v-bind:key="printer.id">
                <th scope="row">{{printer.id}}</th>
                <td><router-link v-bind:to="printer.get_absolute_url" ><b>{{printer.hostname}}</b></router-link></td>
                <td>{{printer.model}}</td>
 
                <td>{{printer.place}}</td>
            </tr>
        </tbody>
    </table>
</div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CartrigeDetail',
    data(){
        return{
            cartrige:[],
            printers:[]
        }
    },
    mounted(){
        this.getCartrige(),
        this.getPrinters()
    },
    methods:{
        async getCartrige(){
            await axios.get('/api/v1/catalog/cartrige/'+this.$route.params.id)
                .then(response=>{
                    this.cartrige= response.data
                })
                .catch(
                    error=>{console.log(error)}
                )
        },
        async getPrinters(){
            await axios.get('/api/v1/catalog/cartrige/'+this.$route.params.id+'/factory_printers/')
                .then(response=>{
                    this.printers=response.data
                    console.log(response.data)
                }).catch(
                    error=>{console.log(error)}
                )
        }
    }
};



</script>


<style scoped>
a{
    text-decoration: none;
}


</style>