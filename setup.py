# -*- coding: utf-8 -*-

from os.path import join
from setuptools import setup, find_packages

version = '0.1'
name = 'menhir.contenttype.photoalbum'

history = open(join('docs', 'HISTORY.txt')).read()
readme = open(
    join('src', 'menhir', 'contenttype', 'photoalbum', 'README.txt')).read()

setup(name = name,
      version = version,
      description = 'Dolmen contenttype extension : photoalbum',
      long_description = readme + '\n\n' + history,
      keywords = 'Grok Zope3 CMS Dolmen',
      author = 'Souheil Chelfouh',
      author_email = 'trollfot@gmail.com',
      url = 'http://tracker.trollfot.org/',
      download_url = '',
      license = 'GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages = ['menhir', 'menhir.contenttype'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      install_requires=[
          'dolmen.app.viewselector',
          'dolmen.content',
          'grokcore.component',
          'hurry.jquery',
          'megrok.resource',
          'menhir.contenttype.image',
          'setuptools',
          'zope.component',
          'zope.intid'
          ],
      classifiers = [
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Grok',
          'Intended Audience :: Other Audience',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
      )
