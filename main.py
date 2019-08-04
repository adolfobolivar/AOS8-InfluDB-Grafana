import auth_aos
import show_command_via_API
import controller_APs
import ap_database
import cpuload
import clients_per_ssid
import users_type
import ap_associations
import ap_statistics
import time

username='jinlin.zhou@hpe.com'
password='Newp0int'
vMM_aosip='10.0.50.10'

while True:
    #Get the token to access vMM information  -- via API
    token = auth_aos.authentication(username,password,vMM_aosip)

    #show ap database command -- via API
    command = 'show+ap+database'
    list_ap_database = show_command_via_API.show_command(vMM_aosip,token,command)['AP Database']
 
    #Adjust format of data (ap database), send info to InfluxDB: 
    ap_database.format_send_data(list_ap_database)

    #show show cpuload command -- via API
    command = 'show+cpuload'
    list_cpuload = show_command_via_API.show_command(vMM_aosip,token,command)['_data']
 
    #Adjust format of data (ap database), send info to InfluxDB: 
    cpuload.format_send_data(vMM_aosip,list_cpuload)

    #Create a list of [Controller's IP Address and APs (APs -> UP status)] 
    list_controllers_and_APs = controller_APs.list_controller_APs(list_ap_database)
    
    #For each controller 
    for d in list_controllers_and_APs:
        #Get the token to access vMC information  -- via API
        token = auth_aos.authentication(username,password,d[0].get('Switch IP'))
        
        #show ap essid  -- via API
        command = 'show+ap+essid'
        list_clients_per_SSID = show_command_via_API.show_command(d[0].get('Switch IP'),token,command)['ESSID Summary']
        
        #Adjust format of data (Clients per SSID), send info to InfluxDB: 
        clients_per_ssid.format_send_data(d[0].get('Switch IP'), list_clients_per_SSID)

        #show user-table verbose -- via API
        command = 'show+user-table+verbose'
        list_users_type = show_command_via_API.show_command(d[0].get('Switch IP'),token,command)['Users']
        
        #Adjust format of data (Clients per SSID), send info to InfluxDB: 
        users_type.format_send_data(d[0].get('Switch IP'), list_users_type)

        #For each controller -> For each AP 
        for AP in d[1].get('APs'):
            
            #show ap association ap-name <AP Name>  -- via API
            command = 'show+ap+association+ap-name' + ' '+AP
            list_associations_per_ap = show_command_via_API.show_command(d[0].get('Switch IP'),token,command)['Association Table']
            
            #Adjust format of data (associations per AP), send info to InfluxDB: 
            ap_associations.format_send_data(list_associations_per_ap, AP)
            
            #show ap debug radio-stats ap-name <AP Name> radio  -- via API
            command = 'show+ap+debug+radio-stats+ap-name+'+AP+'+radio+0'
            list_ap_statistics_per_radio = show_command_via_API.show_command(d[0].get('Switch IP'),token,command)['RADIO Stats']
            
            #Adjust format of data (statistics per AP per radio), send info to InfluxDB: 
            ap_statistics.format_send_data(list_ap_statistics_per_radio, AP, 0)
            
            #show ap debug radio-stats ap-name <AP Name> radio 1  -- via API
            command = 'show+ap+debug+radio-stats+ap-name+'+AP+'+radio+1'
            list_ap_statistics_per_radio = show_command_via_API.show_command(d[0].get('Switch IP'),token,command)['RADIO Stats']
            
             #Adjust format of data (statistics per AP per radio), send info to InfluxDB: 
            ap_statistics.format_send_data(list_ap_statistics_per_radio, AP, 1)

    time.sleep(60)
