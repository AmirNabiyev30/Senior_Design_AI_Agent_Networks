import random

class MultiAgent:
    def choose_actions(self, states):

        actions = []

        for state in states:

            if state[1] > 0.5:
                actions.append(1)
            else:
                actions.append(random.randint(0, 4))

        return actions