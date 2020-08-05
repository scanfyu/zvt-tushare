#!/usr/bin/env python

# To use a consistent encoding
from codecs import open
from os import path

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

install_reqs = parse_requirements("requirements.txt", session=False)

try:
    requirements = [str(ir.req) for ir in install_reqs]
except:
    requirements = [str(ir.requirement) for ir in install_reqs]

setup(
    name='zvt-tushare',
    version='0.0.1',
    description='tushare plugin for zvt,modular quantitative system for human beings ',
    long_description=long_description,
    entry_points={"zvt": ["tushare = zvt_tushare"]},
    py_modules=["zvt_tushare"],
    packages=find_packages(),
    package_data={
        'zvt_tushare.accounts': ['*.json']
    },
    url='https://github.com/scanfyu/zvt-tushare',
    author='scanfyu',
    author_email='494710584@qq.com',
    classifiers=[  # Optional
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Office/Business :: Financial :: Investment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],

    keywords='quant zvt financial data support from tushare',

    install_requires=requirements,
    
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/scanfyu/zvt-tushare/issues',
        'Funding': '',
        'Say Thanks!': '',
        'Source': 'https://github.com/scanfyu/zvt-tushare',
    },

    include_package_data=True,
    long_description_content_type="text/markdown",

)
