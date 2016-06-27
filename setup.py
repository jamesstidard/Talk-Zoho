from distutils.core import setup

setup(
    name='Talk Zoho',
    version='0.1.dev3',
    packages=[
        'talkzoho',
        'talkzoho.crm',
        'talkzoho.books'
    ],
    long_description=open('README.md').read(),
)
