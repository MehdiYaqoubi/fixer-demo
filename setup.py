from setuptools import setup


setup(name='fixer-demo',
      version='0.2',
      description='Fixer service demo package',
      url='https://github.com/MehdiYaqoubi/fixer-demo.git',
      author='Mehdi Yaqoubi',
      author_email='mehdi.code@pm.me',
      license='MIT',
      packages=['fixer'],
      install_requires=['requests'],
      zip_safe=False)
