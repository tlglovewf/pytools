import mysql.connector as mc
import json
from dataclasses import dataclass
from base64 import b64decode


@dataclass
class DwLog:
    id = 0
    userid = 1
    dwsttime = 2
    dwedtime = 3
    mufactor = 4
    pjnm = 5
    params = 6


mydb = mc.connect(host='10.60.151.254', user='root', passwd='cjbdata2020',
                  auth_plugin='mysql_native_password')


myc = mydb.cursor()

try:
    myc.execute("select * from vrs.user_download_log order by id desc")
   
    one = myc.fetchone()

    """eval(str->dict)"""
    #jstr = eval(str(b64decode(one[DwLog.params]),'UTF-8'))
    rst = json.loads(str(b64decode(one[DwLog.params]),'UTF-8'))
    print(rst)
    jrst = json.dumps(rst,indent=4)

    print(jrst)
except mc.errors.DatabaseError:
    print("get except")
except:
    print("unknown error.")
finally:
    mydb.close()
