<script>
import router from '@/router';

export default {
    props: {
        onClick: Function
    },
    methods: {
        goToGenerSet() {
            router.push({name: 'GenerSettings'});
        }
    }
}
</script>

<template>
    <button @click="onClick" class="base-Button">
        <span class="button-content">
            <slot />
        </span>
    </button>
</template>

<style scoped>
.base-Button {
    border: solid white;
    border-radius: 12px;
    border-width: 2px;
    height:135px;

    color: white;
    background: initial;
    
    padding: 0.8em 3%;
    aspect-ratio: 3.3/1;

    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: "Inter", sans-serif;
    font-optical-sizing: auto;
    font-weight: 300;
    font-style: normal;
    font-size: 15px;
}
.button-content {
  display: inline-block;
  text-align: center;
}
</style>