from setuptools import setup, find_packages

setup(
    name='file-helper',
    version='1.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'fh = filehelper:cli'
        ],
    },
)
