<template>
    <div id="eat" class="d-flex align-items-center" style="height: 90vh;">
        <div class="container-fluid">
            <div class="row">
                <div class="col">
                    <div class="typewriter">
                        <h1> {{ this.message }} </h1>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-12">
                    <input v-model="query" type="text" class="mt-3" />
                </div>
            </div>
            <div class="row mt-5">
                <div class="col">
                    <button class="btn btn-lg btn-primary" v-on:click="this.sendReq">Order Up</button>
                </div>
            </div>
        </div>
    </div>
</template>



<script>
import axios from 'axios';

export default {
  methods: {
    sendReq() {
      console.log('yeeti on my deeti')
      axios({
          method: 'post',
          url: `http://localhost:5000/recommendation?request=${this.query}`
      }).then( (response) => {
          this.$router.push({ name: 'recs', params: { results: response.data } })
      })
    }
  },
  data() {
    return {
      messages: [
        'what are we feeling today?',
        'what would you like today?',
        'is this the krusty krab? no this is patrick.',
        'what are you in the mood for?',
        'food uwuwuwuwuwuwuwuwuwuwuwuwu?'
      ],
      message: "",
      query: ""
    }
  },
  mounted() {
    this.message = this.messages[Math.floor(Math.random()*5)]
  }
}
</script>

<style scoped>
.typewriter h1 {
  overflow: hidden; /* Ensures the content is not revealed until the animation */
  border-right: .15em solid orange;
  font-family: monospace;
  white-space: nowrap; /* Keeps the content on a single line */
  margin: 0 auto; /* Gives that scrolling effect as the typing happens */
  letter-spacing: .15em; /* Adjust as needed */
  animation: 
    typing 2s steps(40, end),
    blink-caret .75s step-end infinite;
}

/* The typing effect */
@keyframes typing {
  from { width: 0 }
  to { width: 100% }
}

/* The typewriter cursor effect */
@keyframes blink-caret {
  from, to { border-color: transparent }
  50% { border-color: orange; }
}

input {
  border: 0;
  font-family: 'Kumbh Sans', sans-serif;
  font-size: 2rem;
  box-shadow: -8px 10px 0px -7px #ebebeb, 8px 10px 0px -7px #ebebeb;
  -webkit-transition: box-shadow 0.3s;
  transition: box-shadow 0.3s;
  padding-left: .5rem;
}

input:focus {
  outline: none;
  box-shadow: -8px 10px 0px -7px #4EA6EA, 8px 10px 0px -7px #4EA6EA;
}
</style>
