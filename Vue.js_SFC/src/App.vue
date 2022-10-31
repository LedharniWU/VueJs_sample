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
            users: [
                {
                    id: 1,
                    name: '鈴木太郎',
                    email: 'suzukitaro@example.com'
                },
                {
                    id: 2,
                    name: '佐藤二郎',
                    email: 'satoujiro@example.com'
                },
                {
                    id: 3,
                    name: '田中三郎',
                    email: 'tanakasaburo@example.com'
                },
                {
                    id: 4,
                    name: '山本四郎',
                    email: 'yamamotoshiro@example.com'
                },
                {
                    id: 5,
                    name: '高橋五郎',
                    email: 'takahashigoro@example.com'
                },
            ]
        };
    },
    methods: {
    },
    computed: {
        filteredUsers: function() {

            var users = [];

            for(var i in this.users) {

                var user = this.users[i];

                if(user.name.indexOf(this.keyword) !== -1 ||
                    user.email.indexOf(this.keyword) !== -1) {

                    users.push(user);

                }

            }

            return users;

        }
    }
}
</script>