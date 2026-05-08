from Senior_Design_AI_Agent_Networks.environment.wireless_env import WirelessEnvironment
from Senior_Design_AI_Agent_Networks.agents.single_agent import SingleAgent
from Senior_Design_AI_Agent_Networks.agents.multi_agent import MultiAgent

import numpy as np

def run_experiment(noise_level, episodes=50):

    env = WirelessEnvironment(
        num_agents=3,
        noise_level=noise_level
    )

    single_agent = SingleAgent()
    multi_agent = MultiAgent()

    single_rewards = []
    multi_rewards = []

    for _ in range(episodes):

        state = env.reset()

        single_action = [
            single_agent.choose_action(state)
            for _ in range(3)
        ]

        _, rewards = env.step(single_action)

        single_rewards.append(np.mean(rewards))

        multi_actions = multi_agent.choose_actions(state)

        _, rewards = env.step(multi_actions)

        multi_rewards.append(np.mean(rewards))

    return (
        np.mean(single_rewards),
        np.mean(multi_rewards)
    )