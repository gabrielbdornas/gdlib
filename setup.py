from setuptools import setup, find_packages
import codecs
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


if __name__ == '__main__':
  # Setting up
  setup(
      name='gdlib',
      version='0.0.1.9001',
      author='Gabriel Braico Dornas',
      author_email='pagueumcafepgabriel@gmail.com',
      description="""Breve Pacote Olá Mundo criado como tutorial e futuro template boilerplate para criação de pacotes""",
      long_description_content_type='text/markdown',
      long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
      url='https://github.com/gabrielbdornas/gdlib',
      packages=find_packages(),
      install_requires=open('requirements.txt').read(),
      keywords=['python'],
      classifiers=[
          "Development Status :: 1 - Planning",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 3",
          "Operating System :: Unix",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: Microsoft :: Windows",
      ],
      entry_points="""
        [console_scripts]
        gdlib=gdlib.cli:cli
      """
  )
