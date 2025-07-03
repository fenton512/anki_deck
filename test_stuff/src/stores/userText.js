//This file represents the store for data.
//It is used to transfer user text from textarea between input.vue and filterFromText.vue

import { defineStore } from "pinia";

export const useUserTextStore = defineStore('userText', {
    state: () => ({
        words: [],
        yesLearn: [],
        noLearn: [],
        countLearn: 0,
        known: []
    }),
    actions: {
        setText(text) {
            this.words = text;
        },
        setYes(yes) {
            this.yesLearn = yes;
        },
        setNo(no) {
            this.noLearn = no;
        },
        setCount(count) {
            this.countLearn = count;
        },
        setKnown(known) {
            this.known = known;
        },
        resetStore() {
            this.words = [];
            this.yesLearn = [];
            this.noLearn = [];
            this.countLearn = 0;
            this.known = [];
        },
        startAgain() {
            this.yesLearn = [];
            this.noLearn = [];
            this.known = [];
        }
    },
    persist: {
        enabled: true,
        strategies: [
            {
                key: "userText",
                storage: sessionStorage,
                paths: ['words', 'yesLearn', 'noLearn', 'known']
            }
        ]
    }
});