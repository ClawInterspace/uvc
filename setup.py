from setuptools import setup, find_packages

setup(
    name='uvc',
    version='1.0.3',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    package_data={'uvc': ['logging.ini']},
    install_requires=['click==7.1.2', 'colorama==0.4.4'],
    url='https://github.com/ClawInterspace/uvc',
    license='MIT',
    author='ClawInterspace',
    author_email='alanliu71104@gmail.com',
    description='For universal version control tool'
)
