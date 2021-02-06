<template>
  <div id="landing">
    <div id="container">
      <el-col :span="11"><div class="grid-content">
        <span>
        <div class="title">
          your recommendations
        </div>
        </span>
      </div></el-col>
    </div>
  <div id="background">
      
      <div class = "grid-content2">
      <link href="https://fonts.googleapis.com/css2?family=Kumbh+Sans&display=swap" rel="stylesheet">
      <p src = "slogan" class = "slogan">here are your top local restaurant hits! </p>
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


.title {
  font-family: 'Kumbh Sans', sans-serif;
  font-weight: bold;
  font-size: 80px;
  margin-top: 5%;
  color: #ffb6b9;
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