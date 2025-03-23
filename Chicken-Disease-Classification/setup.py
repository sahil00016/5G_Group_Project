from setuptools import setup, find_packages

setup(
    name="chicken-disease-classification",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "tensorflow",
        "scikit-learn",
        "flask",
        "dvc",
        "matplotlib",
        "seaborn",
        "PyYAML"
    ]
)
