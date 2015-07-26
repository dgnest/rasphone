from tornado.web import url
from handlers import CallHandler, SMSHandler


urlpatterns = [
    url(r"/call/", CallHandler),
    url(r"/sms/", SMSHandler),
]
