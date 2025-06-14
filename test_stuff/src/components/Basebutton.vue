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
        <slot />
    </button>
</template>

<style scoped>
.base-Button {
    border: solid white;
    border-radius: 12px;
    border-width: 2px;
    color: white;
    background: initial;
    padding: 0.8em 3% 0.8em 3%;
}
</style>