<template>
  <div id="landing">
    <div id="container">
      <el-row :gutter="24">
        <el-col :span="1" align-items="left">
          <a href='/AboutUs'><el-button round type="circle" src="button" class="button1">about us</el-button></a>
        </el-col>
        <el-col :span="23" z-index="4">
        </el-col>
      </el-row>

      <el-col :span="11"><div class="grid-content">
        <span>
         <Logo />
        <div class="title">
          food4thought
        </div>
        </span>
      </div></el-col>
    </div>
  <div id="background"><div class = "grid-content2">

      <link href="https://fonts.googleapis.com/css2?family=Kumbh+Sans&display=swap" rel="stylesheet">
      <p src = "slogan" class = "slogan">supporting local in the pandemic</p>
  </div>

  </div>
  </div>
</template>

<script scoped>
import Logo from "../assets/logo.png"
export default {
  name: 'Landing',
  components: {
    Logo
  },
}
</script>

<style scoped>
.title {
  font-family: 'Kumbh Sans', sans-serif;
  font-weight: bold;
  font-size: 70px;
  margin-top: 20%;
}
.el-col {
    border-radius: 4px;
    position: relative; /* Declared position allows for location changes */
    top: -5px; /* Moves the image 5px closer to the top of the page */
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.grid-content2 {
  margin-top:20%;
}

body {
  direction: ltr;
  margin: 0;
  padding: 0;
  background-color:#c9deff;
  /* make it look decent enough #C8E7F5*/
  color: #000000;
  overflow-x: hidden;
  overflow-y: hidden;
  position: relative;
  height: 100%; 
}
#home {
  font-family: 'Kumbh Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
}
@media screen and (max-width: 399px) {
  body {
    overflow: visible;
    overflow-x: hidden;
  }
}
#item {
  margin: 0;
  padding: 0;
}
.button1{
  background-color: #C998C3;
  color: #ffffff;
  font-family: 'Kumbh Sans', sans-serif;
  text-align: center;
  font-size: 20px;
  width: 120px;
  height: 50px;
  margin-left: 10px;
  margin-top: -30px;
}
.button2 {
  background-color: #C998C3;
  color: #ffffff;
  line-height: 10px;
  background-position: center;
  font-family: 'Kumbh Sans', sans-serif;
  text-align: center;
  font-size: 30px;
  width: 120px;
  height: 60px;
}
.button3 {
  background-color: #C998C3;
  color: #ffffff;
  line-height: 10px;
  background-position: center;
  font-family: 'Kumbh Sans', sans-serif;
  text-align: center;
  font-size: 30px;
  width: 135px;
  height: 60px;
  top: 50px;
}
.button1:hover {
   background-color: #E4CEE0;
   color: #C998C3;
}
.slogan {
  font-family: 'Kumbh Sans', sans-serif;
  font-weight: bold;
  font-style: italic;
  font-size: 50px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #3C3C3C;
}


</style>