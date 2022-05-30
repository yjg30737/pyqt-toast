import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='pyqt-toast',
    version='0.0.14',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_toast.style': ['background.css', 'foreground.css']},
    description='PyQt Toast (Small message displayed on the screen, visible for a short time)',
    url='https://github.com/yjg30737/pyqt-toast.git',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper>=0.0.1'
    ]
)