
<script> 
import BaseButton from '@/components/Basebutton.vue';
import router from '@/router';
import { useUserTextStore } from '@/stores/userText';


export default {
    data() {
        return {
            pickedWords: new Array(),
            userText: '',
            isDone: true,
            validatedText: '',
            textStore: null,
        }
    },
    mounted() { 
        //this variable represents store, you can use all its actions as methods
        this.textStore = useUserTextStore();
    },
    components: {
        BaseButton
    },
    methods: {
    //this function is not need and should be deleted later
    //when all features on this page will be finished
        async fatchdata() {
            this.pickWords();
            const resp = {
                unknown_words: this.pickedWords,
            };
            const response = await fetch("https://anki.dbpg.ru/wordlist/post", {
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
        goToFilterText() {
            //using Store variable to set user text
            this.textStore.setText(this.userText);
            router.push({name: "FilterFromText"});
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
        <div class = "header">Введите текст песни или книги</div>
        <div class = "form-container">
            <form>
                <textarea id = "text" v-model="userText" placeholder="Например: To be, or not to be, that is the question. Whether..."></textarea>
            </form>
        </div>
        <BaseButton class = "submit" @click="goToFilterText()">Начать выборку слов</BaseButton>
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
        border: 1px solid whitesmoke;
        width: 100%;
        color: white;
        box-sizing: border-box;
        padding-left: 0.5em;
        font-size: 14px;
        resize: vertical;
        scrollbar-width: thin;
        scrollbar-color: #888 var(--color-background);
    }
    #text::placeholder {
        text-align: left;
        color: white;
        opacity: 0.8;
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
        border: 1px solid whitesmoke;
        margin: 0 auto; 
        margin-top: 300px;
        
    }
    
</style>