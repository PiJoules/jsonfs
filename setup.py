from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='jsonfs',
    packages=['jsonfs'],  # this must be the same as the name above
    version='0.0.1',
    description='A random test lib',
    author='Peter Downs',
    author_email='peterldowns@gmail.com',
    url='https://github.com/PiJoules/jsonfs',  # use the URL to the github repo
    download_url='https://github.com/peterldowns/mypackage/tarball/0.1',  # I'll explain this in a second
    keywords=['testing', 'logging', 'example'],  # arbitrary keywords
    classifiers=[],
    ext_modules=cythonize("jsonfs.pyx"),
)

