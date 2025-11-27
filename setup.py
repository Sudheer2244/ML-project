from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Return list of requirements from a requirements file.
    Ignores empty lines and comments and handles missing file gracefully.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reqs = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]
    except FileNotFoundError:
        # If the requirements file does not exist, return an empty list
        return []

    # remove editable local install marker if present
    if HYPHEN_E_DOT in reqs:
        reqs.remove(HYPHEN_E_DOT)

    return reqs


setup(
    name="mlproject",
    version="0.0.1",
    author="sudheer",
    author_email="sudheerb607@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)