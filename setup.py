
from setuptools import setup, find_packages


def long_description():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="superglue",
    version="0.1.0",
    license="MagicLeap",
    description="SuperGlue: Learning Feature Matching with Graph Neural Networks.",
    long_description_content_type="text/markdown",
    install_requires=["torch", "numpy"],
    author="Paul-Edouard Sarlin, Daniel DeTone, Tomasz Malisiewicz and Andrew Rabinovich",
    url="https://github.com/SergioRAgostinho/SuperGluePretrainedNetwork",
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ],
)