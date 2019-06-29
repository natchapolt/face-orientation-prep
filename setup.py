import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="face-orientation-prep-natchapolt",
    version="0.0.1",
    author="Natchapol.TH",
    author_email="natchapol-t@hotmail.com",
    description="A simple face image orientation pre-processor package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/natchapolt/face-orientation-prep.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)