import random, gym

from gym import spaces

random.seed(17)
# Representación de una skill
class Skill:
    def __init__(self, skill):
        self.skill = skill # Categoria

    def execute(self, emotion): # Acción que ejecuta (Evalúa la probabilidad y retorna o no ganancia)
        # Sorpresa -> 0, Alegría -> 1, Asco -> 2, Tristeza -> 3, Ira -> 4, Miedo -> 5 
        if self.skill == "limites":
            if emotion == 5 and random.random() < 0.05:
                return .1
            elif emotion == 4 and random.random() < 0.09:
                return .33
            elif emotion == 3 and random.random() < 0.26:
                return .42
            elif emotion == 2 and random.random() < 0.19:
                return .35
            elif emotion == 1 and random.random() < 0.35:
                return .5
            elif emotion == 0 and random.random() < 0.45:
                return .15
            return .6
        elif self.skill == "derivadas":
            if emotion == 5 and random.random() < 0.1:
                return .38
            elif emotion == 4 and random.random() < .03:
                return .26
            elif emotion == 3 and random.random() < 0.5:
                return .312
            elif emotion == 2 and random.random() < 0.01:
                return .41
            elif emotion == 1 and random.random() < 0.7:
                return .77
            elif emotion == 0 and random.random() < 0.65:
                return .35
            return .4
        elif self.skill == "inecuaciones":
            if emotion == 5 and random.random() < 0.2:
                return .25
            elif emotion == 4 and random.random() < .09:
                return .10
            elif emotion == 3 and random.random() < 0.05:
                return .74
            elif emotion == 2 and random.random() < 0.23:
                return .34
            elif emotion == 1 and random.random() < 0.75:
                return .83
            elif emotion == 0 and random.random() < 0.45:
                return .27
            return .18
        elif self.skill == "conicas":
            if emotion == 5 and random.random() < 0.075:
                return .33
            elif emotion == 4 and random.random() < .1:
                return .39
            elif emotion == 3 and random.random() < 0.18:
                return .46
            elif emotion == 2 and random.random() < 0.05:
                return .54
            elif emotion == 1 and random.random() < 0.4:
                return .66
            elif emotion == 0 and random.random() < 0.85:
                return .44
            return .22
        elif self.skill == "funciones":
            if emotion == 5 and random.random() < 0.25:
                return .40
            elif emotion == 4 and random.random() < .045:
                return .41
            elif emotion == 3 and random.random() < .4:
                return 0.6
            elif emotion == 2 and random.random() < 0.2333:
                return .75
            elif emotion == 1 and random.random() < 0.5673:
                return .90
            elif emotion == 0 and random.random() < 0.7875:
                return .5
            return .1

class Student(gym.Env):
    def __init__(self):
        super().__init__()
        # Recomendable usarlos como tuplas o listas, porque gym retorna las acciones como enteros
        # Ver línea 62
        #---------------------------------------
        self.skills = (Skill("limites"),Skill("derivadas"),Skill("funciones"),Skill("inecuaciones"),Skill("conicas"))
        #---------------------------------------
        # Obligatorio de gym (Define el espacio de estados el ambiente)
        # Equivalente a las emociones (Modelo de Paul Ekman: 6 emociones)
        # Emociones: Sorpresa -> 0, Alegría -> 1, Asco -> 2, Tristeza -> 3,
        # Ira -> 4, Miedo -> 5 
        #------------------------------------------
        self.observation_space = spaces.Discrete(6)
        #------------------------------------------
        # Obligatorio de gym (Define el espacio de acciones -> Posibles acciones a tomar)
        # En este caso las acciones = tareas = categorias -> 6 categorias
        #--------------------------------------------------
        self.action_space = spaces.Discrete(len(self.skills))
        #--------------------------------------------------
        print("Student Environment")
        self.current_state = 1 # Equivalente a una emoción
        self.action = None # Equivalante a una categoria
        self.reward = None # Equivalente a respondió bien o no (booleano)

    # Función para retornar el estado actual del espacio de estado
    # En este caso siempre está en el mismo estado
    def _get_obs(self):
        return self.current_state

    # Función para retornar información sobre estado actual del espacio de estado
    def _get_info(self):
        return {"state": self._get_obs(), "last-action:": self.action, "reward":self.reward}

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
        self.reward = self.skills[action].execute(self.current_state)
        if self.reward <= 0.14:
            self.current_state = 2
        elif self.reward <= 0.2:
            self.current_state = 4
        elif self.reward <= 0.25:
            self.current_state = 3
        elif self.reward <= 0.30:
            self.current_state = 5
        elif self.reward <= 0.45:
            self.current_state = 0
        else:
            self.current_state = 1
        observation = self._get_obs()
        info = self._get_info()

        self.render()
        # Observation, reward, finished, truncated, info
        return observation, self.reward, False, False, info

    def render(self):
        print(self._get_info())

    def close(self):
        super().close()
