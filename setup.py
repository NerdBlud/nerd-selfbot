from setuptools import setup, find_packages

setup(
    name="nerd-selfbot", 
    version="0.1",
    description="A custom library for creating Discord Self bots",
    author="nerdblud",
    author_email="your.email@example.com",
    url="https://github.com/nerdblud/nerd-selfbot", 
    packages=find_packages(),
    install_requires=[
        "discord.py>=2.0.0",
        "aiohttp>=3.8.0",
        "websockets>=10.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
