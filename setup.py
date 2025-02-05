from setuptools import setup, find_packages

setup(
    name='package',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author='Aayush Sugandhi',
    author_email='aayush.sugandhi@gmail.com',
    description='A small package for random number guessing',
    long_description=open("readme.txt").read(),
    long_description_content_type="text/markdown",
    keywords='random number guessing',
    url='https://github.com/aayushsugandhi2703/python-libraries',
    python_requires='>=3.6',
)