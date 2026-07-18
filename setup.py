
from pathlib import Path
from setuptools import find_packages, setup


def get_requirements(file_path: str) -> list[str]:
    requirements_path = Path(__file__).resolve().parent / file_path
    requirements: list[str] = []

    for line in requirements_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("-r"):
            continue
        if line.startswith("-e "):
            continue
        requirements.append(line)

    return requirements


setup(
    name="ml-project",
    version="0.0.1",
    author="Devansh Bhalla",
    author_email="info.devanshbhalla@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.9",
)