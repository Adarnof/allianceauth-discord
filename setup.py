# -*- coding: utf-8 -*-
from setuptools import setup
import discord

install_requires = [
    'requests>=2.9.1',
    'requests-oauthlib',
    'celery>=4.0.2',
    'allianceauth==2.0b3',
    'django>=1.11',
]

testing_extras = [
    'coverage>=4.3.1',
    'requests-mock>=1.2.0',
    'django-nose',
    'django-webtest',
]

setup(
    name='allianceauth-discord',
    version=discord.__version__,
    author='Alliance Auth',
    author_email='adarnof@gmail.com',
    description='Discord service module for Alliance Auth',
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
    },
    python_requires='~=3.4',
    license='GPLv2',
    packages=['discord'],
    url='https://github.com/allianceauth/allianceauth-discord',
    zip_safe=False,
    include_package_data=True,
    entry_points="""
            [console_scripts]
            discord-bot=discord.bin.discordbot:main
    """,
)


