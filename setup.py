from setuptools import setup, find_packages


with open("README.md") as readme_file:
    readme = readme_file.read()


setup(
    name="icof",
    version="0.0.1",
    description="Is California On Fire?",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Brewster Malevich",
    author_email="sbmalev@gmail.com",
    url="https://github.com/brews/icof",
    packages=find_packages(),
    python_requires=">=3.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
    ],
    extras_require={
        "test": ["pytest"],
    },
)
