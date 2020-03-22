from gym.envs.registration import register

register(
    id='cartpoletwist-v0',
    entry_point='gym_cartpoletwist.envs:CartPoleTwistEnv',
)