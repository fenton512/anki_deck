<script> 
import BaseButton from '@/components/Basebutton.vue';
import router from '@/router';
import { useUserTextStore } from '@/stores/userText';

export default {
    data() {
        return {
        }
    },
    mounted() { 
        const store = useUserTextStore();
        store.resetStore();
    },
    components: {
        BaseButton
    },
    methods: {
        async fatchdata() {
            this.pickWords();
            const resp = {
                unknown_words: this.pickedWords,
            };
            const response = await fetch("http://127.0.0.1:8000/wordlist/post", {
                method: "POST",
                headers: {
                    'Content-Type' : 'application/json'
                },
                body: JSON.stringify(resp),
            })
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            let a = document.createElement('a');
            a.href = url;
            a.setAttribute("download", "Anki_deck.csv");
            document.body.appendChild(a);
            a.click();
            a.remove();
        },
        goBack() {
            router.push({name: "Welcom"})
        }
    },
    watch: {
        isDone(newIsDone) {

        }
    }
}
</script>

<template>
   <main>
    <header>
        <h2 @click="goBack"><-- Вернуться в начало</h2>
    </header>
        <div class = "header">Ваша колода готова!</div>
        <BaseButton class = "download"><img src = "/down.png"> <span>Скачать в формате .apkg</span></BaseButton>
        <BaseButton class = "download"> <img src = "/down.png"><span>Скачать в формате .csv</span></BaseButton>
   </main>
</template>

<style scoped> 
    main {
        margin: 0 px;
        font-family: "Inter", sans-serif;
        font-optical-sizing: auto;
        font-weight: 300;
        font-style: normal;
        color: white;
        font-size: 17px;
    }
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
        font-family: "Inter", sans-serif;;
    }
    .download {
        margin: 0 auto;
        margin-bottom:50px;
        font-size:25    px;
        display: flex;
        border: 2px solid #ffffff;
        align-items: center;
        justify-content: center;
        padding: 0 auto;
        gap: 10px;
    }
    .download span {
        /* Remove padding-bottom to align with image */
    }
    .download img {
        width: 40px;
        height: 40px;
        vertical-align: middle;
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
        margin-bottom: 50px;
    }
    
</style>