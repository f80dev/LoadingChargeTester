import random
from locust  import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def home_page(self):
        self.client.get("https://app.kerberus.tech")

    @task
    def search_page(self):
        self.client.get("https://app.kerberus.tech/?command=store")

    @task
    def faqs_page(self):
        self.client.get("https://app.kerberus.tech/faqs")

    @task
    def get_user(self):
        self.client.get("https://server.f80.fr:6800/api/getuser/Paul.dudule@gmail.com")


    #locust --host https://app.kerberus.tech --users 1000 --hatch-rate 10 --reset-stats --web-host localhost --web-port 8089
    def on_start(self):
        pass