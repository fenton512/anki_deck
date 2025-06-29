import { defineStore } from "pinia";

export const useAPIStore = defineStore("API", {
    state: () => ({
        data: {
            wantLearn: [],
            dontWantLearn: [],
            count: 0
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