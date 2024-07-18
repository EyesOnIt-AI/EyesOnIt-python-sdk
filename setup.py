from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    install_requires = fh.read().splitlines()

setup(
    name="EyesOnIt",
    version="2.0.3",
    author="EyesOnIt",
    author_email="info@eyesonit.us",
    description="Python SDK for EyesOnIt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EyesOnIt-AI/EyesOnIt-python-sdk",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=install_requires,
)
