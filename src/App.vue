<template>
  <v-app>
    <v-app-bar title="BALANCEV GANDON" app>
    </v-app-bar>
    <v-card
        class="mx-auto"
        max-width="344"
    >
      <v-card-text>
        <div>Word of the Day</div>
        <p class="text-h4 text--primary">
          be•nev•o•lent
        </p>
        <p>adjective</p>
        <div class="text--primary">
          well meaning and kindly.<br>
          "a benevolent smile"
        </div>
      </v-card-text>
      <v-select
          v-model="test"
          label="Select"
          :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"
      ></v-select>
      <v-card-actions>
        <v-btn
            border
            variant="text"
            color="grey-darken-1"
        >
          Learn More
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      test: ''
    }
  },
  
  watch: {
    test(value) {
      console.log(value)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
