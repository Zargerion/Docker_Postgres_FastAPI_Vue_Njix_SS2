<template>
  <div class="full-viewport">
    <div class="back-image">
      <img :src="require(`@/assets/MainLogoSubter2.png`)">
    </div>
    <div class="logo-frame">
      <div>Sabter.Site</div>
    </div>
    <div class="start-parent">
      <router-link :to="{ name: 'Creations' }" class="start-button">ENTER</router-link>
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
.back-image {
  position: absolute;
  animation: scroll 17s linear infinite;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  opacity: 0.03;
  z-index: 2;
}

@keyframes scroll {
  from { left: -120%; }
  to { left: 220%; }
}

.full-viewport {
  position: relative;
  height: 100vh;
  width: 100vw;
  background-color: #010114;
  display: grid;
  grid-template-rows: repeat(3, 1fr);
  z-index: 1;
}

.logo-frame {
  width: 20em;
  height: 5rem;
  border-bottom-right-radius: 25px;
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  background-color: #d5a202;
}

.logo-frame > div {
  text-decoration: none;
  margin: 0.3em;
  font-size: 3em;
  font-family: 'Times New Roman';
  font-weight: bold;
  color: white;
}

.start-parent {
  position: relative;
  z-index: 3;
  display: flex;
  justify-content: center;
  align-items: center;
}

.start-button {
  background-color: #e1a900e1;
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
  margin: 0 1em 1em 0;
  opacity: 95%;
}
</style>
