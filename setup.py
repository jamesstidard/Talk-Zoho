from distutils.core import setup
from pip.req import parse_requirements as parse


setup(
    name='Talk Zoho',
    version='0.2.dev0',
    packages=[
        'talkzoho',
        'talkzoho.crm',
        'talkzoho.books'
    ],
    long_description=open('README.md').read(),
    install_requires=[str(r.req) for r in parse('requirements.txt', session=False)],  # noqa
)
