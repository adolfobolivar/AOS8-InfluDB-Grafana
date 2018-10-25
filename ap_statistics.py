#Adjust format of data, send info to InfluxDB: 

import time
import datetime
import write_influxdb

def format_send_data(data, AP, radio):
    db_data= list()
    now = datetime.datetime.today()

    if radio == 0:
        radio = '5Ghz' 
    
    else:
        radio = '2.4Ghz'

    #Rx Data Bytes: Number of data bytes received.
    for d in data:
        if d.get('Parameter') == 'Rx Data Bytes':
            tag1 = d
            break
    
    #Tx Data Bytes Transmitted: Total data bytes received by an AP from its wired interface to be transmitted over the air.
    for d in data:
        if d.get('Parameter') == 'Tx Data Bytes Transmitted':
            tag2 = d
            break

    #Cyclic Redundancy Check (CRC) is a data sequence that is sent with a frame to help verify if all the data received correctly.
    for d in data:
        if d.get('Parameter') == 'Rx CRC Errors':
            tag3 = d
            break

    db_data = [ 
                    { 
                        'measurement':'Bandwidth_Consumed_CRCs',
                        'tags':{'Name':AP,'Radio':radio},
                        'time':int(now.strftime('%s')),
                        'fields': {'Rx Data Bytes':int(tag1.get('Value')),'Tx Data Bytes Transmitted':int(tag2.get('Value')),'Rx CRC Errors':int(tag3.get('Value'))}
                    }
                 ]
    write_influxdb.write_data_db(db_data)