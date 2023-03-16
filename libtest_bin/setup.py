from setuptools import setup


setup(
    name='libtest',

    version='1',

    description='',
    long_description='',

    author='Test',
    author_email='Test@test.te.st',

    license='Apache Software License',
    entry_points={
        'console_scripts': ['libtestmain=main:main'],
    },

    extras_require={
        'foo': ['libtest_foo'],
        'bar': ['libtest_bar'],
        'all': ['libtest_foo', 'libtest_bar'],
    },
)
