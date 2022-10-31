<template>
<div>
    <input type="text" v-model="keyword">
    <table>
        <tr v-for="user in filteredUsers" :key="user.id">
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
    },
    computed: {
        filteredUsers: function() {
            var users = [];
            for(var i in this.users) {
                var user = this.users[i];
                if(user.name.indexOf(this.keyword) !== -1 ||
                    user.email.indexOf(this.keyword) !== -1) {
                        users.push(user)
                }
            }
            return users
        }
    }
}
</script>