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


{
    'name' : 'Invoice custom',
    'version' : '1.0',
    'author' : 'Ing. Javier Salazar Carlos',
    'sumary' : 'Modulo que extiende las funcionalidades del modulo de Contabilidad',
    'description' : """
Personalizacion del modulo de Contabilidad
====================================

Este modulo permite:
-------------------

* Buscar un cliente por RUC/DNI en el formulario de factura
* Imprimir las facturas personalizadas
    """,
    'depends' : ['sale_custom', 'report', 'l10n_pe_partner' ],
    'data' : [            
            'invoice.xml',
        ],
    'installable' : True,
    'aplication' : True,    
}