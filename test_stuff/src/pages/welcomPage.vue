<script> 
import Basebutton from '@/components/Basebutton.vue';
import router from '@/router';
export default {
    components: {
        Basebutton
    },
    methods: {
        goToGenerSettings() {
            router.push({name: 'GenerSettings'});
        }
    }
}
</script>

<template>
    <h1>This is welcome page</h1>
    <Basebutton :onClick="goToGenerSettings"> Text for button</Basebutton>
</template>