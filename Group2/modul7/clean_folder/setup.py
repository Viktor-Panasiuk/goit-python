from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
    version='1.0',
    description='Script for sorted files',
    author='Viktor Panasjuk',
    author_email='vo151184pvv@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    include_package_data=True,
    entry_points={'console_scripts':['clean-folder = clean_folder.clean:clean_f']})