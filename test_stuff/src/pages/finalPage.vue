<script>
import Basebutton from '@/components/Basebutton.vue';
import arrowSVG from '@/components/icons/buttonArrowFinalPage.vue';
import { useAPIStore } from '@/stores/API';
export default {
    components: {
        Basebutton,
        arrowSVG
    },
    data() {
        return {
            resp: null
        }
    },
    mounted() {
        this.resp = useAPIStore().data;
        console.log(this.resp);
    }
}
</script>
<template>
    <div class="main-container">
        <h1>Ваша колода готова</h1>
        <div class="button-flex">
            <Basebutton class="button-csv">
                <div class="inner-button-flex">
                    <arrowSVG class="arrow-icon"/>
                    <span>Скачать в формате .csv</span>
                </div>
            </Basebutton>
        </div>
        <Basebutton class="back-button">Вернуться в начало</Basebutton>
    </div>
</template>

<style scoped>
    .main-container {
        display: flex;
        align-items: center;
        flex-direction: column;
        height: 100%;
        gap: 5%;
    }
    .button-flex {
        height: 70%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        width: 100%;

        /* background-color: aqua; */
    }
    .button-csv {
        width: 30%;
        border-radius: 70px;
        border-color: var(--color-green);
    }
    .inner-button-flex {
        display: flex;
        align-items: center;
        justify-content: space-evenly;
        width: 100%;
        font-size: 2vw;
    }
    .back-button {
        margin-bottom: 3%;
        width: 17%;
        border-radius: 0%;
    }
    @media(min-width: 1280px) {
        h1 {
            font-size: 40px;
        }
    }
    .arrow-icon {
        width: 8%;
    }
</style>

