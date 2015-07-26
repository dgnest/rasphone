import tornado.escape
import tornado.web

from forms import MessageForm


class BaseHandler(tornado.web.RequestHandler):

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

        form = MessageForm(**payload)
        if form.validate():
            response = {
                "message_id": form.message_id.data,
                "order": form.order.data,
                "type_message": form.type_message.data,
                "message": form.message.data,
                "cellphone": form.cellphone.data,
                "status": "in queue",
            }
            self.perform_service(payload=response)
            self.write(tornado.escape.json_encode(response))
        self.write(tornado.escape.json_encode(form.errors))


class CallHandler(BaseHandler):

    def perform_service(self, payload, *args, **kwargs):
        """
            Do stuff here.
        """
        print "Make a Call"


class SMSHandler(BaseHandler):

    def perform_service(self, payload, *args, **kwargs):
        """
            Do stuff here.
        """
        print "Send SMS"
