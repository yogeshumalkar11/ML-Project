from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e."


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, "r") as f:
        require = f.readlines()
        requirements = [req.replace("\n", "") for req in require]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="ML Project",
    version="1.0",
    author="yogeshumalkar11",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
