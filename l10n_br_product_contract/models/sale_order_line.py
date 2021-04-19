# Copyright 2021 KMEE - Luis Felipe Mileo <mileo@kmee.com.br>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    @api.multi
    def _prepare_contract_line_values(
        self, contract, predecessor_contract_line_id=False
    ):
        vals = self._prepare_br_fiscal_dict()
        vals.update(super()._prepare_contract_line_values(
            contract, predecessor_contract_line_id
        ))
        return vals
