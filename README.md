## Poslugon is based on Python3.5 and Flask framework
### INSTALLING 
#### Base installing OSX Sierra:
1. install xcode from market
2. install homebrew:
    * ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"
3. install python
    * brew install python3.5
4. install postgresql (9.6)
    * brew update
    * brew install postgres
5. run postgres server manually
    * postgres -D /usr/local/var/postgres
6. create database Poslugon:
    * createdb 'Poslugon'
    * psql -U your_username Poslugon
7. install postgresql admin pack to use UI editor
    * psql user_name -c 'CREATE EXTENSION "adminpack";'
8. configure postgresql to start automatically
    * mkdir -p ~/Library/LaunchAgents
    * ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents
    * launchctl load ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
9. install psycopg2
    * pip3 install psycopg2<br>
    \#If you have troubles with installing it via pip,
    <br>\#you can try to install it via port
        * download and install port package from [here](https://www.macports.org/install.php)
        * sudo port install py35-psycopg2
