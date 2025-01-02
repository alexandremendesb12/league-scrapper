from setuptools import setup, find_packages

setup(
    name="league_scrapper",
    version="1.0.0",
    description="Scraper para dados de players de League of Legends.",
    author="alexandremendesb12",
    author_email="alexandrem.bastos2526@gmail.com",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4>=4.12.3"
        "certifi>=2024.12.14"
        "charset-normalizer>=3.4.1"
        "idna>=3.10"
        "soupsieve>=2.6"
        "typing>=3.7.4.3"
        "urllib3>=2.3.0"
    ],
    python_requires=">=3.10",
)
