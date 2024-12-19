import gym
import numpy as np

# Hyperparameter Constants
LEARNING_RATE = 0.1  # Controls how much the Q-value is updated after each action (step size)
DISCOUNT = 0.95      # Importance of future rewards (0 = focus on immediate rewards, 1 = focus on long-term rewards)
EPISODES = 25000     # Total number of training episodes
SHOW_EVERY = 2000    # Show the rendered environment every specified number of episodes

# Initialize the MountainCar-v0 environment without rendering
env = gym.make("MountainCar-v0")

# Define the discrete observation space and its bin size
DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)  # Split the observation space into 20 discrete bins for each dimension
DISCRETE_OS_BIN_SIZE = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE  # Calculate the bin size for discretization

# Epsilon parameters for exploration-exploitation tradeoff
epsilon = 0.5  # Initial exploration rate
START_EPSILON_DECAYING = 1  # Start decaying epsilon from episode 1
END_EPSILON_DECAYING = EPISODES // 2  # Stop decaying epsilon halfway through training
epsilon_decay_value = epsilon / (END_EPSILON_DECAYING - START_EPSILON_DECAYING)  # Calculate the decay value per episode

# Initialize Q-table with random values between -2 and 0
q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))

# Function to convert a continuous state to a discrete state index
def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low) / DISCRETE_OS_BIN_SIZE  # Normalize state and scale to discrete space
    return tuple(discrete_state.astype(int))  # Convert to integers and return as tuple

# Main training loop
for episode in range(EPISODES):
    # Render the environment only on specific episodes
    if episode % SHOW_EVERY == 0:
        print(f"Episode: {episode}")  # Print progress
        env = gym.make("MountainCar-v0", render_mode="human")  # Reinitialize environment with rendering
    else:
        env = gym.make("MountainCar-v0")                       # No rendering for other episodes

    # Reset the environment and get the initial state
    state, _ = env.reset()                      # Reset the environment
    discrete_state = get_discrete_state(state)  # Convert the continuous state to discrete
    done = False                                # Initialize the "done" flag

    while not done:
        # Choose action using epsilon-greedy strategy
        if np.random.random() > epsilon:
            action = np.argmax(q_table[discrete_state])  # Exploit: Choose the action with the highest Q-value
        else:
            action = np.random.randint(0, env.action_space.n)  # Explore: Choose a random action

        # Take the action and observe the result
        new_state, reward, terminated, truncated, _ = env.step(action)  # Perform the action
        new_discrete_state = get_discrete_state(new_state)              # Discretize the new state
        done = terminated or truncated                                  # Check if the episode is finished

        # Update the Q-value using the Q-learning formula
        if not done:
            max_future_q = np.max(q_table[new_discrete_state])  # Get the max Q-value for the next state
            current_q = q_table[discrete_state + (action,)]     # Get the current Q-value for the action taken
            # Calculate the new Q-value
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
            q_table[discrete_state + (action,)] = new_q  # Update the Q-value
        elif new_state[0] >= env.goal_position:  # Check if the goal was reached
            print(f"Objective completed on episode {episode}")  # Log success
            q_table[discrete_state + (action,)] = 0  # Set Q-value to 0 for goal-reaching state

        # Update the current state to the new state
        discrete_state = new_discrete_state

    # Decay epsilon for exploration-exploitation balance
    if END_EPSILON_DECAYING >= episode >= START_EPSILON_DECAYING:
        epsilon -= epsilon_decay_value

# Close the environment after training
env.close()
