import codecs

from setuptools import setup, find_packages


def read_file(filename, cb):
    with codecs.open(filename, 'r', 'utf8') as f:
        return cb(f)


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kocrawl-cna',
    version='1.0.1',
    description='Korean web crawler collections',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='(original : Hyunwoong Ko), Saebom Lee, Jeongyun Seo, Youngeun Cho',
    author_email='gusdnd852@naver.com',
    url='https://github.com/choyoungeun/kocrawl-cna.git',
    packages=find_packages(exclude=[]),
    keywords=['crawler', 'korean crawler', 'kochat'],
    install_requires=read_file('requirements.txt', lambda f: list(
        filter(bool, map(str.strip, f)))),
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
