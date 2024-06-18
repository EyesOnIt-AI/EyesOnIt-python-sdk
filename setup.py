from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    install_requires = fh.read().splitlines()

setup(
    name="EyesOnItSDK",
    version="1.0.0",
    author="EyesOnIt",
    author_email="info@eyesonit.us",
    description="Python SDK for EyesOnIt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EyesOnIt-AI/EyesOnIt-python-sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=install_requires,
)
