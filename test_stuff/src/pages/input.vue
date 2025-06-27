
<script> 
import BaseButton from '@/components/Basebutton.vue';
import router from '@/router';
export default {
    data() {
        return {
            pickedWords: new Array(),
            userText: '',
            isDone: true,
        }
    },
    mounted() { 
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
        pickWords() {
            this.pickedWords = [];
            let words = this.userText.split(" ");
            let length = words.length;
            for (let i = 0; i < 10; i++) {
                this.pickedWords.push(words[Math.floor(Math.random() * length)])
            }
        },
        showProccessingTitle() {
            let div = document.createElement('div');
            div.innerHTML = "Proccessing...";
        },
        goToFilter() {
            router.push({name: 'Filter'});
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
        <h2 @click="goBack"><-- Вернуться назад</h2>
    </header>
        <div class = "header">Введите текст песни или книги</div>
        <div class = "form-container">
            <form>
                <textarea id = "text" v-model="userText" placeholder="Например:
To be, or not to be, that is the question. 
Whether..."></textarea>
            </form>
        </div>
        <!-- <BaseButton class = "submit" @click="fatchdata()">Сгенерировать деку</BaseButton> -->
        <BaseButton :onClick="goToFilter" class = "submit">Перейти к генерации деки</BaseButton>
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
    .form-container {
        align-self: center;
        width: 600px;
        margin: 0 auto;
        margin-top:20px;
    }
    #text {
        background-color: transparent;
        border-radius: 10px;
        padding-top:0.5em;
        height: 150px;
        border: 2px solid whitesmoke;
        width: 100%;
        color: white;
        box-sizing: border-box;
        padding-left: 0.5em;
        font-size: 14px;
        resize: vertical;
        font-size: 15px;
    }
    #text::placeholder {
        text-align: left;
        color: white;
        opacity: 0.8;
        font-size: 15px;
    }
    #text:focus {
        outline: none;
        box-shadow: none;
    }
    .submit {
        align-self: center;
        width: 255px;
        height: 60px;
        border-radius: 0;

        margin: 0 auto; 
        margin-top: 35px;
        
    }
    
</style>