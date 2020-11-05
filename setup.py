from setuptools import setup, find_packages

setup(
    name='uvc',
    version='1.0.0',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    package_data={'uvc': ['logging.ini']},
    url='https://github.com/ClawInterspace/uvc',
    license='MIT',
    author='ClawInterspace',
    author_email='alanliu71104@gmail.com',
    description='For universal version control tool'
)
