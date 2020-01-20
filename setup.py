import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tflite",
    version="2.1",
    author="google",
    author_email="google@google.com",
    description="TFLite",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FrozenGene/tflite",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
