#Adjust format of "show user-table verbose" data, send info to InfluxDB: 

import time
import datetime
import write_influxdb

def format_send_data(MC,data):
    db_data= list()
    AP_name_data = list()
    user_type_data = list()
    data_ordered = list()

    #Extract AP names and user types 
    for AP_name_user_type in data:
        AP_name_data.append(AP_name_user_type.get('AP name'))
        user_type_data.append(AP_name_user_type.get('Type'))

    #Remove duplicate AP names and user types in list
    AP_name_data = list(set(AP_name_data)) 
    user_type_data = list(set(user_type_data)) 
    #print(user_type_data)
    
    now = datetime.datetime.today()

    count_android = 0
    count_ipad = 0
    count_OSX = 0

    for ap in AP_name_data: 
        for d in data:
            if d.get('AP name') == ap:
                if d.get('Type') == 'Android':
                    count_android += 1
                if d.get('Type') == 'iPad':
                    count_ipad += 1
                if d.get('Type') == 'OS X':
                    count_OSX += 1
                
        data_ordered.append([{'Switch IP':MC,'AP name':ap,'Android':count_android,'iPad':count_ipad,'OS X':count_OSX}])
        count_android = 0
        count_ipad = 0
        count_OSX = 0

    for d in data_ordered:
        db_data = [ 
                    { 
                        'measurement':'type_users',
                        'tags':{'Switch IP':MC,'AP name':d[0].get('AP name')},
                        'time':int(now.strftime('%s')),
                        'fields': {'Android':int(d[0].get('Android')),'iPad':int(d[0].get('iPad')),'OS X':int(d[0].get('OS X'))}
                    }
                 ]
        write_influxdb.write_data_db(db_data)