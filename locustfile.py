import logging
import random
from locust import HttpUser, task, between, SequentialTaskSet, tag

class Visitor(HttpUser):
    wait_time = between(5, 9)

    @task
    class Ticket_buy(SequentialTaskSet):
        @tag("homepage")
        @task
        def home_page(self):
            logging.info("Ouverture de la home")
            self.client.get("")

        @tag("infos")
        def infos_page(self):
            logging.info("Ouverture des pages d'informations")
            self.client.get("infos-pratiques/tarifs-et-horaires.html")
            self.client.get("infos-pratiques/comment-venir.html")
            self.client.get("infos-pratiques/questions-frequentes.html")

        @tag("tarifs")
        @task
        def tarifs_page(self):
            logging.info("Ouverture des pages de tarifs")
            self.client.get("liste-des-produits")

        @tag("product")
        @task
        def products_page(self):
            logging.info("Ouverture des pages produits")
            self.client.get(
                "fr-FR/produits?familles=1927637254720401100-1927637258670401160-2015439101740400013-2015439174970400017")
            self.client.get("https://tickets.flyview360.com/fr-FR/selection-date-et-seance")
            # self.client.post("https://tickets.flyview360.com/API/FZbgzKYmWp/SessionsGrid",{"day":"2020-07-25"})


    #locust --host / --users 2 --hatch-rate 1 --reset-stats --web-host localhost --web-port 8089
    def on_start(self):
        pass