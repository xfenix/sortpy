import setuptools

from xfsort import __version__


with open('README.md', 'r') as fh:
    DESCRIPTION = fh.read()


setuptools.setup(
    name='xfsort',
    version=__version__,
    author='Denis Anikin',
    author_email='ad@xfenix.ru',
    description='A bunch of serious sorting algorithms in pure python',
    python_requires='>=3.5.0',
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/pypa/xfsort',
    packages=setuptools.find_packages(),
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=(
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)