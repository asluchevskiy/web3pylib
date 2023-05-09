from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="web3pylib",
    version="0.1.0",
    author="Arseny Sluchevskiy",
    author_email="arseniy.sluchevskiy@gmail.com",
    description="Python wrapper and utils for web3.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asluchevskiy/web3pylib",
    packages=find_packages(),
    install_requires=[
        "web3",
        "colorlog",
        # Add other dependencies here
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)