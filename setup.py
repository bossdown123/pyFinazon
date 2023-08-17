from setuptools import setup, find_packages

setup(
    name='pyFinazon',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'datetime',
        'pandas',
    ],
    author='Adam',
    author_email='adamvibeo@gmail.com',
    description='finazon wrapper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bossdown123/pyFinazon',  # URL to your GitHub repository
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
