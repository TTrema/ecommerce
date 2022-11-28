import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "Ad5Qh5D4rkgbc5hycILs7t9OduwDJZn2czAtCi2o2xec7JD3ahhuEHRrK6uW6veDVTZEE-Vrzq5E3ct8"
        self.client_secret = "EBT2eJQaoza5Qwj9xJ-z4EgIWSAcKpG6ulHr-Ilje2c7ZMuWQSykaV8zlNMKk_LCsQcoKx9kAmBywcCL"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)