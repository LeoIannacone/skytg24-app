import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "skytg24-app",
    version = "0.0.1",
    author = "Leo Iannacone",
    author_email = "l3on@ubuntu.com",
    description = ("Un semplice client per Sky TG24"),
    license = "GPLv3",
    keywords = "sky tg informazione",
    url = "https://github.com/LeoIannacone/skytg24-app",
    packages=['skytg24-app',],
    long_description=read('README'),
)
