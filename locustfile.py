import random
from locust  import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    @task
    def home_page(self):
        self.client.get("https://www.flyview360.com/")

    # @task
    # def search_page(self):
    #     self.client.get("https://app.kerberus.tech/?command=store")

    @task
    def faqs_page(self):
        self.client.get("https://app.kerberus.tech/faqs")

    @task
    def tarifs_page(self):
        self.client.get("https://tickets.flyview360.com/fr-FR/liste-des-produits")

    @task
    def products_page(self):
        self.client.get("https://tickets.flyview360.com/fr-FR/produits?familles=1927637257800401148-1927637258670401160-2015439032220400009-2015439174970400017")
        self.client.get(
            "https://tickets.flyview360.com/fr-FR/produits?familles=1927637254720401100-1927637258670401160-2015439101740400013-2015439174970400017")

    @task
    def infos_page(self):
        self.client.get("https://www.flyview360.com/infos-pratiques/tarifs-et-horaires.html")
        self.client.get("https://www.flyview360.com/infos-pratiques/comment-venir.html")
        self.client.get("https://www.flyview360.com/infos-pratiques/questions-frequentes.html")

    # @task
    # def get_user(self):
    #     self.client.get("https://server.f80.fr:6800/api/getuser/Paul.dudule@gmail.com")


    #locust --host https://app.kerberus.tech --users 1000 --hatch-rate 10 --reset-stats --web-host localhost --web-port 8089
    def on_start(self):
        pass