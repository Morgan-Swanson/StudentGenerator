import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="student", # Replace with your own username
    version="0.0.1",
    author="Luis Armendariz, Roxanne Miller, and Morgan Swanson",
    author_email="msswanso@calpoly.edu",
    description="A package for generating student data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Morgan-Swanson/StudentGenerator",
    packages=setuptools.find_packages(),
    package_data={'data': ['data/*']}
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
