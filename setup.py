from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
    description = readme.read()
    
setup(
    name="DataGouvPy",
    version="1.1.0",
    license="Apache-2.0",
    author="CROUStillant Développement",
    keywords="data.gouv.fr, crous, crous api, crous api python, crous api wrapper",
    description="A Python wrapper for the data.gouv.fr API.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/CROUStillant-Developpement/DataGouvPy",
    project_urls={
        "Documentation": "https://github.com/CROUStillant-Developpement/DataGouvPy",
        "Issue tracker": "https://github.com/CROUStillant-Developpement/DataGouvPy/issues",
      },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "aiohttp>=3.11.16",
        "async-timeout>=5.0.1",
        "pandas>=2.2.3",
    ]
)
