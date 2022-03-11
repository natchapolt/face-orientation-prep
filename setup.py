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
    install_requires=[
        "aniso8601==7.0.0",
        "Click==7.0",
        "cmake==3.14.4",
        "cycler==0.10.0",
        "decorator==4.4.0",
        "dlib==19.17.0",
        "Flask==1.0.3",
        "Flask-RESTful==0.3.7",
        "gunicorn==19.9.0",
        "imageio==2.5.0",
        "itsdangerous==1.1.0",
        "Jinja2==2.10.1",
        "kiwisolver==1.1.0",
        "MarkupSafe==1.1.1",
        "matplotlib==3.1.0",
        "networkx==2.3",
        "numpy==1.16.4",
        "opencv-contrib-python==4.1.0.25",
        "Pillow==9.0.1",
        "pyparsing==2.4.0",
        "python-dateutil==2.8.0",
        "pytz==2019.1",
        "PyWavelets==1.0.3",
        "scikit-image==0.15.0",
        "scipy==1.3.0",
        "six==1.12.0",
        "Werkzeug",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)