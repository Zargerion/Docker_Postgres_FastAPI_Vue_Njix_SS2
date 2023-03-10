<template>
  <div class="full-viewport">
    <div class="logo-parent">
      <img :src="require(`@/assets/MainLogoSubter2.png`)">
    </div>
    <div class="start-parent">
      <router-link :to="{ name: 'about' }" class="start-button">ENTER</router-link>
    </div>
    <div class="links-parent">
      <img :src="require(`@/assets/youtube.png`)" alt="Image 1">
      <img :src="require(`@/assets/vk.png`)" alt="Image 2">
      <img :src="require(`@/assets/telegram.png`)" alt="Image 3">
      <img :src="require(`@/assets/discord.png`)" alt="Image 4">
      <img :src="require(`@/assets/e-mail.png`)" alt="Image 5">
    </div>
  </div>
</template>

<style>
.full-viewport {
  height: 100vh;
  width: 100vw;
  background-color: #040f29;
  display: grid;
  grid-template-rows: repeat(3, 1fr);
}

.logo-parent {
  display: flex;
  justify-content: start;
  align-items: flex-start;
}

.logo-parent > img {

  width: 13rem;
  height: auto;
  object-fit: contain;
  margin: 2%;
}

.start-parent {
  display: flex;
  justify-content: center;
  align-items: center;
}

.start-button {
  background-color: #fac70ed5;
  font-family: 'Times New Roman';
  color: #e8e8e8;
  padding: 0.40em 1.6em;
  border: none;
  cursor: pointer;
  font-size: 2.5em;
  border-radius: 10px;
  text-decoration: none;
}

.start-button:hover {
  background-color: #EB6E08;
}

.links-parent {
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
}

.links-parent > img {
  height: auto;
  width: 3rem;
  margin: 0 1% 1% 0;
}
</style>
