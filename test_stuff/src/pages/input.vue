
<script> 
import BaseButton from '@/components/Basebutton.vue';
import router from '@/router';
export default {
    data() {
        return {
            resp: {
                login: 'uuu',
                encrypted_password: "17"
            }
        }
    },
    mounted() { 
    },
    components: {
        BaseButton
    },
    methods: {
        async fatchdata() {
                const response = await fetch("http://127.0.0.1:8000/user/post/", {
                    method: "POST",
                    headers: {
                        'Content-Type' : 'application/json'
                    },
                    body: JSON.stringify(this.resp)
                })
            const result = await response.json()
            console.log(result)
        }
    }
}
</script>

<template>
   <main>
        <div class = "header">Введите текст песни или книги</div>
        <div class = "form-container">
            <form>
                <textarea id = "text" placeholder="Например: To be, or not to be, that is the question. Whether..."></textarea>
            </form>
        </div>
        <BaseButton class = "submit" @click="fatchdata">Сгенерировать деку</BaseButton>
   </main>
</template>

<style scoped> 
    main {
        margin: 0 px;
        font-family: "Inter", sans-serif;
        font-optical-sizing: auto;
        font-weight: 300;
        font-style: normal;
        color: white;
        font-size: 17px;
    }
    .header {
        font-family: "Roboto", sans-serif;
        font-optical-sizing: auto;
        font-weight: 400;
        font-style: normal;
        font-variation-settings:      
        "wdth" 100;
        text-align: center;
        font-size: 32px;
    }
    .form-container {
        align-self: center;
        width: 600px;
        margin: 0 auto;
        margin-top:20px;
    }
    #text {
        background-color: transparent;
        border-radius: 10px;
        padding-top:0.5em;
        height: 150px;
        border: 1px solid whitesmoke;
        width: 100%;
        color: white;
        box-sizing: border-box;
        padding-left: 0.5em;
        font-size: 14px;
        resize: vertical;
    }
    #text::placeholder {
        text-align: left;
        color: white;
        opacity: 0.8;
    }
    #text:focus {
        outline: none;
        box-shadow: none;
    }
    .submit {
        align-self: center;
        width: 255px;
        height: 60px;
        border-radius: 0;
        border: 1px solid whitesmoke;
        margin: 0 auto; 
        margin-top: 300px;
        
    }
    
</style>