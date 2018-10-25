#Adjust format of data, send info to InfluxDB: 

import time
import datetime
import write_influxdb

def format_send_data(data):
    db_data= list()
    now = datetime.datetime.today()
        
    for d in data:
        if d.get('Status').startswith('Up') == True:
            field = 1
        else:
            field = 0
        
        db_data = [ 
                    { 
                        'measurement':'Status_of_APs',
                        'tags':{'Switch IP':d.get('Switch IP'),'Name':d.get('Name')},
                        'time':int(now.strftime('%s')),
                        'fields': {'Status':int(field)}
                    }
                 ]
        write_influxdb.write_data_db(db_data)