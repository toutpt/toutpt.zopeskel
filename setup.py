from setuptools import setup, find_packages
import os

version = '1.3.1'

setup(name='toutpt.zopeskel',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='oaster zopeskel',
      author='JeanMichel FRANCOIS aka toutpt',
      author_email='toutpt@gmail.com',
      url='https://github.com/toutpt/toutpt.zopeskel',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['toutpt'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'PasteScript',
          'ZopeSkel<3.0',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [paste.paster_create_template]
      toutpt_diazotheme = toutpt.zopeskel.theme:Theme
      toutpt_collective = toutpt.zopeskel.collective:Collective
      toutpt_collectivejs = toutpt.zopeskel.collectivejs:CollectiveJS
      """,
      )
