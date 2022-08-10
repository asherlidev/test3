<template>
  <HeaderBar></HeaderBar>
  <TranSaction></TranSaction>
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import TranSaction from './components/TranSaction.vue'
import HeaderBar from './layout/HeaderBar.vue'
export default {
  name: 'App',
  components: {
    TranSaction,HeaderBar
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

}
</style>
