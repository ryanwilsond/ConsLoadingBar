from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ConsLoadingBar",
    version="1.2.3",
    author="flamechain",
    author_email="rwc@thezulus.com",
    description="Easy to make progress bars",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    # install_requires = [
    #   "termcolor >= 1.1.0",
    # ],
)

# delete files from dist
# update version number
# run: python3 setup.py sdist bdist_wheel
# run: twine upload dist/*
# push to git
