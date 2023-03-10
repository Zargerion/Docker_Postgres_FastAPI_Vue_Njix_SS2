<template>
    <div>
      <div v-for="item in items">
        <span>{{item.title}}</span> &nbsp;
        <img :src="item.icon" width="20px" height="auto">
      </div>      
    </div>
  </template>
  <script>
  export default {
    data: () => ({
      items: [
          { title: 'Chat', icon: require('@/assets/chat.png') },
          { title: 'Vue',  icon: require('@/assets/logo.png') },
          { title: 'Notification', icon: require('@/assets/notification.png') },
        ],
    })
  }
  </script>