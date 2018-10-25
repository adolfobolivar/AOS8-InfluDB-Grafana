#Adjust format of data, send info to InfluxDB: 

import time
import datetime
import write_influxdb

def format_send_data(vMM,data):
    db_data= list()
    now = datetime.datetime.today()
    
    data = data[0].split(', ')

    for d in data:
        if d.startswith('idle') == True:
            data = d.lstrip('idle ')
            break
    
    d = data.strip('%')
    field = round (100 - float(d),1) 

    db_data = [ 
                { 
                    'measurement':'cpuload',
                    'tags':{'Switch IP':vMM},
                    'time':int(now.strftime('%s')),
                    'fields': {'Status':field}
                }
            ]
    write_influxdb.write_data_db(db_data)