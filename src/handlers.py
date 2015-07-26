import tornado.escape
import tornado.web

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
            response["status"] = "in queue"
            print payload
            self.perform_service(payload=response)
            self.write(tornado.escape.json_encode(response))
        else:
            self.set_status(400, reason="Bad request")
            self.write(tornado.escape.json_encode(form.errors))


class CallHandler(BaseHandler):
    form_class = CallForm

    def perform_service(self, payload, *args, **kwargs):
        """
            Do stuff here.
        """
        print "Make a Call"


class SMSHandler(BaseHandler):
    form_class = SMSForm

    def perform_service(self, payload, *args, **kwargs):
        """
            Do stuff here.
        """
        print "Send SMS"
