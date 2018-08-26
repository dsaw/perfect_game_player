from setuptools import setup

setup(name='Perfect game player',
      version='1.0',
      description='Plays board games using Minimax algorithm',
      long_description=open("README.md"),
      url='https://github.com/dsaw/perfect-game-player',
      author='Devesh Sawant',
      author_email='devesh47cool@gmail.com',
      license='GPLv3',
      install_requires=[],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False
)