import matplotlib.pyplot as plt

def plot_results(noise_levels, single_results, multi_results):

    plt.plot(noise_levels, single_results, label="Single-Agent")

    plt.plot(noise_levels, multi_results, label="Multi-Agent")

    plt.xlabel("Noise Level")
    plt.ylabel("Average Reward")

    plt.title("Agent Performance Under Noise")

    plt.legend()

    plt.savefig("results/performance.png")

    plt.show()