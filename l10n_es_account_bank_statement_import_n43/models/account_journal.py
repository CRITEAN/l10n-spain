# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    n43_date_type = fields.Selection(
        string='Date type for N43 Import',
        selection=[('fecha_valor', 'Value Date'),
                   ('fecha_oper', 'Operation Date')],
        default='fecha_valor',
    )
