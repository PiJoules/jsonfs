#from distutils.core import setup
#from Cython.Build import cythonize


from distutils.core import setup
from distutils.extension import Extension

try:
    from Cython.Distutils import build_ext
except ImportError:
    use_cython = False
else:
    use_cython = True

cmdclass = {}
ext_modules = []

if use_cython:
    ext_modules += [
        Extension("jsonfs.jsonfs", ["jsonfs/jsonfs.pyx"]),
        #Extension("jsonfs", ["jsonfs.pyx"]),
    ]
    cmdclass.update({'build_ext': build_ext})
else:
    ext_modules += [
        Extension("jsonfs.jsonfs", ["jsonfs/jsonfs.c"]),
        #Extension("jsonfs", ["jsonfs.c"]),
    ]


setup(
    name='jsonfs',
    packages=['jsonfs'],  # this must be the same as the name above
    version='0.0.8',
    description='Tetsing pypi',
    author='Leonard Chan',
    author_email='lchan1994@yahoo.com',
    url='https://github.com/PiJoules/jsonfs',  # use the URL to the github repo
    #download_url='https://github.com/PiJoules/jsonfs/releases/tag/v0.0.1',
    keywords=['testing', 'logging', 'example'],  # arbitrary keywords
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Cython',
        'Topic :: Scientific/Engineering :: Mathematics',
    ],
    #ext_modules=cythonize("jsonfs/jsonfs.pyx"),
    cmdclass=cmdclass,
    ext_modules=ext_modules,
)

