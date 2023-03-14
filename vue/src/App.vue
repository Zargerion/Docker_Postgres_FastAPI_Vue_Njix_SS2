<template>
  <router-view/>
</template>

<style lang="scss">
#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

::-webkit-scrollbar {
  width: 0.4rem;
  background-color: #010114;
}

::-webkit-scrollbar-track {
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: #d5a202; 
  border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
  background: #010114; 
}

html, body{
  width: 100vw;
  height: 100vh;
  padding: 0;
  margin: 0;
  overflow-x: hidden;
}

</style>
