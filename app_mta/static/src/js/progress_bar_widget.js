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
        console.log(value)
        this.$('.background').text(value);
        if(value<=33 || value=='dv'){
            this.$('.background').css('background-color','green');
        }else{
            if(value<=66){
                this.$('.background').css('background-color','yellow');
            }else{
                if(value=='dr'){
                    this.$('.background').css('background-color','red');
                }
                this.$('.background').css('background-color','red');
            }
        }
    },
})
fieldRegistry.add('progress_bar_widget', ProgressBarWidget);