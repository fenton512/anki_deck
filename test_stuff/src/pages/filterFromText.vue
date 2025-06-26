<script>
import { useUserTextStore } from '@/stores/userText';
import Basebutton from '@/components/Basebutton.vue';
export default {
    data() {
        return {
            text: "",
            textStore: null,
            textArea: null,
            words: [],
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
            let wordsArr = this.text.trim().split(/\s/);
            this.words = wordsArr.map((word) => {
                let regex = /[a-zA-Z'`’\d]+/;
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
    }
}
</script>

<template>
    <div class="main-container">
        <h1>Выделение слов</h1>
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
            <Basebutton class="start-generation">Начать генерацию</Basebutton>
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
        flex-grow: 8;
    }
    .h1{
        flex-grow: 1;
    }
    .button-container{
        flex-grow: 1;
        /* height: 50%; */
    }
    .start-generation{
        height: 70%;
    }
</style>