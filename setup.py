from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(filePath : str) -> List[str]:
    requirements = []
    with open(filePath) as fileObejct:
        requirements = fileObejct.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(name="StudentPerformanceML", version="0.0.1",author="Vedant Sagwal",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)