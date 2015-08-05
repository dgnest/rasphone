# -*- coding: utf-8 -*-

import subprocess

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
        # /var/spool/asterisk/outgoing
        # tele1.call
        # Channel:  dongle/dongle0/984287311
        # Application: Playback
        # Data: mensaje1

        # /var/lib/asterisk/sounds/
        # Convert wav to gsm
        # sox originalfile.wav -r 8000 -c1 newfile.gsm

        return "Make a Call"


class SMSHandler(BaseHandler):
    form_class = SMSForm

    def perform_service(self, payload, *args, **kwargs):
        """
            Run command in order to send SMS to Asterisk's queue.
        """
        command = """
            asterisk -x 'dongle sms %(device)s %(cellphone)s %(message)s'
        """
        parsed_command = command % {
            "device": settings.DEVICE,
            "cellphone": payload.get("cellphone"),
            "message": payload.get("message"),
        }
        output, error = subprocess.Popen(
            parsed_command.encode('utf-8'),
            universal_newlines=True,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).communicate()
        return output or error
