from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.agent import Agent
#-----------------------------------------------------------------------------------------------

## Treinar NLU
def train_nlu(data, config_yml, modeldir):
    training_data = load_data(data)
    trainer = Trainer(config.load(config_yml))
    trainer.train(training_data)
    model_directory = trainer.persist(modeldir)

## Treinar Core
def train_core(domain, story, dialogue):
    fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
                          core_threshold=1,
                          nlu_threshold=0.7)
    agent = Agent(domain, policies=[MemoizationPolicy(max_history=3),fallback, KerasPolicy()])
    training_data = agent.load_data(story)
    agent.train(
        training_data,
        epochs=100,
        validation_split = 0.2)
    agent.persist(dialogue)

if __name__ == '__main__':
    ## Arquivos NLU
    data_file = './rasa_nlu/nlu.md'
    model_dir = './models/FateBOT/current/'
    config_yml = './rasa_nlu/config.yml'
    ## Arquivos Core
    domain_file = './rasa_core/domain.yml'
    stories_file = './rasa_core/stories.md'
    dialogue = 'models/current/dialogue'
	
    #train_nlu(data_file, config_yml, model_dir) 
    train_core(domain_file, stories_file, dialogue)