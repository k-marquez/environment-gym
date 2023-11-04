import random
import time

import gym
from gym import spaces

# Representación de una skill
class Skill:
    def __init__(self, p=0, earn=0):
        self.probability = p # Probabilidad de ganar
        self.earn = earn # Recompensa si se da la probabilidad

    def execute(self): # Acción que ejecuta (Evalúa la probabilidad y retorna o no ganancia)
        return self.earn if random.random() < self.probability else 0


class Student(gym.Env):
    def __init__(self):
        super().__init__()
        self.delay = 0.5
        # Recomendable usarlos como tuplas o listas, porque gym retorna las acciones como enteros
        # Ver línea 65
        #---------------------------------------
        self.skills = (Skill(),Skill(),Skill(),Skill(),Skill(),Skill())
        #---------------------------------------
        # Obligatorio de gym (Define el espacio de estados el ambiente)
        # Equivalente a las emociones (Modelo de Paul Ekman: 6 emociones)
        #------------------------------------------
        self.observation_space = spaces.Discrete(6)
        #------------------------------------------
        # Obligatorio de gym (Define el espacio de acciones -> Posibles acciones a tomar)
        # En este caso las acciones = tareas = categorias -> 6 categorias
        #--------------------------------------------------
        self.action_space = spaces.Discrete(len(self.skills))
        #--------------------------------------------------
        print("Two-Armed Bandit Environment")
        self.current_state = None # Equivalente a una emoción
        self.action = None # Equivalante a una categoria
        self.reward = None # Equivalente a respondió bien o no (booleano)

    # Función para retornar el estado actual del espacio de estado
    # En este caso siempre está en el mismo estado
    def _get_obs(self):
        return self.current_state

    # Función para retornar información sobre estado actual del espacio de estado
    def _get_info(self):
        return {"state": self._get_obs()}

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        # Por ahora no usado
        if options is not None:
            if not isinstance(options, dict):
                raise RuntimeError("Variable options is not a dictionary")

        observation = self._get_obs()
        info = self._get_info()
        return observation, info # Por obligación se deben retornar este par de valores

    def step(self, action):
        self.action = action
        self.reward = self.skills[action].execute()
        observation = self._get_obs()
        info = self._get_info()

        self.render()

        return observation, self.reward, False, False, info

    def render(self):
        print(self._get_info())

    def close(self):
        super().close()
