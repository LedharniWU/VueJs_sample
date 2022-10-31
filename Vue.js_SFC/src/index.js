//vueモジュールからcreateAppメソッドを取り込み
import { createApp } from 'vue'
//作成したコンポーネントファイルを取り込み
import App from './App.vue'
import SelectFromApi from './selectFromApi.vue'
import Sample_select from './sample_select.vue'
import SelectAPiFromParameter from './selectAPiFromParameter.vue'

//Vue3のオブジェクトを生成
var app = createApp(App)
var selectFromApi = createApp(SelectFromApi)
var sample_select = createApp(Sample_select)
var selectAPiFromParameter = createApp(SelectAPiFromParameter)
//#appの中に組み込み
app.mount('#app')
selectFromApi.mount('#selectFromApi')
sample_select.mount('#sample_select')
selectAPiFromParameter.mount('#selectAPiFromParameter')