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
    'name' : 'Stock guia',
    'version' : '1.0',
    'author' : 'Ing. Salazar C. J.',
    'sumary' : 'Modulo para generar correlativos de guia',
    'description' : """
Personalizacion de Guias
========================

Este modulo permite:
-------------------

* Generar correlativos de guia por almacen
* Añade transportista a la guia
* Personaliza la impresioon de la guia
    """,
    'depends' : ['base', 'report','stock', ],
    'data' : [            
            'security/ir.model.access.csv',
    		'stock_guia.xml',
            'views/print_guia.xml',
    		'stock_transportista.xml',
    	],
    'installable' : True,
    'aplication' : True,
    
}