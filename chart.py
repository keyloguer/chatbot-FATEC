from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

if __name__ == '__main__':
    agent = Agent("./rasa_core/domain.yml",
                  policies=[MemoizationPolicy(), KerasPolicy()])

    agent.visualize("./rasa_core/stories.md",
                    output_file="graph.png", max_history=5)
