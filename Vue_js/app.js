var items = [
    {
        name: '鉛筆',
        price: 300,
        quantity: 5
    },
    {
        name: 'ノート',
        price: 400,
        quantity: 0
    },
    {
        name: '消しゴム',
        price: 500,
        quantity: 0
    },
    {
        name: '玩具',
        price: 600,
        quantity: 0
    },
]

var vm = new Vue({
    el: '#app',
    data: {
        items: items
    },
    filters: {
        numberWithDelimiter: function (value) {
            if (!value) {
                return '0'
            }
            return value.toLocaleString();
        }
    },
    computed: {
        totalPrice: function() {
            return this.items.reduce(function (sum, item) {
                return sum + (item.price * item.quantity)
            }, 0)
        },
        totalPriceWithTax: function() {
            return Math.floor(this.totalPrice * 1.08)
        }
    }
})

window.vm = vm