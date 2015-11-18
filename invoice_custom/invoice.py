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
from openerp.exceptions import Warning

import logging
_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    ruc_dni =  fields.Char(string='RUC/DNI', size=32, )
    
    @api.onchange('ruc_dni')
    def onchange_ruc_dni(self):
        if self.ruc_dni:
            partner_id = self.env['res.partner'].search([('doc_number','=',self.ruc_dni)])
            if partner_id:
                self.partner_id = partner_id
            else:
                raise Warning('Cliente no registrado!, porfavor registrarlo en el sistema')      
        else:
            self.partner_id = False
            account_id = False
            payment_term_id = False
            fiscal_position = False
            bank_id = False

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        super(AccountInvoice, self)._onchange_partner_id()
        if not self.partner_id:
            self.ruc_dni = False
            return
        partner = self.env['res.partner'].browse(self.partner_id.id)
        self.ruc_dni = partner.doc_number
        #_logger.error("MI wwwww: %r", partner)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['ruc_dni'] = self.ruc_dni or False
        return invoice_vals