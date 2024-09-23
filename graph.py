import matplotlib.pyplot as plt

# Data from the tables
generations = ['Start of Gen 1', 'End of Gen 1', 'Start of Gen 2', 'End of Gen 2', 'Start of Gen 3', 'End of Gen 3']

# Data without predators
fork_no_predators = [4, 1, 2, 2, 3, 3]
tweezer_no_predators = [4, 2, 4, 1, 2, 1]
hand_no_predators = [4, 4, 8, 8, 12, 7]
knife_no_predators = [4, 0, 0, 0, 0, 0]
spoon_no_predators = [4, 1, 2, 1, 3, 1]

# Plotting the data without predators
plt.figure(figsize=(10, 6))

plt.plot(generations, fork_no_predators, marker='o', label='Fork Beak', color='purple')
plt.plot(generations, tweezer_no_predators, marker='o', label='Tweezer Beak', color='green')
plt.plot(generations, hand_no_predators, marker='o', label='Hand Beak', color='blue')
plt.plot(generations, knife_no_predators, marker='o', label='Knife Beak', color='red')
plt.plot(generations, spoon_no_predators, marker='o', label='Spoon Beak', color='orange')

# Adding titles and labels
plt.title('Impact of Different beak types on Finch Population over Time')
plt.xlabel('Generation')
plt.ylabel('Number of Beak Types')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# Adjust layout and show plot
plt.tight_layout()
plt.show()
plt.
