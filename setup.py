from setuptools import setup, find_packages

setup(
    name = "Greetings",
    version = "0.1",
    packages = find_packages(exclude = ['*test']),
    scripts = ['greetings/greeter.py'],
    install_requires = ['argparse']
)

 