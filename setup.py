import setuptools

with open("README.rst", "r") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="limecore-logging",
    version="0.0.1",

    description="limecore: Logging",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/limecore/logging",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    author="Daniel Bradberry",
    author_email="daniel@danielbradberry.com",
    
    license='MIT',
    
    package_dir={'': 'src'},
    packages=[
        'limecore.logging',],
    
    install_requires=required,
    python_requires='>=3.7',
)
