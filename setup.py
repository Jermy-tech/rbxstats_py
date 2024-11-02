from setuptools import setup, find_packages

setup(
    name="rbxstats",
    version="0.1.1",
    description="A Python client for accessing the RBXStats API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="JermyOIS",
    author_email="rbxstatsxyz@gmail.com",
    url="https://github.com/Jermy-tech/rbxstats_api",  # Replace with your repo URL
    packages=find_packages(),
    install_requires=[
        "requests>=2.20.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
