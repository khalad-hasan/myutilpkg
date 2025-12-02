from setuptools import setup, find_packages

setup(
    name="myutilpkg",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.8",
    description="A simple Python utility package with math and string helpers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    url="https://github.com/mkhasan/myutilpkg",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
