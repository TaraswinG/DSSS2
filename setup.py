from setuptools import setup
find_packages

with open('.\\requirements.txt') as file:
    requirements = file.read().splitlines()

setup(
        name = 'dsss2',
        version = '0.0.0',
        packages = find_packages(),
        install_requires = requirements,
        entry_points = {
            'console_scripts':['math_quiz = math_quiz:main',],
            },
        author = 'Taraswin'
    )
