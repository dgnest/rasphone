from __future__ import absolute_import

import requests

from conf import settings
from rasphone.celery import app


class PublicIP(object):
    api_url = settings.MASTER_HOST + "/api/publicip/"

    def __init__(self):
        credentials = {
            'username': settings.ADMIN_EMAIL,
            'password': settings.ADMIN_PASSWORD,
        }
        # Get the authentication token.
        self.token = requests.post(
            settings.MASTER_HOST + "/api-token-auth/",
            data=credentials,
        ).json().get("token")
        # Get the real public ip.
        response = requests.get("https://api.ipify.org?format=json").json()
        self.current_public_ip = response.get("ip")

    def update_public_ip(self):
        payload = {'public_ip': self.current_public_ip}
        headers = {'Authorization': "Token " + self.token}
        # Get the PublicIP object from the master.
        response = requests.get(self.api_url).json()
        result = response.get("results")
        if result:
            public_ip = result[0].get("public_ip")
            if public_ip != self.current_public_ip:
                object_id = result[0].get("id")
                response = requests.patch(
                    self.api_url + str(object_id) + "/",
                    data=payload,
                    headers=headers,
                )
                print(response.text)
            else:
                print("Nothing changed")
        else:
            response = requests.post(
                self.api_url,
                data=payload,
                headers=headers,
            )
            print(response.text)


@app.task(ignore_result=True, name='update-public-ip')
def update_public_ip():
    PublicIP().update_public_ip()
