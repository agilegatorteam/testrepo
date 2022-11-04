from setuptools import setup, find_packages

setup(
    name='project1',
    version="1.0.0",
    author='Mateo',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'': ['*']},
)
