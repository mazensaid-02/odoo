from odoo import models, fields

class TestModel(models.Model):
    _name = 'test.model'
    _description = 'Mon premier modèle'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
