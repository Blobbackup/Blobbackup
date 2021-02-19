import re

from setuptools import setup, Extension

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    license="GPLv3",
    name="blobbackup",
    version="1.0.0.beta3",
    author="Bimba Shrestha",
    packages=["blobbackup"],
    include_package_data=True,
    long_description=long_descr,
    long_description_content_type="text/markdown",
    ext_modules=[Extension('chunker', ["blobbackup/chunker.pyx"])],
    description="A secure, efficient and powerful backup tool.",
    entry_points={
        "console_scripts": ['blobbackup = blobbackup.application:main']
    },
    setup_requires=['setuptools>=18.0', "cython"],
    install_requires=[
        'pyside2', 'azure-storage-blob', 'google-cloud-storage', 'boto3 ',
        'zstd', 'pycryptodome==3.9.7', 'retry', 'b2sdk', 'apscheduler',
        'pyinstaller', 'keyring', 'pysftp', 'google-api-python-client==1.8',
        'google-auth-oauthlib', 'cython', 'randomFileTree', 'mkdocs'
    ],
)