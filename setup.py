from setuptools import setup, find_packages
setup(
    name="quilt-fleet-publish",
    version="0.1.0",
    description="One tool to publish all quilt repos to npmjs/PyPI/crates.io",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Casey / SuperInstance",
    packages=find_packages(),
    python_requires=">=3.8",
)
