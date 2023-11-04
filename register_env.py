# Script para registrar un ambiente personalizado
from gym.envs.registration import register

def register_env(id_env:str, entry_point_env:str):
    register(
        # "TwoBanditsCustom" -> Id para usar con env.make(id)
        id=id_env,
        # "environment:TwoArmedBanditEnv" -> Objeto que contiene el ambiente personalizado
        entry_point=entry_point_env
    )
