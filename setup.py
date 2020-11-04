from setuptools import setup, find_packages

setup(
    name='uvc',
    version='1.0.0',
    # packages=['git', 'git.custom_actions', 'utils', 'models'],
    # package_dir={'foobar': 'uvc'},
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    package_data={'uvc': ['logging.ini']},
    # Scripts=["uvc/uvc.py"],
    # data_files=[('uvc', ['uvc/logging.ini'])],
    # setup_requires=['setuptools_scm'],
    # package_dir={'': 'uvc'},
    url='https://github.com/ClawInterspace/uvc',
    license='MIT',
    author='ClawInterspace',
    author_email='alanliu71104@gmail.com',
    description='For universal version control tool'
)
