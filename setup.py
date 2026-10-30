from setuptools import setup, find_packages
import os

__author__ = "Alexander Urban"
__email__ = "aurban@atomistic.net"

here = os.path.abspath(os.path.dirname(__file__))
package_name = 'dribble'
package_description = 'Lattice percolation simulations'

# Get the long description from the README file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as fp:
    long_description = fp.read()

# Get version number from the VERSION file
with open(os.path.join(here, package_name, 'VERSION')) as fp:
    version = fp.read().strip()

setup(
    name=package_name,
    version=version,
    description=package_description,
    long_description=long_description,
    url='https://github.com/urban-group/dribble/',
    author=__author__,
    author_email=__email__,
    license='MPL2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
    keywords=['percolation', 'materials science', 'monte carlo'],
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.8',
    include_package_data=True,
    install_requires=[
        'numpy>=1.20.1',
        'scipy>=1.5.0',
        'pymatgen>=2022.11.7'
    ],
    entry_points={
        'console_scripts': [
            'dribble=dribble.scripts.dribble:main',
        ],
    },
)
