import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weirdtext-tools", 
    version="0.0.1",
    author="Mateusz Rędzia",
    author_email="123@example.com",
    description="Small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mat2314/weirdtext-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
