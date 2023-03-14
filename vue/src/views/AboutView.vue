<template>
  <div class="main-holder">
    <div class="title">Creations</div>
    <div class="container">
      <div class="division" ref="division">
          <nav id="menu" class="menu-left" ref="menu1">
            <button>link</button>
            <button>link</button>
            <button>link</button>
            <button>link</button>
            <button>link</button>
            <button>link</button>
            <button>link</button>
          </nav>
        <button id="show-button">>></button>
      </div>
      <div class=""></div>
      <div class="division">
        <nav id="menu" class="menu-right" ref="menu2">
          <button>link</button>
          <button>link</button>
          <button>link</button>
          <button>link</button>
          <button>link</button>
          <button>link</button>
          <button>link</button>
        </nav>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    const itemWidth = this.$refs.division.offsetWidth;
      this.$el.style.setProperty('--element-width',
      itemWidth.toString()  + 'px');
    const observer = new ResizeObserver( () => {
      const itemWidth = this.$refs.division.offsetWidth;
      this.$el.style.setProperty('--element-width',
      itemWidth.toString()  + 'px');
    });
    observer.observe(document.body);
    const menuLeft = document.querySelector('.menu-left');
    const menuRight = document.querySelector('.menu-right');
    const button = document.querySelector('#show-button');

    button.addEventListener('click', () => {
      if (menuLeft.classList.contains('open')) {
        menuLeft.style.transform = 'translateX(0)';
        menuRight.style.transform = 'translateX(0)';
        menuLeft.classList.remove('open');
      } else {
        menuLeft.style.transform = 'translateX(-100%)';
        menuRight.style.transform = 'translateX(100%)';
        menuLeft.classList.add('open');
      }
    });
  } 
}
</script>

<style scoped>
  .main-holder {
    height: 3000px;
    width: 100vw;
    background-color: #010114;
    text-align: center;
  }

  .title {
    display: inline-block;
    font-family:'Franklin Gothic Medium';
    font-size: 3em;
    color: #d5a202;
    margin: 2rem;
  }

  .container {
    display: grid;
    width: 100%;
    height: 70%;
    grid-template-columns: 10% 80% 10%;
  }

  .division {
    display: flex;
  }

  #menu {  
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: var(--element-width);;
    height: 52%;
    background-color: #d5a202;
    position: fixed;
    transition: all .5s ease;
  }

  .menu-left {
    border-top-right-radius: 10px;
    border-bottom-right-radius: 10px;
  }

  .menu-right {
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
  }

  button {
    text-decoration: none;
    color: white;
    background-color: #d5a202;
    border: none;
    width: 100%;
    height: 12%;
    font-family: 'Verdana';
  }

  #show-button {
    position: fixed;
    font-family: Helvetica, Arial, sans-serif;
    width: auto;
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
    height: 4%;
  }

  button:hover {
    background-color: #bd8e00;
  }

</style>
