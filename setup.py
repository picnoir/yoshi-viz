from distutils.core import setup

requirements = [
    "jinja2",
    "pip",
]

setup(
    name="YoshiViz",
    packages=["YoshiViz"],
    version="0.0.1",
    description="Visualisation layer for Yoshi",
    install_requires=requirements
)
