from setuptools import setup

setup(name='gym_cartpoletwist',
      version='0.0.2',
      install_requires=['gym'],  # And any other dependencies foo needs
      packages=['gym_cartpoletwist', 'gym_cartpoletwist.envs']
)