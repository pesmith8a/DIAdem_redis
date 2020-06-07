# DIAdem_redis
Interacting with Redis from DIAdem

Just why did I make this: 
DIAdem is very good at processing large data files from NI equipment, and to also benfit from My Datafinder or DataFinder Server to search through a large group of files.   
What DIAdem has problems doing is to communicate to other applications like R, Julia, Python. DIAdem also allows using up to 5 cores of a Machine, by the use of Worker objects.  In my use of Worker objects, I have found that communicating to workers or between workers was quite challenging and lacking ease of use.  
What I was looking for what being able to use Asynchronous data structures like Queue or Stacks. 
To be ale to store large amount of data, and to use Json encoded strings so can store complex objects like Dictionaries or Arrays of Dictionaries into these queues and stacks.   Redis allow this type of Asynchronous and large amount of storage. Redis is also an in memory networked data store, and in my work with Redis in DIAdem, the time cost to do one Command to Redis is under 5 ms. 
What this has allowed:
This level of speed has allowed using Redis a logging system 
Using Redis as a way to transfer instructions between one Master instance of DIAdem to multiple Worker instances
Using Redis a a way to allow interaction between Python, R and Julia, where the needed function is more suited to other language than DIAdem.
Allows using DIAdem from R, Python and Julia, when DIAdem has features that are useful/productive.

This code will allow full interaction with Redis DataStore from NI DIAdem.  It works with DIAdem 2018, 2019 and 2020.  It is calling Python code, so it requires install of python and the package Redis from Python.org 

In this Example code in

Install:   For my install I add installed Python 3.6.5 to c:/python/python365 and instructed the installer to the windows Path so that when in Command window can run  python --version and will return with version 3.6.5.
The Redis package is installed by issuing the Command line   python -m redis

Install of Redis for Windows ( Used MSOpenTech version)  
at  https://github.com/ServiceStack/redis-windows
For my install I did left the install to be only local host. so when prompted to open firewall, Declined to open firewall.

Once python, Python package are installed, should be able in windows Command window to enter  
1) Enter Python
2) Enter import redis as rd
This should give no errors if the package and python and redis package is installed correctly.

To verify redis install.  In the Redis install directory, will find a command called redis-cli.exe
Open a Windows Command window,and enter  redis-cli.exe. 
1) Enter  info  
  Should allow viewing of multiple configurations issues for your installation.
2) Enter  set hw  "hello World"
3) Enter  get hw
4) Enter keys *  
These commands should result in posting a string to the key "hw"  of "hello World"  
The get hw command should allow retrieval of "Hello World" string that is stored in the key "hw"
The keys command will show you all the currnet keys in the Redis datastore instance.


Now that Python, Python redis package
