# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 S&C (<http://salazarcarlos.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from openerp import api, fields, models, _


import logging
_logger = logging.getLogger(__name__)


class stock_guia(models.Model):
    _name ='stock.guia'

    name = fields.Char(string='Nombre')
    sequence_id = fields.Many2one('ir.sequence', string="Secuencia")
    warehouse_id = fields.Many2one('stock.warehouse', string="Almacen")


class stock_picking(models.Model):
    _inherit = 'stock.picking'

    name_default = fields.Char(string='Nombre original')
    guia_id = fields.Many2one('stock.guia', string="Guia remision")
    count_item = fields.Float(string="Nro. items", compute='_count_all')
    count_product = fields.Float(string="Total Productos", compute='_count_all') 
    
    @api.model
    def create(self, vals):        
        res = super(stock_picking, self).create(vals)
        res.name_default = res.name
        return res    

    @api.multi
    def do_new_transfer(self):
        if self.guia_id:            
            name_guia = self.env['ir.sequence'].get_id(self.guia_id.sequence_id.id)  
            #_logger.error("PICKING NAME: %r", name_guia)         
            self._cr.execute("UPDATE stock_picking SET name=%s WHERE id=%s",(name_guia, self.id) )                
        return super(stock_picking, self).do_new_transfer() 
   
    @api.one
    def _count_all(self):
        self.count_item = sum(1 for line in self.move_lines)
        self.count_product = sum(line.product_uom_qty for line in self.move_lines)
        