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
    <button @click="onClick">
        <slot />
    </button>
</template>