# RL-exploration

## Install Requirements
- `pip install gym`
- `pip install matplotlib`
- `pip install pygame`
- `pip install numpy==1.23.5`

---

## Reinforcement Learning Foundation and Context

"Reinforcement learning is learning what to do—how to map situations to actions—so as to maximize a numerical reward signal." ([<sup>1</sup>](https://www.youtube.com/watch?v=lfPEJPHUllg&list=PLTl9hO2Oobd9kS--NgVz0EPNyEmygV1Ha&index=1))

![Markov_diagram_v2](https://github.com/user-attachments/assets/eaee46e6-3d67-4a74-bf0f-21e19db2347d)

This is the Agent-Environment interaction loop which is the core of many RL problems. The Agent does some action and interacts with the environment. The Environment returns a state and a reward, which will be used by the Agent to determine its next action.

Think about driving a car. In the agent-environment loop, a driver (agent) observes the traffic and road conditions (environment) as they drive. They take actions such as steering or braking to navigate through traffic (action). As a result, they see how the car responds and how the traffic changes (new state). If their actions are appropriate for their situation, like braking at a red light, they can eventually reach their destination safely (reward).

But how does the agent know what to do when in a particular state? That has to do with the concept of "policy."

![Screenshot (118)](https://github.com/user-attachments/assets/9a5f9bab-7acb-4fd1-b3bc-dd35cbd2e1d7)

The policy determines how the agent should behave in a certain situation.
