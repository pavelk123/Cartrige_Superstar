<template>
  <div class="container-fluid">
    <div class="row flex-nowrap">
              <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0 bg-dark ">
            <div class="d-flex flex-column align-items-center align-items-sm-start px-3 pt-2 text-white min-vh-100">
                <a href="/" class="d-flex align-items-center pb-3 mb-md-0 me-md-auto text-decoration-none">
                    <span class="fs-5 d-none d-sm-inline text-white">Cartrige<b class="text-danger">Superstar</b></span>
                </a>
                <ul class="nav nav-pills d-flex flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start " id="menu">
                    <li class="nav-item ">
                        <a href="#" class="nav-link align-middle px-0 text-white">
                            <i class="fs-4 bi-house"></i> <span class="ms-1 d-none d-sm-inline">Главная</span>
                        </a>
                    </li>
                    <li>
                        <a href="#submenu1" data-bs-toggle="collapse" class="nav-link px-0 align-middle text-white ">
                            <i class="fs-4 bi-grid"></i> <span class="ms-1 d-none d-sm-inline">Каталог</span> </a>
                        <ul class="collapse show nav flex-column ms-1" id="submenu1" data-bs-parent="#menu">
                            <li class="w-100">
                                <a href="#" class="nav-link px-0 text-white"><i class="fs-5 bi-app text-danger"> </i><span class="d-none d-sm-inline ">Картриджи</span> </a>
                            </li>
                            <li>
                                <a href="#" class="nav-link px-0 text-white"> <i class="fs-5 bi-app text-danger"></i><span class="d-none d-sm-inline">Принтеры</span> </a>
                            </li>
                        </ul>
                    </li>


                    <li>
                        <a href="#submenu3" data-bs-toggle="collapse" class="nav-link px-0 align-middle text-white">
                            <i class="fs-4 bi-file-earmark-arrow-up"></i> <span class="ms-1 d-none d-sm-inline">Добавить в БД</span> </a>
                            <ul class="collapse nav flex-column ms-1 " id="submenu3" data-bs-parent="#menu">
                            <li class="w-100">
                                <a href="#" class="nav-link px-0 text-white"><i class="fs-5 bi-app text-danger"></i> <span class="d-none d-sm-inline ">Картридж</span> </a>
                            </li>
                            <li>
                                <a href="#" class="nav-link px-0 text-white"><i class="fs-5 bi-app text-danger"> </i><span class="d-none d-sm-inline ">Модельную Серию</span> </a>
                            </li>
                            <li>
                                <a href="#" class="nav-link px-0 text-white"><i class="fs-5 bi-app text-danger"> </i><span class="d-none d-sm-inline ">Принтер</span> </a>
                            </li>
                            <li>
                                <a href="#" class="nav-link px-0 text-white"><i class="fs-5 bi-app text-danger"> </i><span class="d-none d-sm-inline ">Организацию</span> </a>
                            </li>
                        </ul>
                    </li>
                    <li>
                        <a href="#" class="nav-link px-0 align-middle text-white">
                            <i class="fs-4 bi-question-square text-warning "></i> <span class="ms-1 d-none d-sm-inline ">Уведомления</span> </a>
                    </li>
                </ul>
                <hr>
                <div class="dropdown pb-4">
                    <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle" id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
                        <img src="https://github.com/mdo.png" alt="hugenerd" width="30" height="30" class="rounded-circle">
                        <span class="d-none d-sm-inline mx-1">User</span>
                    </a>
                    <ul class="dropdown-menu dropdown-menu-dark text-small shadow">
                        <li><a class="dropdown-item" href="#">New project...</a></li>
                        <li><a class="dropdown-item" href="#">Settings</a></li>
                        <li><a class="dropdown-item" href="#">Profile</a></li>
                        <li>
                            <hr class="dropdown-divider">
                        </li>
                        <li><a class="dropdown-item" href="#">Sign out</a></li>
                    </ul>
                </div>
            </div>
        </div>

        
        <div class="col py-3">
            
          <div>  
              <div class="form d-flex justify-content-between">   
                  <input class=" " id="searchBar" type="text" placeholder="Поиск"/>
                  <span class="glyphicon glyphicon-search col-xs-1" data-toggle="tooltip" title="Search"><i class="fs-4 bi-search text-danger"></i></span>
              
              
              </div>
          </div>
   

            <router-view></router-view>
        </div>
    
    </div>
  </div>

</template>

<script>
// import Sidebar from './components/Sidebar.vue'
// import Search from './components/Search.vue'
// import HomePage from './components/Home.vue'

export default {
    name: 'App',
  // components: {
  //   Sidebar,
  //   Search,
  //   HomePage
  // }
}
</script>

<style>
@import '~bootstrap/dist/css/bootstrap.css';
@import '~bootstrap-icons/font/bootstrap-icons.css';

input{
  padding:0;
  border-radius: 0;
  border: none;
  font-size: 20px;
  color: #bbb;
  background:none;
  letter-spacing: 1px;
  word-spacing: 10px;
  font-family: 'Arvo', sans-serif;
  padding: 0;
  line-height: 25px;
}

.form{
  padding: 10px 0;
  padding-right: 15px;
  border: 3px solid #E35865;
  
}






body{
  background: #eee;
  letter-spacing: 2px;
  min-height: 101vh;
}

a:hover, a:active{
  text-decoration: none;
}

input[type="text"], select{ 
    outline: none;
}

.col-xs-1{
  padding:0;
}

h1{
  font-family: 'Arvo', sans-serif;
  color:#E35865;
}

header.container-fluid{
  margin: 0;
  background-color: #39404A;
  box-shadow: 0 0px 3px 3px rgba(0,0,0,.4);
  height: 100vh;
  min-height: 150px;
}

.container{
  max-width: 720px;
  margin: auto;
  padding: 0 50px;
}

ul{
  padding: 0;
}



li > h3{
  margin-top:0;
  color: #E35865;
  line-height: 2;
}

li > p{
  color: #666;
  line-height: 2;
}



#searchBox{
  padding-top: 40vh;
}

button{
  background: none;
  border: none;
}



.form.col-xs-12{
  padding-left: 2px;
}

.glyphicon{
  color: #E35865;
  font-size: 20px;
  line-height: 25px;
}

.glyphicon-search{
  cursor: pointer;

}

.glyphicon-search:hover{

}




li:hover{
  box-shadow: 0 0 15px 15px rgba(0,0,0,.1);
}

::-webkit-input-placeholder {
  color: #bbb;
  opacity: 1;
}

:-moz-placeholder { /* Firefox 18- */
  color: #bbb;
  opacity: 1;
}

::-moz-placeholder {  /* Firefox 19+ */
  color: #bbb;
  opacity: 1;
}

:-ms-input-placeholder {  
  color: #bbb;
  opacity: 1;
}

#mainBody{
  font-family: 'Montserrat', sans-serif;
}

/*********media query starts ***********/

@media screen and (max-width: 420px){
  #searchBar,.glyphicon{
    font-size: 16px;
  } 
  
  h1{
    font-size: 28px;
  } 
}

#app {

  
}
</style>
