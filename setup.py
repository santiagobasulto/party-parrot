import setuptools


setuptools.setup(
    name="party-parrot",
    version="0.0.2",
    author="Santiago Basulto",
    author_email="santiago.basulto@gmail.com",
    description="Party or die",
    long_description="A funny package to join Parrot's party",
    long_description_content_type="text/markdown",
    url="https://github.com/santiagobasulto/party-parrot",
    packages=['party_parrot'],
    package_data={
        'party_parrot': ['frames/*.txt'],
    },
    scripts=['main.py'],
    entry_points={
        'console_scripts': [
            'party = main:party'
        ]
    },
    install_requires=[
        "asciimatics==1.9.0",
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
