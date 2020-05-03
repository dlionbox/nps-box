from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='nps-box',
      version='0.0.1',
      description='Visual analysis of Net Promoter Score with Python 3',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=['Development Status :: In Progress',
                   'Programming Language :: Python 3'],
      url='https://github.com/dlionbox/nps-box',
      author='A. A. Scalet - dlionbox',
      author_email='aascalet@voegol.com.br',
      keywords='nps analysis net promoter score',
      packages=['nps-box'],
      install_requires=['numpy', 
                        'pandas',
                        'datetime',
                        'math',
                        'matplotlib',
                        'scipy',
                        'plotly'],
      include_package_data=True,
      zip_safe=False)