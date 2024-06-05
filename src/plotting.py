import matplotlib.pyplot as plt
import numpy as np



# a = np.random.random((16, 16))
# plt.imshow(a, cmap='hot', interpolation='nearest')
# plt.show()

def plot_letter_distribution(letters_ranked: dict, best_guess: str):
    # Convert dictionary to 2D array
    data = np.array(list(letters_ranked.values()))
    
    # Create the heatmap
    plt.figure(figsize=(8, 6))
    plt.imshow(data, cmap='viridis', aspect='auto')

    # Add color bar
    plt.colorbar()

    # Add labels
    plt.xticks(np.arange(len(letters_ranked['a'])))
    plt.yticks(np.arange(len(letters_ranked)), labels=letters_ranked.keys())

    # Add title
    plt.title(f"Letter heatmap for guess='{best_guess}'")

    # Display the heatmap
    plt.show()


# t = {
#     'a': [40, 20, 50, 10, 50],
#     'b': [60, 24, 12, 25, 150],
#     'c': [60, 24, 12, 25, 150],
#     'd': [60, 24, 12, 25, 150],
#     'e': [60, 24, 12, 25, 150],
#     'f': [60, 24, 12, 25, 150],
# }
# plot_letter_distribution(t)