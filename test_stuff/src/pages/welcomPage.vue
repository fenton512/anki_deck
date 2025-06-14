<script> 
import Basebutton from '@/components/Basebutton.vue';
import router from '@/router';
import ArrowWithHint from '@/components/ArrowWithHintLeft.vue';
export default {
    data() {
        return {
            style1: {
                position: "relative",
                top: "35%"
            },
            style2: {
                position: "relative",
                bottom: "17%"
            }
        }
    },
    components: {
        Basebutton,
        ArrowWithHint
    },
    methods: {
        goToGenerSettings() {
            router.push({name: 'GenerSettings'});
        },
        goToPasteText() {
            router.push({name: 'PasteText'});
        }
    }
}
</script>

<template>
    <div class="welcome-page">
        <h1>DANKO’s Anki Deck Generator</h1>
        <div class="mainContent">
            <ArrowWithHint :style="style2" :isMirrored="false" :right="20">идеально для начинающих</ArrowWithHint>
            <div class="button-conteiner">
                <Basebutton :onClick="goToGenerSettings" class="welcome-button"> Генерация на основе популярных слов</Basebutton>
                <Basebutton :onClick="goToPasteText" class="welcome-button">Генерация на основе текста песни / книги</Basebutton>
            </div>
            <ArrowWithHint :isMirrored="true" :style="style1" :right="-18" style="text-align: center;">подойдет тем, кто уже знаком с основами языка</ArrowWithHint>
        </div>
    </div>
</template>

<style scoped> 
.welcome-button {
    width: 35vw;
    max-height: fit-content;
    font-size: 1.5rem;
}
h1 {
    font-family: Krona One;
    font-size: 2.5rem;
    font-weight: 400;
    text-align: center;
    margin-top: 0%;
}
.mainContent {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    justify-items: center;
    padding-top: 1.5%;
    height: 100%;
}
.welcome-page {
    display: flex;
    flex-direction: column;
}
.button-conteiner {
    display: flex;
    flex-direction: column;
    gap: 3em 0%;
    min-height: fit-content;
}
</style>