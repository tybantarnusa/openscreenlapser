from setuptools import setup

REQUIRED = [
    'ffmpeg',
    'python-pip',
    'python-pil',
    'scrot',
    'python-pygame',
]

setup(
    name='openscreenlapser',
    version='1.0.0',
    description='Screen timelapse video maker.',
    author='Mgs. M. Thoyib Antarnusa',
    author_email='tybantarnusa@null.net',
    maintainer='Mgs. M. Thoyib Antarnusa',
    maintainer_email='tybantarnusa@null.net',
    url='http://www.github.com/tybantarnusa/openscreenlapser/',
    license='Apache',
    install_requires=REQUIRED,
    packages=['openscreenlapser', 'openscreenlapser.aesthetic', 'openscreenlapser.logic'],
    entry_points={
        'gui_scripts': ['openscreenlapser = openscreenlapser.main:main']
    },
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia :: Graphics :: Capture :: Screen Capture',
        'Topic :: Multimedia :: Sound/Audio :: Capture/Recording',
        'Topic :: Multimedia :: Video :: Capture',
    ],
)
