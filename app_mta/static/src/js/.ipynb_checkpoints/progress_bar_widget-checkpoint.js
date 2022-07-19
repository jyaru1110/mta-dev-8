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
        var value = this.value;
        this.$('.background').text(value);
        
        var value = this.value.toString();
        if(value.length == 4){
            this.$('.background').css('padding','10% 33%');
        }else{
            if(value.length == 5){
                this.$('.background').css('padding','10% 30%');
            }else{
                if(value.length==3){
                    this.$('.background').css('padding','10% 34.6%');
                }else{
                    if(value.length==2){
                        this.$('.background').css('padding','10% 38%');
                    }
                }
            }
        }
        
        if(value<=33 || value=='dv'){
            this.$('.background').css('background-color','#35C855');
            
        }else{
            if(value<=66){
                this.$('.background').css('background-color','#EBC232');
                 
            }else{
                if(value=='dr' || value>66){
                    this.$('.background').css('background-color','#F14040');
                }
            }
        }
    },
})
fieldRegistry.add('progress_bar_widget', ProgressBarWidget);