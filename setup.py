from setuptools import setup

setup(
    name = 'easyencrypt',
    packages = ['easyencrypt'],
    version = '0.1.0',
    license = 'MIT',
    description = 'Hashing, symmetric encryption, and asymmetric encryption functions.',
    long_description = ''.join(open('README.md', encoding='utf-8').readlines()),
    long_description_content_type = 'text/markdown',
    author = 'Will Allen',
    author_email = 'wkhallen@gmail.com',
    url = 'https://github.com/WKHAllen/easyencrypt',
    keywords = ['encrypt', 'decrypt', 'cryptography', 'security'],
    install_requires = ['cryptography', 'rsa'],
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Security :: Cryptography',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
