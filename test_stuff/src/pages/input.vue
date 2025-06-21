
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
                    words: this.pickedWords,
                };
                const response = await fetch("http://127.0.0.1:8000/wordlist/post", {
                    method: "POST",
                    headers: {
                        'Content-Type' : 'application/json'
                    },
                    body: JSON.stringify(this.resp)
                })
            const result = await response.json();
            if (result) {
                this.isDone = true;
            }
            console.log(result)
        },
        pickWords() {
            this.pickWords = [];
            let words = this.userText.split(" ");
            let length = words.length;
            for (let i = 0; i < 10; i++) {
                this.pickedWords.push(words[Math.floor(Math.random() * length)])
            }
        },
        showProccessingTitle() {
            let div = document.createElement('div');
            div.innerHTML = "Proccessing...";
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
        <BaseButton class = "submit" @click="showProccessingTitle(); fatchdata()">Сгенерировать деку</BaseButton>
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