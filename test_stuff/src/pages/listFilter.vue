<script>
import Basebutton from '@/components/Basebutton.vue';
import { useAPIStore } from '@/stores/API';
import { useUserTextStoreV } from '@/stores/userTextV';
import { nextTick } from 'vue';
import router from '@/router';

export default {
    data() {    
        return {
            isVisible: false,
            cardNumStart: 1,
            cardNumTotal: 0,
            counter: 0,
            wordList: [],
            scrollerWidth: 0,
            cardWidth: 0,
            gap: 0,
            currentPage: 0,
            maxPage: 0,
            direction: null, // 0 - next page for translation, 1 - previous page for translation
            resp: {
                unknown_words: [],
                known_words: [],
                count: 0
            },
        }
    },
    components: {
        Basebutton
    },
    methods: {
        translate() {
            let distance = (this.cardWidth+this.gap)*4;
            switch (this.direction) {
                case 0:
                    this.$refs.scroller.style.transform = `translateX(-${(this.currentPage)*distance}px)`;
                    break;
                case 1:
                    this.$refs.scroller.style.transform = `translateX(-${(this.currentPage-1)*distance}px)`;
                    break;
                
            }
        },
        moveForward(){
            this.direction = 0;
            if (this.currentPage < this.maxPage-1){
                this.currentPage++;
                this.translate();
            }
        },
        moveBack(){
            this.direction = 1;
            if (this.currentPage > 0){
                this.translate();
                this.currentPage--;
            }
        },
        updateSizes(){
            if (!this.$refs.card[0] || !this.$refs.scroller || this.$refs.card[0].length === 0)
                return;
            this.gap = parseFloat(window.getComputedStyle(this.$refs.scroller).gap);
            this.cardWidth = this.$refs.card[0].offsetWidth;
            this.scrollerWidth = this.$refs.scroller.offsetWidth;
            let cardNum = this.wordList.length;
            // this.maxPage = Math.floor((this.cardWidth*cardNum+(cardNum-1)*this.gap) / ((this.cardWidth+this.gap)*4))
            this.maxPage = Math.ceil(this.wordList.length/4)
            
        },
        changeClass(index){
            let classes = ["wantLearn", "dontWantLearn", "default"];
            let word = this.wordList[index];
            let classNum = classes.indexOf(word.class);
            let nextClass = classes[(classNum+1)%3];
            word.class = nextClass;
        },
        validateWords() {
            let wordArr = useUserTextStoreV().words;
            this.wordList = wordArr.map((word) => {
                let regex = /[a-zA-Z'`’-]+/;
                let newWord = regex.exec(word);
                if (newWord != null) {
                    return {
                    word: newWord[0],
                    class: "default"
                    }
                }else {
                    return {
                        word: "BAD WORD",
                        class: ""
                    }
                }
            })
        },
        handleKeyDown(event){
            if (event.key === "ArrowRight") {
            this.moveForward();
            } else if (event.key === "ArrowLeft") {
            this.moveBack();
            }
        },
        startGen() {
            for (let word of this.wordList) {
                switch (word.class) {
                    case "wantLearn":
                        this.resp.unknown_words.push(word.word);
                        break;
                    case "dontWantLearn":
                        this.resp.known_words.push(word.word);
                        break;
                }
            }
            let API = useAPIStore();
            API.setState(this.resp);
            router.push({name: "FinalPage"});
        },
        goBack() {
            router.push({ name: "Filter" });
        }
    },
    mounted() {
        this.validateWords();
        this.$nextTick(() => this.updateSizes());
        window.addEventListener("resize", this.updateSizes);
        window.addEventListener("keydown", this.handleKeyDown)
    },
    unmounted(){
        window.removeEventListener('resize', this.updateSizes);
        window.removeEventListener('keydown', this.handleKeyDown);
    },
}
</script>

<template>
    <header>
        <h2 @click="goBack"><-- Вернуться к фильтрам</h2>
    </header>
    <div class="main-container">
        <div class="heading-row">
            <div class="heading-group">
                <div class="heading-text">Выбор слов из текста</div>
                <span class="question-mark" @mouseover="isVisible=true" @mouseleave="isVisible=false">?
                    <span v-if="isVisible" class="user-hint">Кликни по карточке со словом, чтобы задать ей статус:<br>
                        <span style="background-color: #71c686;">Зеленые карточки</span> – неизвестные слова<br>
                        <span style="background-color: #B74747;">Красные карточки</span> – слова, которые ты не хочешь учить
                    </span>
                </span>
            </div>
        </div>
        <div class="nested-container">
            <span class="card-number">Слова {{cardNumStart}}-{{cardNumStart+4}} из {{cardNumTotal}}</span>
            <div class="card-container">
                <div class="scroller" ref="scroller">
                    <div ref="card"
                        @click="changeClass(index)" 
                        v-for="word, index in wordList" 
                        :key="index" 
                        :class="['card', word.class]">
                        {{word.word}}
                    </div>
                </div>
            </div>
            <hr>
            <div class="bottom-contaiter">
                <div class="arrow-icons">
                    <img src="/left.png" alt="Left" class="arrow-icon" @click="moveBack" /> 
                     <img src="/right.png" alt="Right" class="arrow-icon" @click="moveForward" /> 
                </div>
                <span class="card-picked">Выбрано слов {{counter}} из {{cardNumTotal}}</span>
            </div>
            <div class="generation-container">
                <Basebutton class="start-generation" @click="startGen"> Начать генерацию </Basebutton> 
            </div>
        </div>
    </div>
</template>

<style scoped>
header {
        font-family: "Inter", sans-serif;
    }
    .main-container{
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 100%;
        margin: 0 px;
        font-family: "Roboto", sans-serif;
        font-optical-sizing: auto;
        font-weight: 300;
        font-style: normal;
        color: white;
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
        gap: 12px;
    }
    .heading-text {
        font-family: "Roboto", sans-serif;
        font-optical-sizing: auto;
        font-weight: 400;
        font-style: normal;
        font-variation-settings: "wdth" 100;
        text-align: center;
        font-size: 32px;
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
    hr {
        border: 1px solid white;
        width: 100%;
        margin: 20px 0 20px 0;
    }
    .user-hint {
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translateX(-50%);
        min-width: 400px;
        z-index: 10;
        background-color: var(--color-background);
        border-radius: 10px;
        border: 1px solid white;
        padding: 10px;
        font-size: 18px;
        margin-top: 0;
        margin-left:350px;
    }
    .nested-container{
        display: flex;
        align-content: start;
        flex-direction: column;
        width: 932px;
    }
    .card-container{
        display: flex;
        width:932px;
        flex: 0 0 auto;
        overflow: hidden;
        /* transition: ; */

    }
    .card-number{
        font-size: 20px;
        margin-bottom:10px;
    }
    .card{
        height: 260px;
        width: 214px;
        box-sizing: border-box;
        border-radius: 28px;
        border: 2px solid #fff;
        font-size: 30px;
        flex-shrink: 0;
        margin: 0 auto;
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 80px;
        min-width: 120px;
        font-size: 35px;
        text-align: center;
    }
    .scroller{
        display: flex;
        gap: 25px;
        flex-wrap:nowrap;
        width: 100%;
        transition: transform 0.5s cubic-bezier(0.255, 0.765, 0.575, 0.925);

    }
    .wantLearn{
        border-color: #71c686;
    }
    .dontWantLearn{
        border-color: #B74747;
    }
    .default{
        border-color: inherit;
    }
    .router-buttons-container{
        display: flex;   
        padding-top: 30px;
        justify-content: space-around;
    }
    .card-picked{
        flex-shrink: 0;
    }
    .router-button{
        width: 240px;
        height: auto;
    }
    .start-generation{
        width: 255px;
        height: 60px;
        border-radius: 0%;
    }
    .generation-container{
        display: flex;
        justify-content: center;
        padding-top: 40px;
    }
    .bottom-contaiter {
        position: relative;
        min-height: 60px;
    }
    .arrow-icons {
        position: absolute;
        top: 0;
        right: 0;
        display: flex;
        gap: 8px;
        z-index: 2;
    }
    .arrow-icon {
        width: 32px;
        height: 32px;
        cursor: pointer;
        filter: brightness(0.85 ) grayscale(0.2);
        transition: filter 0.15s;
    }
    .arrow-icon:hover {
        filter: brightness(1) grayscale(0);                                                                             
    }
</style>