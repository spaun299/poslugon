<h2>**Poslugon is based on Python3.5 and Flask framework**</h2>
<h3>**_INSTALLING_**:</h3>
<h4>**Base installing OSX Sierra:**

1: install xcode from market
<br>
2: install homebrew:
<br>
ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"
<br>
3: install python
<br>
brew install python3.5
<br>
4: install postgresql (9.6)
<br>
brew update
brew install postgres
<br>
5: run postgres server manually
<br>
postgres -D /usr/local/var/postgres
<br>
6: create database Poslugon:
<br>
createdb 'Poslugon'
psql -U your_username Poslugon
<br>
7: install postgresql admin pack to use UI editor
<br>
psql user_name -c 'CREATE EXTENSION "adminpack";'
<br>
8: configure postgresql to start automatically
<br>
mkdir -p ~/Library/LaunchAgents
ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
<br>
9: install psycopg2
<br>
pip3 install psycopg2
If you have troubles with installing it via pip,
you can try to install it via port
download and install port package from here
https://www.macports.org/install.php
sudo port install py35-psycopg2
<br>
