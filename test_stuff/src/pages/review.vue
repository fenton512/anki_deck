<script> 
import BaseButton from '@/components/Basebutton.vue';
import router from '@/router';

import { useUserTextStoreV } from '@/stores/userTextV';


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
            resp: [],
            currentPage: 1,
            pageSize: 20,
            copySuccess: false,
            csv: null,
            words: [], 
        }
    },
    mounted() { 
        //this variable represents store, you can use all its actions as methods
        this.textStore = useUserTextStoreV();
        this.resp = useAPIStore().data;
        this.button = this.$refs.buttonRef;
        this.fatchdata();
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
        async fatchdata() {
            try {
                const response = await fetch("http://127.0.0.1:8000/wordlist/post", {
                    method: "POST",
                    headers: {
                        'Content-Type' : 'application/json'
                    },
                    body: JSON.stringify(this.resp),
                });
                if (!response.ok) throw new Error(`Err: ${response.status}`)
                const blob = await response.blob();
                this.textStore.setCsv(blob);
                // Parse CSV from blob
                const text = await blob.text();
                this.words = text.trim().split('\n').map(line => line.split(';'));
                this.url = window.URL.createObjectURL(blob);
                this.isGetResp = true;
            
            } catch (err) {
                this.isErr = true;
                console.log(err);
            }
        },
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