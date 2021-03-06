import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="sdelmo",
    version="2.0.2",
    author="elmoiv",
    author_email="elmoiv@yahoo.com",
    description="Simple downloader for soundcloud",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elmoiv/sdelmo",
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)