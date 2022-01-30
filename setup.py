from setuptools import setup, find_packages

setup(
    name='pyqt-toast',
    version='0.2.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt Toast (Small message displayed on the screen, visible for a short time)',
    url='https://github.com/yjg30737/pyqt-toast.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)