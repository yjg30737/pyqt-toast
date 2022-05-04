from setuptools import setup, find_packages

setup(
    name='pyqt-toast',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_toast.style': ['background.css', 'foreground.css']},
    description='PyQt Toast (Small message displayed on the screen, visible for a short time)',
    url='https://github.com/yjg30737/pyqt-toast.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
    ]
)