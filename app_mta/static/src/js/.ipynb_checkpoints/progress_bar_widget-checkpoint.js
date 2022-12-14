/** @odoo-module **/
import AbstractField from 'web.AbstractField';
import fieldRegistry from 'web.field_registry';
var ProgressBarWidget = AbstractField.extend({
    template: "ProgressBarWidget",
    start: function(){
        this._super.apply(this, arguments);
        if (this.recordData[this.nodeOptions.currentValue]){
            this.value = this.recordData[this.nodeOptions.currentValue]
        }
    },
    _render: function() {
        var self = this;
        var bandera_alerta = false;
        var value = this.value;
        if(value!='DV' && value!='DR' && value!="N/A"){
            this.$('.background').text(value + "%");
        }else{
            if(value=='DV'){
                this.$('.background').text('Demasiado verde');
            }else if(value=='DR'){
                this.$('.background').text('Demasiado rojo');
            }else if(value=='N/A'){
                this.$('.background').text('Sin alerta');
            }
            bandera_alerta = true;
        }
        
        if(value<=33 || value=='DV'){
            this.$('.background').css('background-color','#35C855');
            
        }else{
            if(value<=66){
                this.$('.background').css('background-color','#EBC232');
                 
            }else{
                if(value=='DR' || value>66){
                    this.$('.background').css('background-color','#F14040');
                }else{
                    if(value=='N/A'){
                        this.$('.background').css('color','black');
                    }
                }
            }
        }
    },
})
fieldRegistry.add('progress_bar_widget', ProgressBarWidget);