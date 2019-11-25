try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='urop_assessment_answers',
    version='1.0',
    description='assessment for potential UROP students',
    url='https://github.com/carismoses/urop_assessment_answers',
    author='Caris Moses',
    author_email='carism@mit.edu',
    packages=[],
    python_requires='>=3.6',
    dependency_links=[
        'odio_urdf @ http://github.com/hauptmech/odio_urdf/tarball/master#egg=odio_urdf'
    ],
    install_requires=[
         'pybullet>=2.5.7',
         'jupyter>=1.0.0',
         'catkin_pkg',
         'numpy'
    ]
)
