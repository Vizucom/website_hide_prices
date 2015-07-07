# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2015- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Website - Hide Prices',
    'category': 'Point of Sale',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['website_sale'],
    'description': """
Website - Hide Prices
=====================
 * Hides all prices from the website

""",
    #'qweb': [
    #    'static/src/xml/product_price.xml',
    #],
    'data': [
        'views/product_price.xml',
    ]
    
}
