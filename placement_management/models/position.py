from odoo import fields, models,api,_
from datetime import date
from odoo.exceptions import ValidationError

class Position(models.Model):
    _name = "position.position" #This will be the table name.
    _description = "This table stores the info of All Positions"


    name=fields.Char(string="Enter Positions")