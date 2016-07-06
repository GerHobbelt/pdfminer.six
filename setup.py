import codecs
import os
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

about = {}
with codecs.open(
    os.path.join(here, 'pdfminer3', '__version__.py'), encoding='utf-8'
) as f:
    exec(f.read(), about)


requires = ['cryptography', 'sortedcontainers']
if sys.version_info >= (3, 0):
    requires.append('chardet')

setup(
    name='3stack-pdfminer3',
    version=about['__version__'],
    packages=['pdfminer3'],
    package_data={'pdfminer3': ['cmap/*.pickle.gz']},
    install_requires=requires,
    description='PDF parser and analyzer',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT/X',
    author='Yusuke Shinyama & contributors',
    author_email='george.w.king@gmail.com',
    url='https://github.com/3stack-software/pdfminer/',
    scripts=['tools/pdf2txt.py', 'tools/dumppdf.py', 'tools/latin2ascii.py'],
    keywords=['pdf', 'pdf parser', 'pdf converter', 'layout analysis', 'text mining'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Text Processing',
    ],
)
