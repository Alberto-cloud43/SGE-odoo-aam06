from odoo import models, fields, api

class Departamento(models.Model):
    _name = 'aam_hospital.departamento'
    _description = 'Departamento del Hospital'

    id_departamento = fields.Integer('ID del departamento', required=True, unique=True)
    especialidad = fields.Char('Especialidad', required=True, unique=True)
    descripcion = fields.Text('Descripcion')
    telefono_guardia = fields.Char('Telefono de guardia',required=True, unique=True)
    numero_despacho = fields.Integer('Numero de despacho',required=True, unique=True)
    paciente_ids = fields.Many2many(
    'aam_hospital.paciente',
    'paciente_departamento_rel',
    'departamento_id',
    'paciente_id',
    string='Pacientes'
    )
    medico_ids = fields.One2many(
    'aam_hospital.medico',   
    'departamento_id',       
    string='Médicos'
)
    _rec_name = 'especialidad'
    _sql_constraints = [
        ('id_departamento_unique', 'unique(id_departamento)', 'El ID del departamento debe ser unico.'),
        ('especialidad_unique', 'unique(especialidad)', 'La especialidad debe ser unica.'),
        ('telefono_guardia_unique', 'unique(telefono_guardia)', 'El telefono de guardia debe ser unico.'),
        ('numero_despacho_unique', 'unique(numero_despacho)', 'El numero de despacho debe ser unico.'),
    ]

