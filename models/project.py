from odoo import fields, models , osv , api

WEIGHT_TYPE_SELECTION = [
    ('a', 'Easy'),
    ('b', 'Intermediate'),
    ('c', 'Hard')
]

PRIORITY_TYPE_SELECTION = [
    ('0', 'High'),
    ('1', 'Medium'),
    ('2', 'Low')
]

STATUS_TYPE_SELECTION = [
    ('0', 'Opened'),
    ('1', 'Started'),
    ('2', 'Inprogress'),
    ('3', 'Done'),
    ('4', 'Hold'),
]

class TaskCustom(models.Model):
    _inherit = 'project.task'
    weight = fields.Selection(WEIGHT_TYPE_SELECTION, 'Weight')
    priority_list = fields.Selection(PRIORITY_TYPE_SELECTION, 'Priority')
    status_list = fields.Selection(STATUS_TYPE_SELECTION, 'Status')

    @api.multi
    def do_done(self):
        for task in self: 
            task.status_list = '2'
        return True 
