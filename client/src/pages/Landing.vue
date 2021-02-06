<template>
  <div id="landing">
    <div id="container">
      <el-row :gutter="24">
        <el-col :span="1" align-items="left">
          <a href='/About'><el-button round type="circle" src="button" class="button1">about us</el-button></a>
        </el-col>
        <el-col :span="23" z-index="4">
        </el-col>
      </el-row>

      <el-col :span="11"><div class="grid-content">
        <span>
         <img src="../assets/logo.png" class="img" alt="image">
        <div class="title">
          food4thought
        </div>
        </span>
      </div></el-col>
    </div>
  <div id="background">
      
      <div class = "grid-content2">
      <link href="https://fonts.googleapis.com/css2?family=Kumbh+Sans&display=swap" rel="stylesheet">
      <p src = "slogan" class = "slogan">supporting local in the pandemic</p>
  </div>

  </div>
  </div>
</template>

<script scoped>

export default {
  name: 'Landing',
  components: {

  },
}
</script>

<style scoped>

.img {
    margin-top: 15%;
}
.title {
  font-family: 'Kumbh Sans', sans-serif;
  font-weight: bold;
  font-size: 100px;
  margin-top: 5%;
  color: #8cc4ff;
}
.el-col {
    border-radius: 4px;
    position: relative; /* Declared position allows for location changes */
    top: -5px; /* Moves the image 5px closer to the top of the page */
}

body {
  direction: ltr;
  margin: 0;
  padding: 0;
  /* make it look decent enough #C8E7F5*/
  position: relative;
  height: 100%; 
}

img {
    height: 200px;
    width: 200px;
}

#home {
  font-family: 'Kumbh Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
  background-color:azure;
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
  color: black;
  font-family: 'Kumbh Sans', sans-serif;
  font-size: 20px;
  text-align: left;
}


.button1:hover {
   background-color: azure;
   color: black;
}
.slogan {
  font-family: 'Kumbh Sans', sans-serif;
  font-weight: bold;
  font-style: italic;
  font-size: 30px;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #3C3C3C;
}


</style>