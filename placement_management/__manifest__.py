
{
    'name': 'Placement Management',
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': 'This is Placement Management System',
    'description': """
    This is Placement Management System.
    """,
    'sequence':-500,
    'depends': ['base'],
    'data': [
    'security/ir.model.access.csv',
    'views/applicant.xml',
    'views/recruiter.xml',
    'views/position.xml',
    ],
    'installable':True,
    'auto_install':False,
    'application':True,
    'license': 'LGPL-3',
}