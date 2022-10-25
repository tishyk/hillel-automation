#!/usr/bin/env python
from setuptools import find_packages, setup


def main():
    setup(
        name='test_utils',
        version='0.0.1',
        description='Tests Repository Utils',
        url='https://your_blog_web_page',
        author='Cool Team',
        author_email='sytischenko@gmail.com',
        packages=find_packages(),
        package_dir={'test_utils': 'test_utils',
                     'records': 'records',
                     'pages': 'pages',
                     'data': 'data',
                     'sites': 'sites'},
        zip_safe=False,
        include_package_data=True,
    )


if __name__ == '__main__':
    main()
