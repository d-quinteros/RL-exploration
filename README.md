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

This is the Agent-Environment interaction loop which is the core of many RL problems. The **Agent** does some **action** and interacts with the **environment**. The Environment returns a **state** and a **reward**, which will be used by the Agent to determine its next action.

Think about driving a car. In the agent-environment loop, a driver (agent) observes the traffic and road conditions (environment) as they drive. They take actions such as steering or braking to navigate through traffic (action). As a result, they see how the car responds and how the traffic changes (new state). If their actions are appropriate for their situation, like braking at a red light, they can eventually reach their destination safely (reward).

But how does the agent know what to do when in a particular state? That has to do with the concept of **policy**.

![Screenshot (118)](https://github.com/user-attachments/assets/9a5f9bab-7acb-4fd1-b3bc-dd35cbd2e1d7)

The policy determines how the agent should behave in a certain situation. Reinforcement learning uses two approaches to develop policies: **on-policy** and **off-policy**.  

In on-policy methods, the agent learns and improves the same policy it's using to make decisions. This means the agent directly learns from its own actions and experiences in the environment.

Off-policy methods are a bit different. Here, the agent learns one policy while possibly behaving according to a different one. This allows it to explore the environment in one way while still figuring out the best actions for a potentially better strategy.

(Note: We will be using the Q-learning algorithm, which is off-policy, so we will be diving deeper into off-policy.)

So, what makes a policy "good," and how do we go about developing one? A good policy is one that maximizes the total reward accumulated over a given time period. Let's take a trip to the casino.

![Screenshot (120)](https://github.com/user-attachments/assets/5313e218-c289-4612-9d8a-c5f27fc58ad7)

Let’s say we want to do 1,000 plays on the slot machines. Looking at the probabilities of a payout, we’d probably stick with slot machine #2 for all 1,000 plays. But that’s because we already know the probabilities of success. What if we didn’t?

If we didn’t know the probabilities, we could try playing each slot machine 250 times to gather some data. However, this approach wouldn’t necessarily result in the best possible outcome because we’d spend too much time on less promising machines. Instead, we need a strategy that balances exploration (trying different machines to learn about their payouts) and exploitation (focusing on the machine that seems to perform the best so far).

This balance is crucial in reinforcement learning because it helps the agent gather enough information to make good decisions without wasting resources on less-optimal choices.

Now that we have an idea of what a good policy is and a general understanding of how to develop one, let’s talk about the two main ways policies are used in reinforcement learning algorithms: **value-based** and **policy-based**.

In value-based methods, the goal is to estimate the value of different actions or states to figure out the best policy. Basically, these methods calculate how much reward you can expect by taking a specific action in a given state, and then they use those values to decide what to do. The policy isn’t directly learned; it’s based on these value estimates.

Policy-based methods, on the other hand, skip the value calculations and focus on learning the policy itself. Instead of estimating rewards for each action, the algorithm directly works on figuring out the best actions to take in any situation.

Since Q-learning is a value-based approach, let’s take a closer look at how value-based methods work.
![Screenshot (121)](https://github.com/user-attachments/assets/b4de98a6-fbf5-4656-bf67-d4461a21bb9d)

Value-based methods use a value function to determine the policy that maximizes the total reward. The value function takes inputs and produces a score based on them. The specific inputs depend on the type of value function being used: the **state value function** or the **state-action value function**.

State value functions take the current state of the agent and output a numerical score that answers the question, "How good is it to be in this state?" On the other hand, state-action value functions take both the current state and the action the agent performs, outputting a numerical score known as a "q-value." This q-value answers the question, "How good is it to be in this state and take this specific action?"

In Q-learning, state-action value functions are used, which is why we refer to the value as a "q-value."

![lagrida_latex_editor (1)](https://github.com/user-attachments/assets/7e2871d6-a43e-438b-bd15-44a53c195a90)

This function is the core of Q-learning. I initially tried to explain it with written content and visuals, but the visuals were better suited for a video, so I decided to scrap that approach. Instead, I recommend watching this short [<sup>9-minute clip</sup>]([https://www.youtube.com/watch?v=lfPEJPHUllg&list=PLTl9hO2Oobd9kS--NgVz0EPNyEmygV1Ha&index=1](https://youtu.be/TiAXhVAZQl8?si=XblpvYOAIfi6DTCs&t=197)) for a high-level overview of how the function works.

## My Implementation
