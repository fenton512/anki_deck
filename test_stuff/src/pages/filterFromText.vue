<script>
import { useUserTextStore } from '@/stores/userText';
export default {
    data() {
        return {
            text : "",
            textStore: null
        }
    },
    mounted() {
        this.textStore = useUserTextStore();
        //after rendering get data from store
        this.text = this.textStore.text;
    },
    methods: {
        validateWords() {
            let wordsArr = this.userText.trim().split(' ');
            this.userText = '';

            wordsArr.forEach((word) => {
                word = word.match(/^[a-zA-Z\d]*/);
                if (word != "") {
                    this.validatedText += `${word} `;
                }
            })

        },
    }
}
</script>

<template>
    <span>{{text}}</span>
</template>