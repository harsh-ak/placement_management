from odoo import fields, models,api,_
from datetime import date
from odoo.exceptions import ValidationError

class Recruiter(models.Model):
    _name = "recruiter.recruiter" #This will be the table name.
    _description = "This table stores the info of recruiters"
    _rec_name="company_name"


    name = fields.Char(string='HR Name')
    company_name=fields.Char(string="Company Name")
    location=fields.Char(string="Location")
    vacant_pos=fields.Many2many(comodel_name="position.position",string="Vacant Position/s")
    description=fields.Char(string="Job Description")
    work_type=fields.Selection([('work_from_home','Work From Home'),('work_from_office','Work From Office'),('Remote','Remote')])

    # @api.model
    # def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
    #     print ("\n\n Recruiter name>>>>>>", name)
    #     print ("\n\n Recruiter args>>>>>>", args)
    #     print ("\n\n Recruiter operator>>>>>>", operator)
    #     print ("\n\n Recruiter self>>>>>>", self)
    #     args = ['|', ('name', 'ilike', name), ('location', 'ilike', name)] + args
    #     print ("\n\n Recruiter args>>>>>>", args)
    #     result = self._search(args, limit=limit, access_rights_uid=name_get_uid)
    #     print ("\n\n Recruiter result>>>>>>", result)
    #     return result
    

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{} - {}".format(record.company_name, record.location)))
        return result


    