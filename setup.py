from setuptools import setup

setup(
   name='alternate-cli',
   version='0.1',
   description='A cli tool for simple interactions with the Alternate.de online shop',
   author='FritzJo',
   author_email='fritzjo-git@mailbox.org',
   packages=['foo'],  #same as name
   install_requires=[
   'beautifulsoup4==4.9.1',
   'bs4==0.0.1',
   'certifi==2020.4.5.1',
   'chardet==3.0.4',
   'idna==2.9',
   'lxml==4.5.1',
   'requests==2.23.0',
   'soupsieve==2.0.1',
   'urllib3==1.25.9--'
   ],
)
