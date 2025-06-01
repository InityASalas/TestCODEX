from odoo import api, fields, models


class IncomingEmailRule(models.Model):
    _name = 'incoming.email.rule'
    _description = 'Incoming Email Rule'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    from_email = fields.Char(string='From Email')
    subject_contains = fields.Char(string='Subject Contains')
    model_id = fields.Many2one('ir.model', string='Target Model', required=True)
    priority = fields.Integer(default=5)
    create_user_id = fields.Many2one('res.users', string='Create as User')

    def apply_rule(self, message):
        """Check if the message matches this rule."""
        if self.from_email and self.from_email not in message.get('from', ''):
            return False
        if self.subject_contains and self.subject_contains not in message.get('subject', ''):
            return False
        return True

    def create_record_from_message(self, message):
        model = self.model_id.model
        vals = {
            'name': message.get('subject'),
            'email_from': message.get('from'),
            'body': message.get('body', ''),
        }
        self.env[model].with_user(self.create_user_id or self.env.user).create(vals)
        return True
