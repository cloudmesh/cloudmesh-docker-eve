Cloudmesh extdocker
==============

An dynamically extensible CMD5 based command shell to manager single docker instances and also docker swarm

Requirements
------------

* Python 2.7.13

Installation from source
------------------------

Setup a virtualenv either with virtualenv or pyenv.

virtualenv::

    virtualenv ~/ENV2

pyenv::

    pyenev virtualenv 2.7.13 ENV2

Now you need to get two source directories. We assume yo place them in
~/github::

    mkdir ~/github
    cd ~/github
    git clone https://github.com/cloudmesh/common.git
    git clone https://github.com/cloudmesh/cmd5.git
    git clone https://github.com/cloudmesh/extdocker.git

The cmd5 repository contains the shell, while the extdocker directory
contains the commands docker and swarm.

To install them simply to the following::

    cd ~/github/common
    python setup.py install
    cd ~/github/cmd5
    python setup.py install
    cd ~/github/extdocker
    python setup.py install

Execution
---------

to run the shell you can activate it with the cms command. cms stands
for cloudmesh shell::

    (ENV2) $ cms

It will print the banner and enter the shell::

    +-------------------------------------------------------+
    |   ____ _                 _                     _      |
    |  / ___| | ___  _   _  __| |_ __ ___   ___  ___| |__   |
    | | |   | |/ _ \| | | |/ _` | '_ ` _ \ / _ \/ __| '_ \  |
    | | |___| | (_) | |_| | (_| | | | | | |  __/\__ \ | | | |
    |  \____|_|\___/ \__,_|\__,_|_| |_| |_|\___||___/_| |_| |
    +-------------------------------------------------------+
    |                  Cloudmesh CMD5 Shell                 |
    +-------------------------------------------------------+

    cms>


To see the list of commands you can say::

    cms> help

To see the manula page for a specific command, please use::

    help COMMANDNAME

Extension
---------

One of the most important features of CMD5 is its ability to extend it
with new commands.  This is done via packaged name spaces. This is
defined in the setup.py file of your enhancement. 

