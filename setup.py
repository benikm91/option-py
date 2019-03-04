from setuptools import setup, find_packages

setup(
    name='option',
    version='0.1',
    description='Simple Option implementation.',
    url='https://github.com/benikm91/option-py',
    author='Benjamin Meyer',
    author_email='benjamin.meyer@fhnw.ch',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    python_requires='>=3',
    include_package_data=True,
    install_requires=[
    ],
)