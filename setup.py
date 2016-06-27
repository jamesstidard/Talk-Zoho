from distutils.core import setup
from pip.req import parse_requirements


# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt', session=False)

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]


setup(
    name='Talk Zoho',
    version='0.1.dev7',
    packages=[
        'talkzoho',
        'talkzoho.crm',
        'talkzoho.books'
    ],
    long_description=open('README.md').read(),
    install_requires=reqs,
)
