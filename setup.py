import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ZeusDetector",
    version="0.1",
    author="Sathish2004!",
    author_email="sourechebala19470@gmail.com",
    description="Detect profanity in a sentence.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZeusRepo/ZeusDetector",
    license="GNU AFFERO GENERAL PUBLIC LICENSE (v3)",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
