<script> 
import BaseButton from '@/components/Basebutton.vue';
import router from '@/router';


export default {
    data() {
        return {
            countleft: 0,
            countadded: 0
        }
    },
    mounted() { 

    },
    components: {
        BaseButton
    },
    methods: {
        goBack() {
            router.push({name: 'Filter'});
        },
    },
    watch: {
    }
}
</script>

<template>
   <main>
    <header>
        <h2 @click="goBack"><-- Вернуться назад</h2>
    </header>
        <div class = "header">Тиндер слов</div>
        <div class = "card-container">
            <div class = "goBack">
                Вернуться к предыдущему слову
            </div>
            <div class = "card">
                <img class="corner-img" src="/star.png" alt="star">
                <div class="word">Word</div>
                <div class = "button-container">
                    <button class = "like left"><img src="/dislike.png" alt="disike"></button>
                    <button class = "like right"><img src="/like.png" alt="like"></button>
                </div>
            </div>
            <h2>Слов осталось: {{ countleft }}</h2>
            <h2>Слов добавлено в деку: {{ countadded }}</h2>
        </div>
        
   </main>
</template>

<style scoped> 
    header h2 {
        font-size: 15px;
        font-weight: 100;
    }
    header h2:hover {
        cursor: pointer;
        text-decoration: underline;
        text-decoration-color: #fff;
        text-underline-offset: 4px;
    }
    main {
        margin: 0 px;
        font-family: "Roboto", sans-serif;
        font-optical-sizing: auto;
        font-weight: 300;
        font-style: normal;
        color: white;
        font-size: 17px;
    }
    header {
        font-family: "Inter", sans-serif;

    }
    .header {
        font-family: "Roboto", sans-serif;
        font-optical-sizing: auto;
        font-weight: 400;
        font-style: normal;
        font-variation-settings:      
        "wdth" 100;
        text-align: center;
        font-size: 32px;
    }
    .card-container {
        margin: 0 auto;
        width: 570px;
        margin-top: 88px;
    }
    .goBack {
        padding-left: 15px;
        font-size: 15px;
    }
    .goBack:hover {
        cursor: pointer;
        text-decoration:underline;
        text-decoration-color: #fff;
        text-underline-offset: 3px;
    }
    
    .card {
        width:100%;
        height: 230px;
        border: 2px solid white;
        border-radius: 20px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        position: relative;
    }
    .word {
        flex: 1 1 auto;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        font-family: "Roboto", sans-serif;
        font-size: 60px;
        font-weight: 350;
    }
    .button-container {
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        display: flex;
        justify-content: space-between;
        padding: 0 20px 20px 20px;
        box-sizing: border-box;
    }
    .like.left {
        align-self: flex-end;
    }
    .like.right {
        align-self: flex-end;
    }
    .like {
        background-color: transparent;
        border: 0px;
    }
    .corner-img {
        position: absolute;
        top: 15px;
        right: 25px;
    }
    .card-container h2{
        text-align: center;
        font-size: 20px;
        font-weight: 350;
    }
</style>