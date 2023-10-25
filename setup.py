from setuptools import setup

setup(
   name='toggl_track_api_wrapper',
   version='0.1',
   description='A useful module',
   author='Ghodot',
   author_email='foomail@foo.example',
   packages=['toggl_track_api_wrapper'],  #same as name
   install_requires=['wheel', 'requests'], #external packages as dependencies
)