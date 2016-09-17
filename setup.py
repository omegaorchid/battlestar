from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='battlestar',
      version='0.1',
      description='Space Invaders type game',
      long_description='A game based on the original Space Invaders game styled as BattleStar Galactica ',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Topic :: Exploring the use of github, pygame and MVC in game design',
      ],
      keywords='model view controller mvc pygame github game design spaceinvaders space invaders battlestar galactica',
      url='https://github.com/omegaorchid/battlestar',
      author='Dameon Orin',
      author_email='omegaorchid@users.noreply.github.com',
      license='MIT',
      packages=['battlestar'],
      install_requires=[
          # 'markdown',
      ],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose2.collector',
      tests_require=['nose2'],
      scripts=['bin/']
      )
