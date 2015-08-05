import os


DEVICE = os.getenv("DEVICE", "dongle0")

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
MASTER_HOST = "http://" + os.getenv("MASTER_HOST")

UPDATE_IP_TIME = os.getenv("UPDATE_IP_TIME", 10)
