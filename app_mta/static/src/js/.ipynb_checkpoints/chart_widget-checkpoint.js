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
        var ajax = require('web.ajax');
        var result = [];
        var labels = []
        var data_c =[]
        var canvas = this.$('.canvas')[0]
        var ctx = canvas.getContext("2d");
        var enlace = "/get_buffer_changes/"+value.toString();
        ajax.jsonRpc(enlace, 'call', {}, {
            'async': false
        }).then(function (data) {
            result.push(data);
            result[0].forEach(element=>{
                //console.log(typeof(element.create_date))
                //data_c.push({x:element.create_date,y:element.buffer_size})
                labels.push(element.create_date);
                data_c.push(element.buffer_size);
                
            })
            const myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [{
                            fill:true,
                            label: 'Buffer size',
                            data: data_c,
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
        });
        //console.log(labels)
        //console.log(data_c)
        
        
    },
})
fieldRegistry.add('chart_widget', ChartWidget);