from odoo import fields, models,api,_
from datetime import date
from odoo.exceptions import ValidationError

class Applicant(models.Model):
    _name = "applicants.applicants" #This will be the table name.
    _description = "This table stores the info of applicants"

    name = fields.Char(string='Name')
    phone_no=fields.Integer(string="Phone Number")
    email=fields.Char(string="Email Id")
    dob=fields.Date(string="Date of Birth")
    age=fields.Integer(string="Age",compute="_compute_age")
    cv=fields.Binary(string="Upload CV",attachment=True)
    college=fields.Char(string="College/University")
    degree=fields.Selection([('BscIT','BscIT'),
        ('MscIT','MscIT'),
        ('BCA','BCA'),
        ('MCA','MCA'),
        ('BE','BE'),
        ('ME','ME'),
        ('BTech','Btech'),
        ('MTech','MTech'),
        ('Other','Other')],string="Current Degree")
    applicants_type=fields.Selection([('Fresher','Fresher'),('Experienced','Experienced')],string="Are you?",default="Fresher")
    filename = fields.Char()
    applied_jobs_ids=fields.One2many(comodel_name="jobs.jobs",inverse_name="applicant_id")


    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            rec.age =0
            if rec.dob:
                birthDate = rec.dob
                today = date.today()
                age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
                rec.age = age





    @api.constrains('cv','filename')
    def _check_file(self):
       if str(self.filename.split(".")[1]) != 'pdf' :
            raise ValidationError("Cannot upload file different from .pdf file")



class AppliedJobs(models.Model):
    _name = "jobs.jobs" #This will be the table name.
    _description = "This table stores the info of Number of Jobs An Applicants has apllied"  

    applicant_id=fields.Many2one(comodel_name="applicants.applicants")
    company_id=fields.Many2one(comodel_name="recruiter.recruiter",string="Company Name")
    position_applied_ids=fields.Many2many(string="Position Applied",related="company_id.vacant_pos")
    position_applied_id=fields.Many2one(comodel_name="position.position",string="Position Applied") 


    # @api.onchange('company_id')
    # def cal_vacancy(self):
    #     for job_record in self:
    #         res=self.env['position.position'].search([('id','in',job_record.company_id.vacant_pos.ids)])
    #         for rec in res:
    #             print("_________",rec.name)
    #             self.position_applied_id=rec.id
            

            
    #         # print("__________________",res.vacant_pos.name)
    #         # print("____________________",self)
    #         # print("____________________",job_record)
    #         # print("______________________",job_record.position_applied_id)
    #         # print("______________________",job_record.company_id.vacant_pos)
    #         # for records in job_record.company_id.vacant_pos:
    #         #     print("___________________",records.name)
    #         #job_record.position_applied_id=job_record.company_id.vacant_pos



    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        # print("____________________________________Res",res)
        
        print("____________________aaaaaaaaa",args)
        # print("____________________bbbbbbbbb",rec.company_id.vacant_pos)

        # print("_____________________args",args)
        # print("_____________________self",self)

        # args += [(self.position_applied_id,'in',self.company_id.vacant_pos)]
        # print("_____________________args",args)

        return super(AppliedJobs, self)._search(args, offset, limit, order, count=count, access_rights_uid=access_rights_uid)