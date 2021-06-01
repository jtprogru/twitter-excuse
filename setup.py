from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="twtrexcs",
    version="2021.1.0",
    description="A simple project for autoposting excuse in Twitter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jtprogru/twitter-excuse",
    author="Michael (jtprogru) Savin",
    author_email="jtprogru@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: WTFPL",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Natural Language :: Russian",
    ],
    keywords="sample, twitter, development, excuses",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8, <4",
    install_requires=["twitter"],
    extras_require={
        "dev": ["autopep8", "flake8", "flake8-colors"],
        "test": ["coverage", "pytest"],
    },
    entry_points={"console_scripts": ["twtrexcs=twtrexcs:main",],},
    project_urls={
        "Bug Reports": "https://github.com/jtprogru/twitter-excuse/issues",
        "Patreon": "https://patreon.com/jtprog",
        "Sobe.ru": "https://sobe.ru/na/jtprogru",
        "Source": "https://github.com/jtprogru/twitter-excuse",
    },
)
