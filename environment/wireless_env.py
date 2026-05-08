import numpy as np

class WirelessEnvironment:
    def __init__(self, num_agents=3, noise_level=0.1):
        self.num_agents = num_agents
        self.noise_level = noise_level

        self.channels = np.zeros(num_agents)
        self.latency = np.random.uniform(1, 5, num_agents)
        self.interference = np.random.uniform(0, 1, num_agents)

    def reset(self):
        self.channels = np.zeros(self.num_agents)

        state = self._get_state()
        return state

    def _get_state(self):
        signal_strength = np.random.uniform(0.5, 1.0, self.num_agents)

        gaussian_noise = np.random.normal(
            0,
            self.noise_level,
            self.num_agents
        )

        state = []

        for i in range(self.num_agents):
            state.append([
                signal_strength[i],
                self.interference[i],
                self.latency[i],
                gaussian_noise[i]
            ])

        return np.array(state)

    def step(self, actions):
        rewards = []

        for i, action in enumerate(actions):

            reward = 10

            if action == 1:
                reward += 2

            if self.interference[i] > 0.7:
                reward -= 5

            reward -= abs(np.random.normal(0, self.noise_level))

            rewards.append(reward)

        next_state = self._get_state()

        return next_state, rewards