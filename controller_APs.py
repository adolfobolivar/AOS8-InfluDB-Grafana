#Extract [Controller's IP Address and APs]: 

def list_controller_APs(data):

    data_AP_vMC = list()
    data_IP_vMC = list()
    data_AP_vMC_list = list()

    #Extract Controller's IP address
    for controller in data:
        data_IP_vMC.append(controller.get('Switch IP'))

    #Remove duplicate Controller's IP address in list
    data_IP_vMC = list(set(data_IP_vMC)) 

    #Create list [Controller, APs]
    for value in data_IP_vMC:
        data_AP_vMC.clear()
        for i in data:
            if value == i.get('Switch IP'):
                 if i.get('Status').startswith('Up') == True:
                    data_AP_vMC.append(i.get('Name'))   
    
        data_AP_vMC_list.append([{'Switch IP':value},{'APs':data_AP_vMC.copy()}])
    
    return (data_AP_vMC_list)

