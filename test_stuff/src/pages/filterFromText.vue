<script>
import { useUserTextStore } from '@/stores/userText';
import Basebutton from '@/components/Basebutton.vue';
import router from '@/router';
import {useAPIStore} from "@/stores/API";

export default {
    data() {
        return {
            text: "",
            textStore: null,
            textArea: null,
            words: [],
            isVisiable: false,
            resp: {
                unknown_words: [],
                known_words: [],
                count: 0
            },
        }
    },
    mounted() {
        this.textStore = useUserTextStore();
        //after rendering get data from store
        this.text = this.textStore.text;
        this.textArea = document.getElementsByClassName("textarea")[0];
        this.validateWords();
    },
    components: {
        Basebutton
    },
    methods: {
        validateWords() {
            let wordsArr = this.text.trim().split(/(\s+)/);
            this.words = wordsArr.map((word) => {
                if (word == '\n') {
                    return {
                        word: '',
                        extrChars:['', '\n'],
                        class: "default"
                    }
                }
                let regex = /[a-zA-Z'`’-]+/;
                let newWord = regex.exec(word);
                if (newWord != null) {
                    return {
                    word: newWord[0],
                    extrChars: newWord.index == 0 ? 
                        ['', `${word.substring(newWord[0].length)} `] : 
                        [word.substring(0, newWord.index), `${word.substring(newWord.index + newWord[0].length)} `],
                    class: "default"
                    }
                } else {
                    return {
                        word: '',
                        extrChars: ['', `${word} `],
                        class: "default"
                    }
                }
            })
        },
        changeClass(index) {
            let word = this.words[index];
            let classes = ["default", "wantLearn", "neverLearn"];
            let current = classes.indexOf(word.class);
            let next = classes[(current+1)%3];
            word.class = next;
        },
        startGeneration() {
            for (let word of this.words) {
                switch (word.class) {
                    case "wantLearn":
                        this.resp.unknown_words.push(word.word);
                        break;
                    case "neverLearn":
                        this.resp.known_words.push(word.word);
                        break;
                }
            }
            let API = useAPIStore();
            API.setState(this.resp);
            router.push({name: "FinalPage"});
        },
        goFilter() {
            router.push({name: "Filter"})
        }
    }
}
</script>

<template>
    <header>
        <h2 @click="goFilter"><-- Вернуться к фильтрам</h2>
    </header>
    <main>
    <div class="main-container">
        <div class="heading-row">
        <div class="heading-group">
            <div class="heading-text">Выделение слов</div>
            <span class="question-mark" @mouseover="isVisiable = true" @mouseleave="isVisiable = false">?
                <span v-if="isVisiable" class="user-hint">Кликни по карточке со словом, чтобы задать ей статус:<br>
                        <span style="background-color: #71c686;">Зеленые карточки</span> – неизвестные слова<br>
                        <span style="background-color: #B74747;">Красные карточки</span> – слова, которые ты не хочешь учить
                    </span>
            </span>
        </div>
        </div>
        <div class="text-area" >
            <span v-for="(word, index) in words">
            <span>{{word.extrChars[0]}}</span>
            <span
            :key="index"
            :class="word.class"
            @click="this.changeClass(index)">
                {{word.word}}
            </span>
            <span>{{word.extrChars[1]}}</span>
            </span>
        </div>
        <div class="button-container">
            <Basebutton class="start-generation" @click="startGeneration()">Начать генерацию</Basebutton>
        </div>
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
    .heading-text{
        font-family: "Roboto", sans-serif;
        font-optical-sizing: auto;
        font-weight: 400;
        font-style: normal;
        font-variation-settings:      
        "wdth" 100;
        text-align: center;
        font-size: 32px;
    }
    main {
        margin: 0 px;
        font-family: "Roboto", sans-serif;
        font-optical-sizing: auto;
        font-weight: 300;
        font-style: normal;
        color: white;
    }
    header {
        font-family: "Inter", sans-serif;
    }
    header h2:hover {
        cursor: pointer;
        text-decoration: underline;
        text-decoration-color: #fff;
        text-underline-offset: 4px;
    }
    .default{
        background-color: inherit;
    }
    .wantLearn{
        background-color: #71c686;
    }
    .neverLearn{
        background-color: #B74747;
    }
    .main-container{
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 100%;
        text-align: center;
        width: 100%;
        max-width: 700px;
        margin: 0 auto;
    }
    .text-area{
        user-select: none;
        flex: 1 1 auto;
        white-space: pre-line;
        overflow-y: auto;
        min-height: 0;
        width: 100%;
        font-size: 22px;
        text-align:center;
        min-height: 400px;
    }
    .text-area span {
        user-select: none;
        pointer-events: none;
    }
    .text-area span[class] {
        pointer-events: auto;
        cursor: pointer;
    }
    .heading-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        margin-bottom: 10px;
        position: relative;
    }
    .heading-text {
        flex: 1;
        text-align: center;
        font-size: 30px;
        margin: 0;
    }
    .button-container{
        flex: 0 0 auto;
        min-height: 13%;
        /* height: 50%; */
    }
    .start-generation{
        width: 255px;
        height: 60px;
        margin-top:20px;
        border-radius: 0%;
    }
    .text-area {
        scrollbar-width: thin;
        scrollbar-color: #888 var(--color-background);
        
    }
    .text-area, .text-area * {
        user-select: none !important;
    }
    .text-area ::selection, .text-area ::-moz-selection {
        background: transparent;
    }
    .text-area {
    user-select: none; /* Standard property */
    -webkit-user-select: none; /* Safari */
    -moz-user-select: none; /* Firefox */
    -ms-user-select: none; /* IE/Edge */
    
    /* Optional: Prevent highlighting when clicking rapidly */
    -webkit-tap-highlight-color: transparent;
}

/* For the spans inside text-area */
.text-area span {
    user-select: none;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
}

/* If you still see selection on click, add this */
.text-area span[class] {
    pointer-events: auto; /* Keep click events working */
    cursor: pointer; /* Show pointer cursor */
}
    .heading-row {
  display: flex;
  justify-content: center;
  width: 100%;
  margin-bottom: 10px;
}

.heading-group {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 12px; /* This controls the space between text and question mark */
}

.heading-text {
  font-size: 30px;
  margin: 0;
  position: relative;
}

.question-mark {
  border: 1px solid #888;
  border-radius: 50%;
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  cursor: pointer;
  flex-shrink: 0;
}

.user-hint {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  min-width: 400px;
  background-color: var(--color-background);
  border-radius: 10px;
  border: 1px solid white;
  padding: 10px;
  font-size: 18px;
  margin-top: 0;
  z-index: 10;
  margin-left:350px;
  text-align: left;
}

</style>