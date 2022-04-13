from setuptools import setup, find_packages

setup(
    name='fluent-python-note',
    extras_require=dict(test=['pytest']),
    packages=find_packages(where='src'),
    package_dir={"": 'src'},
)


