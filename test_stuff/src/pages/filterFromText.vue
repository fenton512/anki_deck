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
                count: 0,
                context_sentences: []
            },
            sentences: []
        }
    },
    mounted() {
        this.textStore = useUserTextStore();
        //after rendering get data from store
        this.text = this.textStore.text;
        console.log(this.text);
        this.sentences = this.text.split(/[\.!?\n]+/)
                                    .filter((sentance) => sentance.length > 0)
                                    .map((sentance) => {
                                    return sentance.trim();
                                    });
        this.textArea = document.getElementsByClassName("textarea")[0];
        this.validateWords();
    },
    components: {
        Basebutton
    },
    methods: {
        validateWords() {
            let wordsArr = this.text.trim().split(/(\s+)/);
            let sentenceIndex = 0;
            let prevWord = "";
            this.words = wordsArr.map((word) => {
                let currentIndex = sentenceIndex;
                let endOfSentance = /[!?\.]+/.exec(word);
                if (endOfSentance != null) {
                    sentenceIndex++
                }
                if (word == '\n') {
                    if (/[!?\.]+/.exec(prevWord) == null)
                        sentenceIndex++;
                    return {
                        word: '',
                        extrChars:['', '\n'],
                        class: "default"
                    }
                }
                prevWord = word;

                let regex = /[a-zA-Z'`’-]+/;
                let newWord = regex.exec(word);
                if (newWord != null) {
                    return {
                    word: newWord[0],
                    extrChars: newWord.index == 0 ? 
                        ['', `${word.substring(newWord[0].length)} `] : 
                        [word.substring(0, newWord.index), `${word.substring(newWord.index + newWord[0].length)} `],
                    class: "default",
                    sentenceIndex: currentIndex
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
                        this.resp.context_sentences.push(this.sentences[word.sentenceIndex]);
                        break;
                    case "neverLearn":

                        this.resp.known_words.push(word.word);
                    break;
                }
            }
            let API = useAPIStore();
            API.setState(this.resp);
            router.push({name: "FinalPage"});
        }
    }
}
</script>

<template>
    <div class="main-container">
        <h1>Выделение слов <span class="question-mark" @mouseover="isVisiable = true" @mouseleave="isVisiable = false">?
            <span v-if="isVisiable" class="user-hint">Кликни по слову чтобы задать ему статус:<br><span style="background-color: #71c686;">Зеленые:</span>
            неизвестные слова, которые ты хочешь учить<br>
                <span style="background-color: #B74747;">Красные:</span> слова, которые ты не хочешь учить</span>
            </span>
        </h1>
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
</template>

<style scoped>
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
    }
    h1{
        flex: 0 0 auto;
        font-size: 30px;
        position: relative;
    }
    .button-container{
        flex: 0 0 auto;
        min-height: 13%;
        /* height: 50%; */
    }
    .start-generation{
        height: 70%;
    }
    .text-area {
        scrollbar-width: thin;
        scrollbar-color: #888 var(--color-background);
        
    }
    .question-mark{
        border: #888 solid;
        border-radius: 24px;
        display: inline-block;
        width: 28px;
        height: 28px;
        text-align: center;
        position: absolute;
        top: 5px;
        right: -42px;
        font-size: 22px;
    }

    .user-hint{
        content: attr(data-text);
        min-width: 400px;
        z-index: 1;
        background-color: var(--color-background);
        position: absolute;
        border-radius: 10px;
        border: white solid;
        border-width: 1px;
        top: 35px;
        font-size: 18px;
        font-weight: 400;
        left: 30px;
    }

</style>