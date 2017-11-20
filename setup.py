from setuptools import setup

REQUIRED = [
    'Pillow',
    'pyscreenshot'
]

setup(
    name='openscreenlapser',
    version='0.0.1',
    description='Screen timelapse video maker.',
    author='Mgs. M. Thoyib Antarnusa',
    author_email='tybantarnusa@gmail.com',
    url='http://www.github.com/tybantarnusa/openscreenlapser/',
    packages=['openscreenlapser', 'openscreenlapser.aesthetic', 'openscreenlapser.logic'],
    install_requires=REQUIRED,
)
