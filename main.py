import sys
import gym
from register_env import register_env
from agent import QLearning

id_env = "Student"
entry_point = "environment:Student"
register_env(id_env, entry_point)

def train(env, agent, episodes):
    for _ in range(episodes):
        observation, _ = env.reset(seed=17)
        terminated, truncated = False, False
        #while not (terminated or truncated):
        action = agent.get_action(observation, "random")
        new_observation, reward, terminated, truncated, _ = env.step(action)
        agent.update(observation, action, new_observation, reward, terminated)
        observation = new_observation


def play(env, agent):
    observation, _ = env.reset()
    env.render()
    terminated, truncated = False, False
   # while not (terminated or truncated):
    action = agent.get_action(observation, "greedy")
    new_observation, reward, terminated, truncated, _ = env.step(action)
    agent.update(observation, action, new_observation, reward, terminated)
    observation = new_observation
    env.render()


if __name__ == "__main__":

    env = gym.make(id_env)
    agent = QLearning(
        env.observation_space.n, env.action_space.n, alpha=0.1, gamma=0.9, epsilon=0.3
    )
    # alpha -> Que tan rápido aprende el modelo (Importancia a la observación)
    # epsilon -> Que tanto usa el conocimiento (0-> exploración, 1->explotación)

    episodes = 100 if len(sys.argv) == 1 else int(sys.argv[1])

    train(env, agent, episodes)
    agent.render()
    env.close()

    # env = gym.make(id_env)
    # play(env, agent)
    # env.close()
