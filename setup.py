from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    description="image processing package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joaopmelosantos/image-processing-package",
    packages=find_packages(),
    install_requirements=requirements,
    python_requires=">=3.5",
)