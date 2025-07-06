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
            valid: true,
            store: null,
            validatedText: '',
            textStore: null,
            // Sample data. Fetch from API the csv file and format it like this
            words: [
                [0, "made", "сделать", "she made a cake", "она сделала торт", "she made a cake"],
                [1, "run", "бегать", "he can run fast", "он может быстро бегать", "he can run fast"],
                [2, "see", "видеть", "I see the stars", "Я вижу звезды", "I see the stars"],
                [3, "eat", "есть", "They eat apples", "Они едят яблоки", "They eat apples"],
                [4, "read", "читать", "I read books", "Я читаю книги", "I read books"],
                [5, "write", "писать", "He writes letters", "Он пишет письма", "He writes letters"],
                [6, "go", "идти", "We go to school", "Мы идём в школу", "We go to school"],
                [7, "come", "приходить", "She comes home", "Она приходит домой", "She comes home"],
                [8, "drink", "пить", "I drink water", "Я пью воду", "I drink water"],
                [9, "sleep", "спать", "They sleep well", "Они хорошо спят", "They sleep well"],
                [10, "walk", "гулять", "We walk in the park", "Мы гуляем в парке", "We walk in the park"],
                [11, "talk", "разговаривать", "He talks a lot", "Он много разговаривает", "He talks a lot"],
                [12, "listen", "слушать", "She listens to music", "Она слушает музыку", "She listens to music"],
                [13, "watch", "смотреть", "I watch TV", "Я смотрю телевизор", "I watch TV"],
                [14, "play", "играть", "They play football", "Они играют в футбол", "They play football"],
                [15, "study", "учиться", "We study English", "Мы учим английский", "We study English"],
                [16, "buy", "покупать", "He buys bread", "Он покупает хлеб", "He buys bread"],
                [17, "sell", "продавать", "She sells flowers", "Она продаёт цветы", "She sells flowers"],
                [18, "open", "открывать", "I open the door", "Я открываю дверь", "I open the door"],
                [19, "close", "закрывать", "They close the window", "Они закрывают окно", "They close the window"],
                [20, "draw", "рисовать", "We draw pictures", "Мы рисуем картинки", "We draw pictures"],
                [21, "cook", "готовить", "She cooks dinner", "Она готовит ужин", "She cooks dinner"],
                [22, "drive", "водить", "He drives a car", "Он водит машину", "He drives a car"],
                [23, "ride", "ездить", "I ride a bike", "Я катаюсь на велосипеде", "I ride a bike"],
                [24, "swim", "плавать", "They swim in the pool", "Они плавают в бассейне", "They swim in the pool"],
                [25, "sing", "петь", "We sing songs", "Мы поём песни", "We sing songs"],
                [26, "dance", "танцевать", "She dances well", "Она хорошо танцует", "She dances well"],
                [27, "help", "помогать", "He helps his friend", "Он помогает своему другу", "He helps his friend"],
                [28, "find", "находить", "I find my keys", "Я нахожу свои ключи", "I find my keys"],
                [29, "lose", "терять", "They lose the game", "Они проигрывают игру", "They lose the game"],
                [30, "build", "строить", "We build a house", "Мы строим дом", "We build a house"],
                [31, "break", "ломать", "He breaks the glass", "Он разбивает стакан", "He breaks the glass"],
                [32, "fix", "чинить", "She fixes the car", "Она чинит машину", "She fixes the car"],
                [33, "teach", "учить", "I teach children", "Я учу детей", "I teach children"],
                [34, "learn", "изучать", "They learn new words", "Они изучают новые слова", "They learn new words"],
            ],
            currentPage: 1,
            pageSize: 20,
            copySuccess: false,
        }
    },
    mounted() { 
        //this variable represents store, you can use all its actions as methods
        this.textStore = useUserTextStore();
    },
    components: {
        BaseButton
    },
    computed: {
        paginatedWords() {
            const start = (this.currentPage - 1) * this.pageSize;
            return this.words.slice(start, start + this.pageSize);
        },
        totalPages() {
            return Math.ceil(this.words.length / this.pageSize);
        }
    },
    methods: {
        goToFilterText() {
            //using Store variable to set user text
            router.push({name: "Filter"});
        },
        goToFilter() {
                router.push({name: "FinalPage"})
        },
        goBack() {
            this.textStore.startAgain();
            router.push({name: "Tinder"})
        },
        nextPage() {
            if (this.currentPage < this.totalPages) this.currentPage++;
        },
        prevPage() {
            if (this.currentPage > 1) this.currentPage--;
        },
        goToPage(page) {
            if (page >= 1 && page <= this.totalPages) this.currentPage = page;
        },
        copyWordsToCSV() {
            const csv = this.words.map(row => row.join(';')).join('\n');
            navigator.clipboard.writeText(csv).then(() => {
                this.copySuccess = true;
                setTimeout(() => { this.copySuccess = false; }, 1500);
            });
        },
    },
    watch: {
        isDone(newIsDone) {

        }
    }
}
</script>

<template>
   <main>
    <div class="copy-csv-row">
      <button class="copy-csv-btn" @click="copyWordsToCSV">Скопировать как CSV</button>
      <span v-if="copySuccess" class="copy-success">Скопировано!</span>
    </div>
    <header>
        <h2 @click="goBack"><-- Вернуться к подбору слов</h2>
    </header>
        <div class = "header">Предварительный просмотр деки</div>
        <table class="word-table">
  <thead>
    <tr>
      <th>Индекс слова</th>
      <th>Слово на англ</th>
      <th>Слово на русском</th>
      <th>Предложение на англ</th>
      <th>Предложение на русском</th>
      <th>Исходное предложение</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="(word, idx) in paginatedWords" :key="word[0]">
      <td>{{ word[0] }}</td>
      <td>
        <input
          v-model="words[(currentPage-1)*pageSize+idx][1]"
          class="edit-input"
          type="text"
          :placeholder="'Слово на англ'"
        />
      </td>
      <td>{{ word[2] }}</td>
      <td>{{ word[3] }}</td>
      <td>{{ word[4] }}</td>
      <td>{{ word[5] }}</td>
    </tr>
  </tbody>
</table>
        <div class="pagination">    
          <button @click="prevPage" :disabled="currentPage === 1">Назад</button>
          <span>Страница {{ currentPage }} из {{ totalPages }}</span>
          <button @click="nextPage" :disabled="currentPage === totalPages">Вперёд</button>
        </div>
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
        scrollbar-width: thin;
        scrollbar-color: #888 var(--color-background);
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
    .word-table {
        width: 100%;
        border-collapse: collapse;
        margin: 30px 0;
        background: rgba(255,255,255,0.05);
        color: white;
        font-size: 16px;
    }
    .word-table th, .word-table td {
        border: 1px solid #fff;
        padding: 8px 12px;
        text-align: center;
    }
    .word-table th {
        background: rgba(255,255,255,0.15);
        font-weight: 500;
    }
    .word-table tr:nth-child(even) {
        background: rgba(255,255,255,0.07);
    }
    .edit-input {
        width: 100%;
        background: rgba(255,255,255,0.1);
        color: #fff;
        border: 1px solid #ccc;
        border-radius: 4px;
        padding: 4px 8px;
        font-size: 15px;
        box-sizing: border-box;
    }
    .edit-input:focus {
        outline: 1.5px solid #fff;
        background: rgba(255,255,255,0.2);
    }
    td input{
        text-align: center;
    }
    .pagination {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
        gap: 16px;
        font-size: 16px;
    }
    .pagination button {
        background: #222;
        color: #fff;
        border: 1px solid #fff;
        border-radius: 4px;
        padding: 6px 16px;
        font-size: 15px;
        cursor: pointer;
        transition: background 0.2s;
    }
    .pagination button:disabled {
        background: #555;
        color: #aaa;
        cursor: not-allowed;
    }
    .copy-csv-row {
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 18px;
        margin-top: 10px;
        justify-content: flex-end;
    }
    .copy-csv-btn {
        background: #222;
        color: #fff;
        border: 1px solid #fff;
        border-radius: 4px;
        padding: 6px 16px;
        font-size: 15px;
        cursor: pointer;
        transition: background 0.2s;
    }
    .copy-csv-btn:hover {
        background: #444;
    }
    .copy-success {
        color: #7fff7f;
        font-size: 15px;
        font-weight: 500;
    }
</style>