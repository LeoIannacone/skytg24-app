import os, sys
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def create_desktop():
    # Read in myapp.desktop.in template file
    infile = open(os.path.join('data', 'skytg24.desktop.in'))
    # Replace all @PREFIX@ with prefix defined by sys.prefix
    data = infile.read().replace('@PREFIX@', sys.prefix)
    infile.close()

    # Create the updated myapp.desktop file
    outfile = open(os.path.join('data', 'skytg24.desktop'), 'w')
    outfile.write(data)
    outfile.close()

create_desktop()

setup(
    name = "Sky TG24 App",
    version = "0.0.1",
    author = "Leo Iannacone",
    author_email = "l3on@ubuntu.com",
    description = ("Un semplice client per Sky TG24"),
    license = "GPLv3",
    keywords = "sky tg informazione",
    url = "https://github.com/LeoIannacone/skytg24-app",
    long_description=read('README.md'),
    
    scripts = ['skytg24-app/skytg24'],
    
    data_files=[
        ('share/skytg24-app', ['README.md', ]), # 'Changelog', 'Authors']),
        ('share/applications', ['data/skytg24.desktop']),
        ('share/icons', ['data/skytg24-256.png']),
        ('share/man/man1', ['man/skytg24.1']),
    ],
)
