odoo.define('pos_ticket_custom.sequence', function (require) {
"use strict";

function sequence_next(seq){
        var idict = {
            'year': moment().format('YYYY'),
            'month': moment().format('MM'),
            'day': moment().format('DD'),
            'y': moment().format('YY')
            //'doy': moment().format('%j'),
            //'woy': moment().format('%W'),
            //'weekday': moment().format('%w'),
            //'h24': moment().format('%H'),
            //'h12': moment().format('%I'),
            //'min': moment().format('%M'),
            //'sec': moment().format('%S'),
        }
        var format = function(s, dict){
            s = s || '';
            $.each(dict, function(k, v){
                s = s.replace('%('+k+')s', v)
            })
            return s;
        };
        function pad(n, width, z) {
            z = z || '0';
            n = n + '';
            return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
        }
        var number_actual = seq.number_next_actual - seq.number_increment;
        seq.number_next_actual += seq.number_increment;
        var next_number = number_actual + seq.number_increment
        //console.log('SIGUIENTE: ', seq.number_next_actual);
        return format(seq.prefix, idict) + pad(next_number, seq.padding) + format(seq.suffix, idict)
    }


var pos_model = require('point_of_sale.models');


pos_model.load_models({
    model: 'ir.sequence',
    fields: [],
    ids:    function(self){ return [self.config.pos_order_sequence_id[0]]; },
    loaded: function(self, sequence_obj){ 
    	self.sequence_order = sequence_obj[0];
    	//console.log('CARGA inicial: ', self.sequence_order);     	
    },
});

var PosModelSuper = pos_model.PosModel.prototype;
pos_model.PosModel = pos_model.PosModel.extend({
    initialize: function(session, attributes) {
    	this.sequence_order = null;
        return PosModelSuper.initialize.call(this,session,attributes);
    },	
    /* VALIDO PERO SE USA
 	load_server_data: function(){
 		var self = this;
        var loaded = PosModelSuper.load_server_data.apply(this,arguments); 
        //console.log(this.sequence_order);     
        return loaded;
        },
    */
    push_order: function(order, opts){
        opts = opts || {};
        var self = this;        
        if(order){
        	var name_custom = sequence_next(self.sequence_order)
            //console.log('NUMERO FINAL:', name_custom);
            order.name = name_custom;
            this.db.add_order(order.export_as_JSON());
        }
        
        var pushed = new $.Deferred();

        this.flush_mutex.exec(function(){
            var flushed = self._flush_orders(self.db.get_orders(), opts);

            flushed.always(function(ids){
                pushed.resolve();
            });
        });
        
        return pushed;
    },    
});

});
