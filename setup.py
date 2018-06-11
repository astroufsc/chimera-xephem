from distutils.core import setup

setup(
    name='chimera-xephem',
    version='0.0.1',
    packages=['chimera_xephem', 'chimera_xephem.controllers'],
    scripts=[],
    url='http://github.com/astroufsc/chimera-xephem',
    license='GPL v2',
    author='William Schoenell',
    author_email='william@iaa.es',
    description='Chimera controller plugin for XEphem integration'
)
