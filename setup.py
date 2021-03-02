from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

_VERSION = '1.0.0'

setup(
    name='htmlBuilder',
    packages=['htmlBuilder'],
    version=_VERSION,
    description='A beautiful html builder library.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Jaime Viñas',
    author_email='jaimevp54@gmail.com',
    license="MIT",
    url='https://github.com/jaimevp54/htmlBuilder',
    download_url=f'https://github.com/jaimevp54/htmlBuilder/archive/{_VERSION}.tar.gz',
    keywords=['html', 'builder', 'render', 'template', 'templating', 'python'],
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)
