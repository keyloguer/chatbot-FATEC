from rasa_nlu.model import Interpreter
import json

def recebeInput(frase):
    interpreter = Interpreter.load("models/FateBOT/current")
    message = frase
    result = interpreter.parse(message)
    print(json.dumps(result, indent=2))
frase = input('Digite o que quer testar: ')
recebeInput(frase)

