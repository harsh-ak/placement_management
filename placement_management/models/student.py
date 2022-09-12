from odoo import fields, models,api,_
from datetime import date
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = "student.student" #This will be the table name.
    _description = "This table stores the info of students"

    name = fields.Char(string='Name')
    phone_no=fields.Integer(string="Phone Number",size=10)
    email=fields.Char(string="Email Id")
    dob=fields.Date(string="Date of Birth")
    age=fields.Integer(string="Age")
    cv=fields.Binary(string="Upload CV",attachment=True)
    college=fields.Char(string="Your College")
    degree=fields.Char(string="Current Degree")
    student_type=fields.Selection([('Fresher','Fresher'),('Experienced','Experienced')],string="Are you?",default="Fresher")





    @api.constrains('cv')
    def _check_file(self):
       if str(self.file_name.split(".")[1]) != 'pdf' :
            raise ValidationError("Cannot upload file different from .pdf file")