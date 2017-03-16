#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
version = '2.0'
setup(name='ceph-request',
      version=version,
      description="ceph cmd tool to send rest http request to rgw",
      long_description="""ceph cmd tool to send rest http request to rgw""",
      classifiers=[],
      keywords='python ceph radosgw',
      author='wzyuliyang',
      author_email='wzyuliyang911@gmail.com',
      url='https://github.com/wzyuliyang/ceph-request',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'requests-toolbelt',
	    'requests',
        'docopt',
      ],
      entry_points={
        'console_scripts':[
            'ceph-request = ceph_request.ceph_request:main'
        ]
      },
)
