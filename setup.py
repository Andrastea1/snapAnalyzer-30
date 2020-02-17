from setuptools import setup

setup(
    name ='snapAnalyzer-30',
    version='0.1',
    author = "Robin Norwood",
    author_email = "mahimc@amazon.com",
    summary="SnapShotAnalyzer 30 is a tool to manage AWS EC@ snapshots",
    licence ="GPLv3+",
    packages=['shotty'],
    url="https://github.com/Andrastea1/snapAnalyzer-30",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
        ''',


)
