import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="singlecell",
    version="1.0.1",
    author="Edwin Vans",
    author_email="vans.edw@gmail.com",
    description="A python package for managing single-cell RNA-seq data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edwinv87/singlecell",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)