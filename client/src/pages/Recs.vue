<template>
  <div id="recs" class="d-flex align-items-center">
      <div class="row">
        <div id="map" class="col-md-6 col-sm-12">
        </div>
        <div class="col-md-6 col-sm-12" id="results">
            <div class="row d-flex justify-content-center"
                v-for="rec in recs"
                :key="rec.name">
                <div class="col-6">
                    <b-card
                      :title="rec.name"
                      img-alt="image"
                      img-top
                      tag="article"
                      style="max-width: 20rem;"
                      class="mb-2"
                    >
                        <b-card-text>
                          {{ rec.formatted_address }}
                        </b-card-text>
                        <b-button :href="rec.url" variant="primary" class="mr-3">See More</b-button>
                        {{ rec.rating }}  <i class="fas fa-star star"></i>
                    </b-card>
                </div>
            </div>
        </div>
      </div>
  </div>
</template>

<script scoped>
export default {
  data() {
    return {
      recs: [],
      map: null,
      mapCenter: { lat: 30, lng: -95 }
    }
  },
  mounted() {
    this.recs = this.$route.params.results
    this.recs.sort( function(a, b) {
      let aRate = parseFloat(a.rating)
      let bRate = parseFloat(b.rating)
      return bRate - aRate
    })
    this.initMap()
    this.initRecs()
  },
  methods: {
    initMap() {
        this.map = new window.google.maps.Map(document.getElementById('map'), {
          center: this.mapCenter,
          zoom: 10,
          maxZoom: 20,
          minZoom: 3,
          streetViewControl: false,
          mapTypeControl: false,
          fullscreenControl: false,
          zoomControl: false
        })
    },
    initRecs() {
      this.recs.forEach( (value) => {
        let marker = new window.google.maps.Marker({
          position: value.location,
          map: this.map,
          label: {
            text: value.name,
            color: '#000'
          }
        })
        console.log(marker)
      })
    }
  }
}
</script>

<style scoped>
#recs {
  height: 100vh;
}

#map {
  width: 60vw;
  height: 60vh;
  border: 4px solid black;
}

#results {
  overflow-y: scroll;
  height: 60vh;
}

.star {
  color: goldenrod;
}
</style>