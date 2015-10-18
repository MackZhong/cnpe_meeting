# -*- coding: utf-8 -*-

from openerp import models, fields, api

class cnpe_meeting_room(models.Model):
    _name = 'cnpe_meeting.room'

    name = fields.Char('Room Location')
    video = fileds.Boolean('Has Video')
    projector = fields.Boolean('Has Projector')
    volume = fields.Integer(string='Volume', default=10)
    image = fields.Binary('Image')
    video_meeting = fields.Char(string='Video Meeting Avalible', compute='_get_video_meeting')

    @api.one
    def set_video(self):
        self.video = True

    @api.one
    def remove_video(self):
        self.video = False

    @api.one
    def set_projector(self):
        self.projector = True

    @api.one
    def remove_projector(self):
        self.projector = False

    @api.one
    @depends('video', 'projector')
    def _get_video_meeting(self):
        return self.video and self.projector
