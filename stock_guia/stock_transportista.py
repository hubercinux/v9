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


class stock_transportista(models.Model):
    _name = 'stock.transportista'

    name = fields.Char(string='Nombre')
    ruc = fields.Char(string='RUC', size=32)
    street_ids = fields.One2many('stock.transportista.street','transportista_id',string="Nueva direccion")
    conductor_ids = fields.One2many('stock.transportista.conductor','transportista_id',string="Nuevo conductor")
    movilidad_ids = fields.One2many('stock.transportista.movilidad','transportista_id',string="Nueva movilidad")
    active = fields.Boolean(default=True, string='Activo', help="Para no visualizar desactivarlo")
    
    _sql_constraints = [
        ('ruc_number_uniq', 'unique(ruc)', 'Numero de documento ya existe!')
        ]

class stock_transportista_street(models.Model):
    _name = 'stock.transportista.street'

    name = fields.Char(string='Direccion', size=64)
    state_id = fields.Many2one('res.country.state', string='Distrito', ondelete='cascade')
    transportista_id = fields.Many2one('stock.transportista', string='Empresa', ondelete='cascade')
    active = fields.Boolean( string = 'Activo', default=True, help="Para no visualizar desactivarlo")

    '''
    def fields_view_get(self, cr, uid, view_id=None, view_type=False, context=None, toolbar=False, submenu=False):
	    if view_type == 'form' and not view_id:
	        mod_obj = self.pool.get('ir.model.data')
	        #if self._name == "stock.picking.in":
	        model, view_id = mod_obj.get_object_reference(cr, uid, 'delivery_extension', 'view_stock_transportista_sede_form')
	        #if self._name == "stock.picking.out":
	        #    model, view_id = mod_obj.get_object_reference(cr, uid, 'stock', 'view_picking_out_form')
	    return super(stock_transportista_sede, self).fields_view_get(cr, uid, view_id=view_id, view_type=view_type, context=context, toolbar=toolbar, submenu=submenu)
	'''

class stock_transportista_conductor(models.Model):
    _name = 'stock.transportista.conductor'

    name = fields.Char(string='Apellidos y Nombres')
    licencia = fields.Char( string='Licencia', size=32)
    active = fields.Boolean( string='Activo', default=True, help="Para no visualizar desactivarlo")
    transportista_id = fields.Many2one('stock.transportista', string='Empresa', ondelete='cascade')

class stock_transportista_movilidad(models.Model):
    _name = 'stock.transportista.movilidad'

    name = fields.Char(string='Placa', size=64)
    marca = fields.Char(string='Marca', size=32)
    active = fields.Boolean(string='Active', default=True, help="Para no visualizar desactivarlo")
    transportista_id = fields.Many2one('stock.transportista', string='Empresa', ondelete='cascade')

class stock_picking(models.Model):
    _inherit = 'stock.picking'

    #Tramo 1
    transportista_id = fields.Many2one('stock.transportista', string='Empresa de transporte')
    conductor_id = fields.Many2one('stock.transportista.conductor', string='Conductor')
    movilidad_id = fields.Many2one('stock.transportista.movilidad', string=' Movilidad Placa/Marca' )
    partida_id = fields.Many2one('stock.transportista.street', string='Punto partida')
    #llegada_id = fields.Many2one('stock.transportista.street','Punto llegada sucursal', states={'done':[('readonly', True)], 'cancel':[('readonly',True)]}),
    llegadacliente_id = fields.Many2one('res.partner', string='Punto llegada')
	
	#Tramo 2 
    tramoii= fields.Boolean(string='Mostar tramo II') 
    transportista2_id = fields.Many2one('stock.transportista', string='Empresa de transporte')
    partida2_id = fields.Many2one('stock.transportista.street', string='Punto partida agencia')
    conductor2_id = fields.Many2one('stock.transportista.conductor', string='Conductor')
    movilidad2_id = fields.Many2one('stock.transportista.movilidad', string='Movilidad Placa/Marca')
    llegada2_id = fields.Many2one('stock.transportista.street', string='Punto llegada agencia')
    llegadacliente2_id = fields.Many2one('res.partner', string='Punto llegada cliente')

