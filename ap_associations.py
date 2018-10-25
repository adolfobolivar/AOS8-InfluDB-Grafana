
import time
import datetime
import write_influxdb

def format_send_data(data, AP):
    field = len(data)
    db_data= list()
    now = datetime.datetime.today()

    db_data = [ 
                    { 
                        'measurement':'Number_Associations_APs',
                        'tags':{'Name':AP},
                        'time':int(now.strftime('%s')),
                        'fields': {'Num Clients':int(field)}
                    }
                 ]
    write_influxdb.write_data_db(db_data)