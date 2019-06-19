from setuptools import setup


setup(
    name="pre_commit_dummy_package",
    version="0.0.0",
    install_requires=[
        "isort@git+https://github.com/mattbennett/isort.git@4.3.20-dev#egg=4.3.20-dev"
    ],
)
