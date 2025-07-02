import { defineStore } from "pinia";

export const useAPIStore = defineStore("API", {
    state: () => ({
        data: {
            unknown_words: [],
            known_words: [],
            count: 10
        }
    }),
    actions: {
        setState(object) {
            this.data = object
        }
    },
    persist: {
        enabled: true,
        storageies: [
            {
                key: "API",
                strorage: sessionStorage,
                paths: ['data']
            }
        ]
    }
})