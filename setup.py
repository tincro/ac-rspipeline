import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="magpie", # Replace with your own username
    version="0.0.1",
    author="Austin Cronin",
    author_email="austin.cronin3d@gmail.com",
    description="A package for project creation and navigation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tincro/magpie",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)