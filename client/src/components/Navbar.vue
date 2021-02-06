<template>
  <div class="container mt-5">
    <b-navbar toggleable="lg" type="light" variant="faded" id="navbar">
      
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item class="nav-item" right>
            <router-link class="nav-link" to="/"> Home </router-link>
          </b-nav-item>
          <b-nav-item class="nav-item" right>
            <router-link class="nav-link" to="/onboarding"> Let's Eat! </router-link>
          </b-nav-item>
          <b-nav-item class="nav-item" right>
            <router-link class="nav-link" to="/about"> About </router-link>
          </b-nav-item>

        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>


    

<script>
export default {
  methods: {
    
  }
}
</script>

<style scoped>
#navbar {
  background: #ffffff;
  font-family: Avenir;
  color: #2a2a2a;
}
b-navbar{
  background: #ffffff;
}
.nav-item {
  margin: 0rem 1rem;
}
.nav-link {
  text-decoration: none;
  color: #000;
}
.btn {
  background: #a2dce7;
  border-color: #a2dce7;
  color: #2a2a2a;
}
.btn:hover {
  background: #32afc7;
  color: #2a2a2a;
  border-color: #32afc7;
}
</style>