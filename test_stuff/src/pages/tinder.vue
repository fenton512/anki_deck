<script> 
import BaseButton from '@/components/Basebutton.vue';
import router from '@/router';

export default {
    data() {
        return {
            countleft: 0,
            countadded: 0,
            words: ['aboba', 'skibidi', 'burmeowkoff', 'pure random', 'boba tee', 'nikolay shilov'],
            yesLearn: [],
            noLearn: [],
            currentIndex: 0,
            currentWord: '',
        }
    },
    mounted() { 
        this.initializeGame();
    },
    components: {
        BaseButton
    },
    methods: {
        initializeGame() {
            this.countleft = this.words.length;
            this.countadded = 0;
            this.currentIndex = 0;
            this.yesLearn = [];
            this.noLearn = [];
            this.updateCurrentWord();
        },
        updateCurrentWord() {
            if (this.currentIndex < this.words.length) {
                this.currentWord = this.words[this.currentIndex];
            } else {
                this.currentWord = '';
            }
        },
        likeWord() {
            if (this.currentIndex < this.words.length) {
                this.yesLearn.push(this.currentWord);
                this.countadded++;
                this.nextWord();
            }
        },
        dislikeWord() {
            if (this.currentIndex < this.words.length) {
                this.noLearn.push(this.currentWord);
                this.nextWord();
            }
        },
        nextWord() {
            this.currentIndex++;
            this.countleft = this.words.length - this.currentIndex;
            this.updateCurrentWord();
            
            if (this.currentIndex >= this.words.length) {
                this.finishGame();
            }
        },
        goBack() {
            if (this.currentIndex > 0) {
                this.currentIndex--;
                this.countleft = this.words.length - this.currentIndex;
                

                if (this.yesLearn.length > 0 && this.yesLearn[this.yesLearn.length - 1] === this.words[this.currentIndex]) {
                    this.yesLearn.pop();
                    this.countadded--;
                } else if (this.noLearn.length > 0 && this.noLearn[this.noLearn.length - 1] === this.words[this.currentIndex]) {
                    this.noLearn.pop();
                }
                
                this.updateCurrentWord();
            } else {
                router.push({name: 'Filter'});
            }
        },
        redirect() {
            router.push({name: 'FinalPage'});
        },
        goFilter() {
            router.push({name: "Filter"})
        }
    },
    watch: {
    }
}
</script>

<template>
   <main>
    <header>
        <h2 @click="goFilter"><-- Вернуться к фильтрам</h2>
    </header>
        <div class = "header">Тиндер слов</div>
        <div class = "card-container">
            <div class = "goBack" @click="goBack">
                Вернуться к предыдущему слову
            </div>
            <div class = "card" v-if="currentWord">
                <img class="corner-img" src="/star.png" alt="star">
                <div class="word">{{ currentWord }}</div>
                <div class = "button-container">
                    <button class = "like left" @click="dislikeWord"><img src="/dislike.png" alt="dislike"></button>
                    <button class = "like right" @click="likeWord"><img src="/like.png" alt="like"></button>
                </div>
            </div>
            <div class="game-finished" v-else>
                <h2>Все слова обработаны!</h2>
                <p>Слов добавлено в деку: {{ countadded }}</p>
                <p>Слов пропущено: {{ noLearn.length }}</p>
            </div>
            <div v-if ="currentWord">
              <h2>Слов осталось: {{ countleft }}</h2>
            <h2>Слов добавлено в деку: {{ countadded }}</h2>  
            </div>
            <div v-else>
                <BaseButton class = "submit" @click="redirect">Начать генерацию</BaseButton>
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
    .card-container h2{
        text-align: center;
        font-size: 20px;
        font-weight: 350;
    }
    .game-finished {
        width: 100%;
        height: 230px;
        border: 2px solid white;
        border-radius: 20px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .game-finished h2 {
        font-size: 28px;
        margin-bottom: 20px;
        font-weight: 400;
    }
    .game-finished p {
        font-size: 18px;
        margin: 5px 0;
        opacity: 0.9;
    }
    .submit {
        margin: 0 auto;
        margin-top: 3em;
        width: 255px;
        height: 60px;   
        border-radius: 0px;
        padding: 0;
    }
</style>