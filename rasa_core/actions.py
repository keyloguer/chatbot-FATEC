from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import logging

logger = logging.getLogger(__name__)

class ActionCheckServico(Action):
    def name(self):
        return "action_check_servico"

    def run(self, dispatcher, tracker, domain):
        setor = tracker.get_slot('setor')
        responses = {
            'atendimento':  'utter_servico_atendimento',
            'cursos':    'utter_servico_cursos',
            'coordenação':   'utter_servico_coordenacao',
            'onde fica':    'utter_servico_ondefica',
        }

        if setor != None:
            response = responses.get(setor,"utter_default")
            dispatcher.utter_template(response, tracker)
            return []
        else:
            dispatcher.utter_template("utter_default",tracker)

class ActionCheckCursos(Action):
    def name(self):
        return "action_check_cursos"

    def run(self, dispatcher, tracker, domain):
        area = tracker.get_slot('area')
        
        responses = {
            'gestão portuária':     'utter_GP',
            'gestão empresarial':  'utter_GE',
            'sistemas para internet':     'utter_SI',
            'análise e desenvolvimento de sistemas':  'utter_ADS',
            'logística': 'utter_LOG',
        }

        if area != None:
            response = responses.get(area,"utter_default")
            dispatcher.utter_template(response, tracker)
        else:
            dispatcher.utter_template("utter_default",tracker)

        return []