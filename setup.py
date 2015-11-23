import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "DataAnalytics",
    version = "0.0.12",
    author = "Tom Wiesing",
    author_email = "tkw01536@gmail.com",
    description = ("Python Library for DataAnalytics"),
    license = "MIT",
    url = "https://github.com/tkw1536/DataAnalytics",
    packages=['DataAnalytics', 'DataAnalytics.textual'],
    install_requires=('numpy', 'matplotlib', 'scipy', 'sklearn', 'networkx'),
    long_description=read('README.md'),
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
)
