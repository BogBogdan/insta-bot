from setuptools import setup, find_packages

setup(
    name='MojaAplikacija',
    version='1.0.0',
    packages=find_packages(),
    scripts=['my_script.py'],
    author='Vaše Ime',
    author_email='email@example.com',
    description='Opis vaše aplikacije',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'schedule',
        'selenium',
        'webdriver_manager',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
