from odoo import models, fields, api
from odoo.exceptions import ValidationError
class Habitacion(models.Model):
    _name = 'aam_hospital.habitacion'
    _description = 'Habitacion del Hospital'

    numero_habitacion = fields.Integer('Numero de habitacion', required=True, unique=True)
    tipo_habitacion = fields.Selection([
        ('individual', 'Individual'),
        ('doble', 'Doble'),
        ('suite', 'Suite'),
    ], 'Tipo de habitacion', required=True)
    planta = fields.Integer('Planta de la habitacion', required=True)
    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('ocupada', 'Ocupada'),
        ('mantenimiento', 'En mantenimiento'),
    ], 'Estado de la habitacion', default='disponible')
    _sql_constraints = [
        ('numero_habitacion_unique', 'unique(numero_habitacion)', 'El numero de habitacion debe ser unico.'),
    ]
    id_paciente = fields.One2many('aam_hospital.paciente', 'id_habitacion', string='Paciente asignado')
    @api.constrains('id_paciente', 'tipo_habitacion')
    def _check_max_pacientes(self):
        for hab in self:
            max_pacientes = 1 if hab.tipo_habitacion == 'individual' else 2

            if len(hab.id_paciente) > max_pacientes:
                raise ValidationError(
                    f"La habitación {hab.numero_habitacion} ({hab.tipo_habitacion}) "
                    f"solo permite {max_pacientes} paciente(s)."
                )
