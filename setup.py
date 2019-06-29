try:
    from setuptools import setup,find_packages
except ImportError:
    from distutils.core import setup,find_packages

sdict = {
    'name' : 'py_experiment',
    'version' : 1.0,
    'packages' : ['src'],
    'entry_points' : {
        'console_scripts' : [
            'exp = src.com.tgl.exp.exp:main'],
    },

}

sdict['packages'] = find_packages()



setup(**sdict)