//Expressのモジュールを取り込んで生成
const express = require('express')
const path = require('path')
const app = express()

//サーバーを起動
app.listen(3000, () => {
    console.log('sucsess!!')
})

//publicディレクトリ以下は自動で返す
app.use(express.static(path.join(__dirname, 'public')))
//トップへのアクセスを/publicへ流す
app.get('/', (req, res) => {
    res.redirect(302, '/public')
})