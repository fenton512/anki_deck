//This file represents the store for data.
//It is used to transfer user text from textarea between input.vue and filterFromText.vue

import { defineStore } from "pinia";

export const useUserTextStore = defineStore('userText', {
    state: () => ({
        text: '',
    }),
    actions: {
        setText(text) {
            this.text = text;
        }
    }
});