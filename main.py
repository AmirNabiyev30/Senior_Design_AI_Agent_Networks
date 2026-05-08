from experiments.run_experiments import run_experiment
from visualization.graphs import plot_results

noise_levels = [0.1, 0.3, 0.5]

single_results = []
multi_results = []

for noise in noise_levels:

    single, multi = run_experiment(noise)

    single_results.append(single)
    multi_results.append(multi)

    print(f"Noise: {noise}")
    print(f"Single-Agent Reward: {single}")
    print(f"Multi-Agent Reward: {multi}")
    print()

plot_results(
    noise_levels,
    single_results,
    multi_results
)