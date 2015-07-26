# -*- coding: utf-8 -*-

import os

import tornado.escape
import tornado.web

from conf import settings

from forms import MessageForm, CallForm, SMSForm


class BaseHandler(tornado.web.RequestHandler):
    form_class = MessageForm

    def perform_service(self, payload, *args, **kwargs):
        """
            Do stuff here.
        """
        pass

    def post(self):
        try:
            payload = tornado.escape.json_decode(self.request.body)
        except:
            payload = {}
            for key, value in self.request.arguments.iteritems():
                payload[str(key)] = value[0]

        form = self.form_class(**payload)
        if form.validate():
            response = form.data
            status = self.perform_service(payload=response)
            response["status"] = status
            self.write(response)
        else:
            self.set_status(400, reason="Bad request")
            self.write(form.errors)


class CallHandler(BaseHandler):
    form_class = CallForm

    def perform_service(self, payload, *args, **kwargs):
        """
            Do stuff here.
        """
        return "Make a Call"


class SMSHandler(BaseHandler):
    form_class = SMSForm

    def perform_service(self, payload, *args, **kwargs):
        """
            Run command in order to send SMS to Asterisk's queue.
        """
        command = "asterisk -x 'dongle sms dongle0 %(cellphone)s %(message)s'"
        parsed_command = command % {
            "device": settings.DEVICE,
            "cellphone": payload.get("cellphone"),
            "message": payload.get("message"),
        }
        response = os.system(parsed_command.encode('utf-8'))
        return response
