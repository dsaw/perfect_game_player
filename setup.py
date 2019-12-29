from setuptools import setup, find_packages

setup(name='perfect_game_player',
      version='1.2',
      description='Plays board games using Minimax algorithm',
      url='https://github.com/dsaw/perfect-game-player',
      author='Devesh Sawant',
      author_email='devesh47cool@gmail.com',
      packages=find_packages(exclude=['tests']),
      test_suite='nose.collector',
      tests_require=['nose'],
      license='GPLv3',
      install_requires=[],
      zip_safe=False
      )
