<template>
    <div>
        <input type="text" v-model="keyword">
        <table>
            <tr v-for="user in users" :key="user.id">
                <td v-text="user.id"></td>
                <td v-text="user.name"></td>
                <td v-text="user.email"></td>
            </tr>
        </table>
    </div>
</template>

<script>
export default { 
    data() {
        return {
            keyword: '',
            users: [],
        }
    },
    mounted() {
        axios.get('https://jsonplaceholder.typicode.com/users')
            .then(response => this.users = response.data)
            .catch(error => console.log(error))
    }
}

</script>