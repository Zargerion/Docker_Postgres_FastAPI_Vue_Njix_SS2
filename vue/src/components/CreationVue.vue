<template>
    <div class=" mx-auto">
        <div class="bg-gray-200 p-6 rounded special" v-for="item in items" :key="item.id">
            <img :src="item.image" :alt="item.image" class="rounded-lg shadow-lg mb-3">
            <h1 class="text-gray-800 text-lg font-semibold m-2">{{item.type}}</h1>
            <p class="text-gray-600 text-justify m-4 mt-0">{{item.description}}</p>
            <a :href="item.link" class="text-blue-500 hover:text-blue-700">Link</a>
        </div>
        <InfiniteLoading/>
    </div>
</template>

<script>
    
    import axios from 'axios'
    import InfiniteLoading from 'vue-infinite-loading';
    export default {
        name: 'CreationVue',
        components: {
            InfiniteLoading
        },
        data() {
            return {
            items: [],
            };
        },
        methods: {
            async getItems() {
            await axios.get('/api/creations/')
                .then((res) => {
                this.items = res.data;
                })
                .catch((error) => {
                console.error(error);
                });
            },
        },
        created() {
            this.getItems()
        }
    }
</script>

<style scoped>
    @import '../index.css';

    .special {
        background-color: #f2f2f2;
        margin: 0 auto 20px auto;
    }
    img {
        object-fit:scale-down;
        margin: 0 auto;
    }

    @media (min-width: 785px) and (orientation: landscape) {
        img {
            max-width: 500px;
        }
        .special {
            max-width: 700px;
        }
    }

    @media (max-width: 785px) and (orientation: landscape) {
        .special {
            max-width: 60px;
        }
    }

</style>