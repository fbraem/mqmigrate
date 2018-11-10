from setuptools import setup
setup(
    name = 'mqmigrate',
    version = '0.0.1',
    entry_points = {
        'console_scripts': [
            'mqmigrate = src.__main__:main'
        ]
    })
