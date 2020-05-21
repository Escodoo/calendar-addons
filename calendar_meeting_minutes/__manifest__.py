# Copyright 2020 Escodoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Calendar Meeting Minutes',
    'summary': """
        This module enable report meeting minutes.""",
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Escodoo,Odoo Community Association (OCA)',
    'website': 'www.escodoo.com.br',
    'depends': [
        'calendar',
    ],
    'data': [
            'views/calendar_event_view.xml',
            'reports/calendar_event_meeting_minutes_report.xml',
    ],
    'demo': [
    ],
}
