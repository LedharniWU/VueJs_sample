<template>
    <div>
        <div class="drop_area" @dragenter="dragEnter" 
                               @dragleave="dragLeave" 
                               @dragover.prevent
                               @drop.prevent="dropFile"
                               :class="{enter: isEnter}">
            ファイルアップロード
        </div>
        <div>
            <ul class="flex">
                <li class="flex-col" v-for="(file,index) in files" :key="index" @click="deleteFile(index)">
                    <div style="position: relative;">
                        <span class="delete-mark">×</span>
                        <img class="file_icon" src="../../public/static/img/icon-file.png">
                    </div>
                    <span>{{ file.name }}</span>
                </li>
            </ul>
            <div v-show="files.length">
                <button class="button" @click="sendFile">送信</button>
            </div>
            <ul>
                <li v-for="(item, index) in info" :key="index">
                    {{ item }}
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'DragDrop',
    data() {
        return {
            isEnter: false,
            info: null,
            files: [],
            files_name: {name: ''},
        }
    },
    mounted () {
        axios.get('/files')
        .then(response => { this.info = response.data.files })
    },
    methods: {
        dragEnter() {
            this.isEnter = true;
        },
        dragLeave() {
            this.isEnter = false;
        },
        dragOver() {
            console.log('DragOver')
        },
        dropFile() {
            // ここはドロップダウンした処理
            this.files.push(...event.dataTransfer.files)
            this.isEnter = false;
        },
        deleteFile(index) {
            this.files.splice(index, 1)
        },
        sendFile() {
            this.files.forEach(file => {
                this.files_name = {...this.files_name, name: file.name}
                axios.post('/file', this.files_name)
                .then(response => {
                    console.log(response.data)
                }).catch(error => {
                    console.log(error)
                })
                this.getFiles()
            })
        },
        getFiles: function() {
            axios.get('/files')
            .then(response => { this.info = response.data.files })
        }
    }
}
</script>

<style>
    .drop_area {
        color: gray;
        font-weight: bold;
        font-size: 1.2em;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 500px;
        height: 300px;
        border: 5px solid gray;
        border-radius: 15px;
    }

    .enter {
        border: 10px dotted powderblue;
    }

    ul {
        margin: 0;
        padding: 0;
        list-style-type: none;
    }

    .flex {
        display: flex;
        align-items: center;
    }

    .flex-col {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 0.5em;
        font-size: 10px;
    }

    .delete-mark {
        position: absolute;
        top: -14px;
        right: -10px;
        font-size: 20px;
    }

    .button {
        padding: 0.5em 1.5em;
        background-color: #0070a7;
        color: white;
        font-size: 14px;
        font-weight: bold;
        border-radius: 5px;
        border-color: #0070a7;
    }
</style>