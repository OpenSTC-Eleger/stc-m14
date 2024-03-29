# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2008 JAILLET Simon - CrysaLEAD - www.crysalead.fr
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################
{
    "name" : "France - M14 Accounting",
    "version" : "1.1",
    "author" : "OpenERP SA",
    "website": "http://www.openerp.com",
    "category" : "Localization/Account Charts",
    "description": """
This is the module to manage the M14 accounting chart for Collectivities in France in OpenERP.
========================================================================
This module is an adaptation of l10n_fr module: 
* it replaces general chart of account with M14 chart of accounts
* it adds another taxe 20.6

This module applies to companies based in France mainland. It doesn't apply to companies based in the DOM-TOMs (Guadeloupe, Martinique, Guyane, Réunion, Mayotte, etc...)

This localisation module creates the VAT taxes of type "tax included" for purchases (it is notably required when you use the module "hr_expense"). Beware that these "tax included" VAT taxes are not managed by the fiscal positions provided by this module (because it is complex to manage both "tax excluded" and "tax included" scenarios in fiscal positions).

This localisation module doesn't properly handle the scenario when a France-mainland company sells services to a company based in the DOMs. We could manage it in the fiscal positions, but it would require to differentiate between "product" VAT taxes and "service" VAT taxes. We consider that it is too "heavy" to have this by default in l10n_fr ; companies that sell services to DOM-based companies should update the configuration of their taxes and fiscal positions manually.

Credits: Sistheo, Zeekom, CrysaLEAD, Akretion and Camptocamp.
""",
    "depends" : ['base_iban', 'account', 'account_chart', 'base_vat', 'l10n_fr_rib'],
    "init_xml" : [],
    "update_xml" : [
        "fr_report.xml",
        "fr_account_type_data.xml",
        #"plan_comptable_general.xml",
        "account.account.template.csv",
        "l10n_fr_wizard.xml",
        "fr_pcg_taxes.xml",
        "fr_tax.xml",
        "fr_fiscal_templates.xml",
        "security/ir.model.access.csv",
        "wizard/fr_report_bilan_view.xml",
        "wizard/fr_report_compute_resultant_view.xml",

    ],
    #"test": ['test/l10n_fr_report.yml'],
    "demo_xml" : [],
    "certificate" : "00435321693876313629",
    "auto_install": False,
    "installable": True,
    'images': ['images/config_chart_l10n_fr.jpeg','images/l10n_fr_chart.jpeg'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

