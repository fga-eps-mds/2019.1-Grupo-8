
from rasa_core_sdk import Action
import json
import requests


class ActionTest(Action):
    def name(self):
        return "action_test"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message('Pesquisando perguntas pesquisadas para você')
        except ValueError:
            dispatcher.utter_message(ValueError)
        x =  '{ "name":"John", "age":30, "city":"New York"}'
        y = json.loads(x)
        try:
            ##data = json.load(requests.get('https://ludum-duvidas.herokuapp.com/api/duvidas'))
            dispatcher.utter_message(y)
        except ValueError:
            dispatcher.utter_message(ValueError)
        return []

    
class ActionQuestion(Action):
    def name(self):
        return "action_question"

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_message('Pesquisando perguntas pesquisadas para você')
        except ValueError:
            dispatcher.utter_message(ValueError)
        x = {
            "nome": "Siqueira",
            "age": 21,
            "adjetivo": "Lindão"
            }
        y = json.dumps(x)
        try:
            ##data = json.load(requests.get('https://ludum-duvidas.herokuapp.com/api/duvidas'))
            dispatcher.utter_message(y)
        except ValueError:
            dispatcher.utter_message(ValueError)
        return []
