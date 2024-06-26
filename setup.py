import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cass",
    version="1.0.0",
    author="Begüm İpek",
    author_email="ipekkbegumm@gmail.com",
    description="Extendable communication library with support for various protocols for the use of CASMarine ROV team",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bbegumipek/deneme",
    project_urls={
        "Bug Tracker": "https://github.com/bbegumipek/issues",
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=['tests', 'test']),
    install_requires=["pyserial", "crccheck", "stm32loader", "requests", "packaging"],
    python_requires=">=3.7"
)
