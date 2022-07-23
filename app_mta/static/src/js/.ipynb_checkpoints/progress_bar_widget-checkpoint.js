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
            this.$('.background').text(value);
            //this.$('.background').css('padding','50% 100%');
            bandera_alerta = true;
        }
        
        /*var value = this.value.toString();
        if(value.length == 4){
            this.$('.background').css('padding','10% 33%');
        }else{
            if(value.length == 5){
                this.$('.background').css('padding','10% 30%');
            }else{
                if(value.length==3){
                    this.$('.background').css('padding','10% 34.6%');
                }else{
                    if(value.length==2 && !bandera_alerta){
                        this.$('.background').css('padding','10% 38%');
                    }else{
                        if(value.length==6){
                            this.$('.background').css('padding','10% 27%');
                        }
                    }
                }
            }
        }*/
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