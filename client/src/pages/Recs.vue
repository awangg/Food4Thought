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
 
 
  <div>
  <b-card-group deck>
    <b-card v-for="res in recs" :key="res.gPlusPlaceId" :title="res.name" class="r1" >
      <img class = "icon" src="~@/assets/blue_icon.png">
      <b-card-text>
        This is a wider card with supporting text below as a natural lead-in to additional content.
        This card has even longer content than the first to show that equal height action.
      </b-card-text>
      <template #footer>
        <small class="text-muted">Address</small>
      </template>
    </b-card>
  </b-card-group>
</div>


  </div>

</template>

<script scoped>

export default {
  data() {
    return {
      recs: [],
      key: 'AIzaSyAiFbxvrMV6zhM2rnJYLFu1lvkEyYHI8ZI'
    }
  },
  mounted() {
    this.recs = this.$route.params.results
  }
}
</script>

<style scoped>

.icon {
    width: 240px;
    height: 200px;
}

.r1 {
    font-size: 20px;
    padding-right: 60%;
    padding-left: 10%;
    margin-top: -15%;
}

.r2 {
    font-size: 20px;
    padding-left: 60%;
    padding-right: 10%;
    margin-top: -15%;

}


.title {
  font-family: 'Kumbh Sans', sans-serif;
  font-weight: bold;
  font-size: 80px;
  margin-top: 7%;
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
  padding-bottom: 16%;
}


</style>