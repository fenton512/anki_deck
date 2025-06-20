<script> 
import Basebutton from '@/components/Basebutton.vue';
import router from '@/router';
import ArrowWithHint from '@/components/ArrowWithHint.vue';

export default {
    data() {
        return {
            right: -18,
            secondRight: 20,
            isMobile: window.innerWidth <= 550,
        }
    },
    mounted() { 
        this.resizeHandler();
        window.addEventListener('resize', this.resizeHandler);
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
            router.push({name: 'Input'});
        },
        resizeHandler() {
            const query = window.matchMedia('(max-width: 550px)');
            this.isMobile = query.matches;
            if (this.isMobile) {
                this.right = 19;
                this.secondRight = -15;
                return false;
            }else {
                this.right = -18;
                this.secondRight = 20;
                return true;
            }
        }
    }
}
</script>

<template>
    <div class="welcome-page">
        <h1>DANKO’s </h1>
        <h1>Anki Deck Generator</h1>
        <div class="mainContent">
            <div class="grid-cell">
                <ArrowWithHint class="leftArrow" :isMirrored="isMobile" :right="secondRight" >идеально для начинающих</ArrowWithHint>
            </div>
            <div class="button-conteiner">
                <Basebutton :onClick="goToGenerSettings" class="welcome-button"> Генерация на основе популярных слов</Basebutton>
                <Basebutton :onClick="goToPasteText" class="welcome-button">Генерация на основе текста песни / книги</Basebutton>
            </div>
            <div class="grid-cell">
                <ArrowWithHint :isMirrored = "!isMobile"  class="rightArrow" :right="right" style="text-align: center;">подойдет тем, кто уже знаком с основами языка</ArrowWithHint>
            </div>
        </div>
        <div style="flex-grow: 1.5;"></div>
    </div>
</template>

<style scoped> 
.rightArrow, .leftArrow {
    /* background-color: grey; */
    aspect-ratio: 2.68/1;
    min-width: 100%;
    position: absolute;
}
.welcome-button {
    font-weight: 600;

}
h1 {
    font-family: Krona One;
    font-size: 48px;
    text-align: center;
    margin-top: 0%;
    margin-bottom: 0px;

}
.mainContent {
    flex-grow: 2;
    font-family: "Inter", sans-serif;
    font-optical-sizing: auto;
    font-weight: 550;
    font-style: normal;
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    justify-items: center;
    align-items: center;
    padding-top: 1.5%;
    height: 100%;
    width: 100%;
    position: relative;
}
.welcome-page {
    /* background-color: bisque; */
    display: flex;
    flex-direction: column;
    min-height: 100%;
    align-items: center;
}
.button-conteiner {
    display: flex;
    flex-direction: column;
    gap: 3em 0%;
    min-height: fit-content;
    align-items: center;
    width: 100%;
}
.grid-cell {
    position: relative;
    width: 100%;
    height: 100%;
}
@media (max-width: 550px) {
    h1 {
        font-size: 25px;
    }
    .welcome-button{
        font-size: 13px;
        width: 70%;
    }
    .mainContent {
        grid-template-columns: 1fr;
        grid-template-rows: 1fr 2fr 1fr;
    }
    .rightArrow {
        transform: rotate(319deg);
        font-size: 10px;
        width: 35%;
        min-width: min-content;
        left: 4%;
    }
    .leftArrow {
        transform: rotate(333deg);
        font-size: 10px;
        width: 35%;
        min-width: min-content; 
        left: 70%;
    }
}
@media (min-width: 551px) {
    h1 {
        font-size: 35px;
    }
    .welcome-button {
        width: 85%;
        font-size: 18px;
    }
    .rightArrow {
        top: 38%;
        left: -9%;
        font-size: 12px;
        width: 90%;
        min-width: min-content;
    }
    .leftArrow {
        top: 17%;
        left: 30%;
        font-size: 12px;
    }
}
@media (min-width: 800px) {
    h1 {
        font-size: 45px;
    }
    .welcome-button {
        width: 60%;
        font-size: 23px;
    }
    .rightArrow {
        top: 40%;
        left: -30%;
        font-size: 15px;
    }
    .leftArrow {
        top: 10%;
        left: 40%;
        font-size: 15px;
    }
}
@media (min-width: 1115px) {
    h1 {
        font-size: 45px;
    }
    .welcome-button {
        width: 60%;
        font-size: 2rem;
    }
    .rightArrow {
        top: 45%;
        left: -40%;
        font-size: 23px;
    }
    .leftArrow {
        top: 10%;
        left: 40%;
        font-size: 23px;
    }
}
</style>