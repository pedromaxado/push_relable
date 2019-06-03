import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='push_relable',
    version='0.0.1',
    packages=setuptools.find_packages(),
    install_requires=required,
    url='https://github.com/pedromaxado/push_relable',
    license='GNU GPLv3',
    author='Pedro Otávio',
    author_email='p.o.maxado@gmail.com',
    long_description=long_description,
    description='Push-Relable algorithm with FIFO implementation to solve maximum flow problem in a directed graph.'
)
