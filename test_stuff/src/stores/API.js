import { defineStore } from "pinia";

export const useAPIStore = defineStore("API", {
    state: () => ({
        wantLearn: [],
        dontWantLearn: [],
        count: 0
    }),
    actions: {
        setState(object) {
            this.wantLearn = object.wantLearn;
            this.dontWantLearn = object.dontWantLearn;
            this.count = object.count;
        }
    }
})