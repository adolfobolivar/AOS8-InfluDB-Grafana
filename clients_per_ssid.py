#Adjust format of 'show+ap+essid' data, send info to InfluxDB: 

import time
import datetime
import write_influxdb

def format_send_data(MC,data):
    db_data= list()
    now = datetime.datetime.today()
    
    for d in data:
        db_data = [ 
                    { 
                        'measurement':'Number_Clients_SSID',
                        'tags':{'Switch IP':MC,'ESSID':d.get('ESSID')},
                        'time':int(now.strftime('%s')),
                       'fields': {'Clients':int(d.get('Clients'))}
                    }
                 ]
        write_influxdb.write_data_db(db_data)