from odoo import models, fields, api

class Paciente(models.Model):
    _name = 'aam_hospital.paciente'
    _description = 'Paciente de el Hospital'

    nip = fields.Char('Numero Identificacion', required=True, unique=True)
    nombre = fields.Char('Nombre del Paciente', required=True)
    apellido1 = fields.Char('Primer apellido', required=True)
    apellido2 = fields.Char('Segundo apellido',required=True)
    fecha_nacimiento = fields.Date('Fecha de Nacimiento',required=True)
    fecha_ingreso = fields.Datetime('Fecha de Ingreso', required=True, default=fields.Datetime.now)
    fecha_alta = fields.Date('Fecha de alta')
    genero = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ], string='Género', required=True)
    direccion = fields.Text('Direccion', required=True)
    ciudad = fields.Char('Ciudad', required=True)
    codigo_postal = fields.Char('Codigo Postal', required=True)
    telefono = fields.Char('Telefono ', required=True, unique=True)
    email = fields.Char('Email', required=True, unique=True)
    historial_medico = fields.Text('Historial Medico')
    movilidad = fields.Selection([
        ('reposo_absoluto', 'Reposo Absoluto'),
        ('con_ayuda', 'Con Ayuda'),
        ('libre', 'Libre'),
    ], string='Movilidad',required=True)
    alergias = fields.Text('Alergias del Paciente')
    aislamiento = fields.Selection([
        ('no', 'Sin Aislamiento'),
        ('contacto', 'Aislamiento por Contacto'),
        ('goteo', 'Aislamiento por Goteo'),
        ('aereo', 'Aislamiento por Aéreo'),
    ], string='Aislamiento')
    departamento_ids = fields.Many2many(
         'aam_hospital.departamento', 'paciente_departamento_rel', 
         'paciente_id', 'departamento_id', string='Departamentos' )
    id_habitacion = fields.Many2one('aam_hospital.habitacion', 'Habitacion Asignada')
    _sql_constraints = [
        ('nip_unique', 'unique(nip)', 'El NIP debe ser unico.'),
        ('telefono_unique', 'unique(telefono)', 'El telefono debe ser unico.'),
        ('email_unique', 'unique(email)', 'El email debe ser unico.'),
    ]


    
