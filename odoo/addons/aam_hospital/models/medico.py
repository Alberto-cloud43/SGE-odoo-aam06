from odoo import models, fields, api
class Medico(models.Model):
    _name = 'aam_hospital.medico'
    _description = 'Medico del Hospital'

    numero_colegiado = fields.Integer('Numero de colegiado', required=True)
    nombre_medico = fields.Char('Nombre', required=True)
    apellido_medico_1 = fields.Char('Primer apellido', required=True)
    apellido_medico_2 = fields.Char('Segundo apellido', required=True)
    email = fields.Char('Email', required=True)
    telefono = fields.Char('Telefono', required=True)
    imagen=fields.Image('Fotografia del medico')
    departamento_id = fields.Many2one('aam_hospital.departamento', 'Departamento', required=True)
    _sql_constraints = [
        ('numero_colegiado_unique', 'unique(numero_colegiado)', 'El numero de colegiado debe ser unico.'),
        ('email_unique', 'unique(email)', 'El email debe ser unico.'),
        ('telefono_unique', 'unique(telefono)', 'El telefono debe ser unico.'),
    ]


    