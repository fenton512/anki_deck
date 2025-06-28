//This file represents the store for data.
//It is used to transfer user text from textarea between input.vue and filterFromText.vue

import { defineStore } from "pinia";

export const useUserTextStore = defineStore('userText', {
    state: () => ({
        text: '',
        yesLearn: [],
        noLearn: [],
        countLearn: 0
    }),
    actions: {
        setText(text) {
            this.text = text;
        },
        setYes(yes) { this.yesLearn = yes; },
        setNo(no) { this.noLearn = no; },
        setCount(count) { this.countLearn = count; },
    }
});