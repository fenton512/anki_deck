<script>
let id = 0;
export default {
    data() {
        return {
            onlyFiltered: false,
            newTodo: "",
            todoList: [
                {id: id++, text: "first task" , isdone: false},
                {id: id++, text: "second task", isdone: false},
                {id: id++, text: "third task", isdone: false}
            ]
        }
    },
    methods: {
        addTodo() {
            this.todoList.push({id: id++, text: this.newTodo});
            this.newTodo = "";
        },
        deleteTodo(todo) {
            this.todoList = this.todoList.filter(e => e != todo);
        }
    },
    computed: {
        filterTodo() {
            return this.onlyFiltered ?
            this.todoList.filter(e => !e.isdone) :
            this.todoList;
        }
    }
}
</script>
<template>
    <form @submit.prevent="addTodo">
        <input v-model="newTodo" required placeholder="Enter new task">
        <button>Add new task</button>
    </form>
    <ul>
        <li v-for="todo in filterTodo" :key="todo.id">
            <input type="checkbox" v-model="todo.isdone">
            <span :class="{done:todo.isdone}">{{todo.text}}</span>
            <button @click="deleteTodo(todo)">X</button>
        </li>
    </ul>
    <button @click="onlyFiltered = !onlyFiltered">{{onlyFiltered ? "Show all" : "Hide completed"}}</button>
</template>

<style>
.done {
    text-decoration: line-through;
}
</style>