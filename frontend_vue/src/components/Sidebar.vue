<template>
  

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

        
        

</template>

<script>
export default {
  name: 'App',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style >
// .nav a:hover{
     background-color:#808080
 };


</style>
