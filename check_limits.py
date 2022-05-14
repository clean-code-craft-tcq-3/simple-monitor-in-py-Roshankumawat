def battery_is_ok(temperature, soc, charge_rate):
    return(check_temperature(temperature) and check_soc(soc) and check_charge_rate(charge_rate))
       
def check_temperature(temperature):
    return check_feature_limit(0,45,temperature, 'Temperature')
      
def check_soc(soc):
    return check_feature_limit(20,80,soc, 'SOC')
        
def check_charge_rate(charge_rate):
    return check_feature_limit(0,0.8,charge_rate, 'Charge_Rate')

def check_feature_limit(lower_limit, upper_limit, feature_value, feature):
    check_lower_threshold_limit(lower_limit, upper_limit, feature_value)
    check_upper_threshold_limit( upper_limit, feature_value)
    if(feature_value<lower_limit or feature_value>upper_limit):
        print(feature,":",feature_value, "is out of range")
        return False
    else:
        return True

def check_lower_threshold_limit(lower_limit, upper_limit, feature_value):   
    if((feature_value<=(lower_limit+(upper_limit*5)/100) and feature_value>=lower_limit)):
        print_text('Warning: Approaching discharge') 

def check_upper_threshold_limit(upper_limit, feature_value):
    if((feature_value>=(upper_limit-(upper_limit*5)/100) and feature_value<=upper_limit)):
        print_text('Warning: Approaching charge-peak')
        
def print_text(text):
    print(text)
     
if __name__ == '__main__':
    assert(check_temperature(1) is True)
    assert(check_temperature(45)is True)
    assert(check_temperature(46)is False)
    assert(check_temperature(-1)is False)
    assert(check_soc(20)is True)
    assert(check_soc(19)is False)
    assert(check_soc(80)is True)
    assert(check_soc(81)is False)
    assert(check_charge_rate(0.9)is False)
    assert(check_charge_rate(0.8)is True)
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
