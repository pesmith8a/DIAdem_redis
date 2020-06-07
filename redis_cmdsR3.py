#! python

import os, sys
import win32com.client
import numpy as np
import DIAdem
import redis
import base64
import json

# Verify that the passed in parameters are correct. 

dd = DIAdem.Application                                        # Get access to all DIAdem identifers

python_redis_ip      = dd.python_redis_ip
python_redis_port    = dd.python_redis_port
python_redis_cmd     = dd.python_redis_cmd
python_redis_key     = dd.python_redis_key
python_redis_value   = dd.python_redis_value
python_redis_param1  = dd.python_redis_param1
python_redis_param2  = dd.python_redis_param2
python_redis_db      = dd.python_redis_db
#python_redis_cmdlist = dd.python_redis_cmdlist
#python_redis_guid    = dd.python_redis_guid
#python_redis_resultsPath = dd.python_redis_resultsPath

python_redis_cmd = python_redis_cmd.lower().strip()

def redis_call(sip, iport, idb, scmd, skey, svalue, sparam1,sparam2):
  r = redis.Redis(host=sip, port=iport, db=idb)
  # python_redis_cmd="get"
  sResult = ""
  if (scmd == 'lpush'):
    try:
      retval = r.lpush(skey, svalue)
      sResult = str(retval)
      bStatus = True
    except:
      sResult = "ERROR"
      bStatus = False
      pass

  elif (scmd == 'lpop'):
    try:
      retval = r.lpop(skey)
      sResult = "".join(map(chr, retval))
      bStatus = True

    except:
      sResult = "ERROR"
      bStatus = False
      pass
  elif (scmd == 'ltrim'):
    try:
      retval = r.ltrim(skey, sparam1, sparam2)
      sResult = str(retval)
      bStatus = True
    except:
      sResult = "ERROR"
      bStatus = False
      pass

  elif (scmd == 'llen'):
    try:
      retval = r.llen(skey)
      sResult = str(retval)
      bStatus = True
    except:
      bStatus = False
      sResult = "0"
      pass
  elif (scmd == 'rpop'):
    try:
      retval = r.rpop(skey)
      sResult = "".join(map(chr, retval))
      bStatus = True
    except:
      sResult = "ERROR"
      bStatus = False
      pass

  elif (scmd == 'rpush'):
    try:
      retval = r.rpush(skey, svalue)
      sResult = str(retval)
      bStatus = True
    except:
      sResult = "ERROR"
      bStatus = False
      pass

  elif (scmd == 'del'):
    try:
      retval = r.delete(skey)
      sResult = str(retval)
      bStatus = True
    except:
      sResult = "ERROR"
      bStatus = False
      pass

  elif (scmd == 'flushall'):
    try:
      retval = r.flushall()
      sResult = str(retval)
      bStatus = True
    except:
      sResult = "ERROR"
      bStatus = False
      pass

  elif (scmd == 'set'):
    try:
      retval = r.set(skey, svalue)
      sResult = str(retval)
      bStatus = True
    except:
      sResult = "ERROR"
      bStatus = False
      pass

  elif (scmd == 'get'):
    try:
      retval = r.get(skey)
      sResult = "".join(map(chr, retval))
      bStatus = True
    except:
      sResult = "ERROR"
      bStatus = False
      pass
  elif (scmd == 'incr'):
    try:
      retval = r.incr(skey)
      sResult = str(retval)
      bStatus = True
    except:
      sResult = "ERROR"
      bStatus = False
      pass
  elif (scmd == 'incrby'):
    try:
      retval = r.incrby(skey,svalue)
      sResult = str(retval)
      bStatus = True
    except:
      sResult = "ERROR"
      bStatus = False
      pass
  elif (scmd == 'keys'):
    list01 = list()

    try:
      retval = r.keys(skey)

      for i, val in enumerate(retval):
        list01.append("".join(map(chr, val)))

      sResult = json.dumps(list01)
      bStatus = True
    except:
      sResult = "ERROR"
      bStatus = False
      pass

  elif (scmd == 'exists'):
    try:
      retval = r.exists(skey)
      if (retval == 0):
        sResult = "false"
      elif (retval == 1):
        sResult = "true"

      bStatus = True
    except:
      sResult = "ERROR"
      bStatus = False
      pass

  elif (scmd == 'ping'):
    try:
      retval = r.ping()
      if (retval):
        sResult = "true"
      else:
        sResult = "false"
      bStatus = True
    except:
      sResult = "false"
      bStatus = False
      pass

  elif (scmd == 'type'):
    try:
      retval = r.type(skey)
      sResult = "".join(map(chr, retval))
      bStatus = True

    except:
      sResult = "ERROR"
      bStatus = False

  if (bStatus):
    sRetVal = "true"
  else:
    sRetVal = "false"

  return (sResult, sRetVal)

  # print("sResult:"+ sResult)
  # print ("bStatus" + " ")

(sResults, sStatus) = redis_call(python_redis_ip, python_redis_port, python_redis_db, python_redis_cmd,python_redis_key, python_redis_value,python_redis_param1,python_redis_param2)
#print(sResult)
#print (sRetVal)
#print ("Print test")

dd.python_redis_dict.Add("status", sStatus)
dd.python_redis_dict.Add("results", sResults)
#~~~~~~~~~~~~~~~~~~~~~~~