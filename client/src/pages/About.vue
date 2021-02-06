<template>
  <div id="AboutUs">
    <link href="https://fonts.googleapis.com/css2?family=Kumbh+Sans&display=swap" rel="stylesheet">
    <h1  class = "about-title">about us</h1>    
    <h4 class='intro'> We are Andy, Claire, Megan, and Sarah, 4 sophomores at Rice University 
        passionate about food and supporting small businesses, especially through the pandemic. 
        Furthermore, if we look past the pandemic, local restaurants will still be recovering
        from the financial burdens of COVID-19. As a result, this project seeks to bring 
        visibility to these businesses, and support them as much as possible! </h4>
    <img src="~@/assets/andy.jpg" alt="face" class="face">
    <img src="~@/assets/claire_pic.png" alt="face" class="face">
    <img src="~@/assets/megan_new.png" alt="face" class="face">
    <img src="~@/assets/sarah.jpg" alt="face" class="face">
    <Logo/>
    <Footer />
  </div>
</template>

<script scoped>
//import Navbar from "./components/Navbar.vue"
import Logo from "../assets/logo.png";
export default {
  name: 'AboutUs',
  components: {
    Logo
  }
}
</script>

<style scoped>
body {
  direction: ltr;
  margin: 40px;
  background-color:#ffffff;
  /* make it look decent enough #C8E7F5*/
  color: #000000;
  overflow-x: hidden;
  position: relative;
  height: 100%; 
}
.about-title {
  font-family: 'Kumbh Sans', sans-serif;
  font-size: 80px;
  color: #ffb6b9;
  margin-top: 7%;
  margin-bottom: -10px;
}
.intro {
  font-size: 24px;
  margin-left: 20px;
  margin-right: 20px; 

}
.small_logo {
  width: 150px;
  height: 85px;
  margin-top: -400px;
  margin-bottom: 20px;
  margin-right:1200px;
}
.face {
  width: 300px;
  height: 350px;
  margin-left: 15px;
  margin-right: 15px;
  margin-top: 10px;
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
</style>