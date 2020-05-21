# Copyright 2020 Marcel Savegnago - Escodoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CalendarEvent(models.Model):

    _inherit = 'calendar.event'

    meeting_presenter_id = fields.Many2one('res.partner', string='Presenter', )
    meeting_facilitator_id = fields.Many2one('res.partner', string='Facilitator', )
    meeting_note_taker_id = fields.Many2one('res.partner', string='Note Taker', )
    meeting_timekeeper_id = fields.Many2one('res.partner', string='Timekeeper', )
    meeting_discussion = fields.Text(string='Discussion', )
    meeting_actions = fields.Text(string='Action Items', )
    meeting_conclusion = fields.Text(string='Conclusion', )
