from setuptools import setup

setup( name='pyhello',
       version='0.1',
       description='This module greets the user.  ',
       url='',                # usually a github URL
       author='David Blaikie',
       author_email='david@davidbpython.com',
       license='MIT',
       packages=['pyhello'],
       install_requires=[ 'numpy' ],
       test_suite='pytest',
       setup_requires=['pytest-runner'],
       tests_require=['pytest'],
       zip_safe=False )

