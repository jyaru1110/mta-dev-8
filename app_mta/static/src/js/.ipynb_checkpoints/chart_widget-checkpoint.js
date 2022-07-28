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
        var timeFormat = 'DD/MM/YYYY';
        var data_v =[];
        var data_a =[];
        var data_r = [];
        var data_q = [];
        //var data_completa = [];
        var canvas = this.$('.canvas')[0]
        var ctx = canvas.getContext("2d");
        var enlace = "/get_buffer_changes/"+value.toString();
        console.log('test con for en vez de forEach')
        ajax.jsonRpc(enlace, 'call', {}, {
            'async': false
        }).then(function (data) {
            //result.push(data);
            data.forEach(element=>{
                //console.log(typeof(element.create_date))
                //data_c.push({x:element.create_date,y:element.buffer_size})
                //labels.push(element.create_date);
                
                /*const date = new Date(element.create_date);
                console.log(date.toUTCString())
                console.log(date)*/
                
                if(element.type=='buffer'){
                    /*data_v.push({x:date.toUTCString(),y:element.buffer_size});
                    data_a.push({x:date.toUTCString(),y:2*element.buffer_size/3});
                    data_r.push({x:date.toUTCString(),y:element.buffer_size/3});*/
                    //const fecha = new Date(element.create_date);
                    
                    //console.log(fecha)
                    data_v.push({x:element.create_date,y:element.buffer_size});
                    data_a.push({x:element.create_date,y:2*element.buffer_size/3});
                    data_r.push({x:element.create_date,y:element.buffer_size/3});
                }else{
                    if(element.type=='available'){
                        data_q.push({x:element.create_date,y:element.qty_available})
                    }
                }
                
                
            })
            const tiempoTranscurrido = Date.now();
            const hoy = new Date(tiempoTranscurrido);
            console.log(hoy.toUTCString)
            //console.log(data[data.length-1])
            data_v.push({x:hoy.toUTCString(),y:data[data.length-1].buffer_size});
            data_a.push({x:hoy.toUTCString(),y:2*data[data.length-1].buffer_size/3});
            data_r.push({x:hoy.toUTCString(),y:data[data.length-1].buffer_size/3});
            data_q.push({x:hoy.toUTCString(),y:data[data.length-1].qty_available});
            const myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        //labels: labels,
                        datasets:[
                        {
                            //fill:true,
                            label:'Quantity On Hand',
                            data:data_q,
                            borderColor:'rgba(198,108,241,1)',
                            tension:0.1,
                        },
                        {
                            fill:true,
                            data:data_r,
                            stepped: true,
                            backgroundColor:'rgba(241,64,64,0.4)',
                            borderColor:'rgba(241,64,64,1)',
                        },
                        {
                            fill:true,
                            data:data_a,
                            stepped: true,
                            backgroundColor:'rgba(235,194,50,0.4)',
                            borderColor:'rgba(235,194,50,1)',
                        },
                        {
                            label:'Buffer size',
                            fill:true,
                            data:data_v,
                            stepped: true,
                            backgroundColor:'rgba(53,200,85,0.4)',
                            borderColor:'rgba(53,200,85,1)',
                        },
                        ]
                    },
                    options: {
                        scales: {
                            y: {
                                beginAtZero: true,
                            },
                            x: {
                                type: 'time',
                                time: {
                                    displayFormats: {
                                        quarter: 'MMM YYYY'
                                    },
                                },
                                title: {
                                    display: true,
                                    text: 'Fecha'
                                }
                            },
                            
                        },
                        plugins:{
                           legend: {
                                display: false
                           },
                            title: {
                                display: true,
                                text: 'Comportamiento historico del buffer'
                            },
                        },
                        tooltips: {
                            mode: 'nearest',
                            intersect: false
                        }
                    }
            });
        });
        //console.log(labels)
        //console.log(data_c)
        
        
    },
})
fieldRegistry.add('chart_widget', ChartWidget);