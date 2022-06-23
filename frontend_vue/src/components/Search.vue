<template>
  
  
    <div>  
        <div class="form d-flex justify-content-between">   
            <input class=" " id="searchBar" type="text" placeholder="Поиск"/>
            <span class="glyphicon glyphicon-search col-xs-1" data-toggle="tooltip" title="Search"><i class="fs-4 bi-search text-danger"></i></span>
        
        
        </div>
    </div>
   


        

</template>

<script>
export default {
  name: 'App',
  props: {
    msg: String
  }
};



</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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

</style>
