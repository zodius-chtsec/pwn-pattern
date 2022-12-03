from setuptools import setup, find_packages

setup(
    name="pwn-pattern",
    version="1.0",
    author="zodius",
    author_email="zodius.chen@gmail.com",
    description="Cyclic pattern generator for pwn",
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'pattc = PwnPattern:pattc',
            'patts = PwnPattern:patts',
        ]
    },
)