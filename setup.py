#=============================================================================
#
# screener Package Setup Script
#
# ### Normal Installation
#
#     python setup.py install
#
# ### Development Installation (symlinks to current copy)
#
#     python setup.py develop
#
# ### Create a Compressed Source Distribution
#
#     python setup.py sdist
#
#=============================================================================

"""
screener Package Setup Script
=============================

Run this script to install the screener package for your system.

    python setup.py install

"""


from setuptools import setup


setup(
    name         = 'screener',
    version      = '0.0.0',
    description  = 'Python Code Screening Tools',
    url          = 'https://github.com/zhester/screener',
    author       = 'Zac Hester',
    author_email = 'zac.hester@gmail.com',
    license      = 'BSD',
    packages     = [ 'screener' ],
    zip_safe     = False
)

