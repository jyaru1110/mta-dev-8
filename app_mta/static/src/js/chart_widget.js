/** @odoo-module **/
import AbstractField from 'web.AbstractField';
import fieldRegistry from 'web.field_registry';
var ChartWidget = AbstractField.extend({
    template: "ChartWidget",
    start: function(){
        this._super.apply(this, arguments);
        if (this.recordData[this.nodeOptions.currentValue]){
            this.value = this.recordData[this.nodeOptions.currentValue]
        }
    },
    _render: function() {
        var self = this;
        var value = this.value;
        console.log(value)
        var ajax = require('web.ajax');
        var result = [];
        var enlace = "/get_buffer_changes?product_id="+value.toString();
        ajax.jsonRpc(enlace, 'call', {}, {
            'async': false
        }).then(function (data) {
            result.push(data);
            result.foreach(element=>{
                console.log(element)
            })
        });
        var canvas = this.$('.canvas')[0]
        var ctx = canvas.getContext("2d");
        const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Oranges'],
        datasets: [{
            fill:true,
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor:'rgba(78,115,223,0.4)',
            borderColor:'rgba(78, 115, 223, 1)',
            tension: 0.1
            //borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
        
    },
})
fieldRegistry.add('chart_widget', ChartWidget);