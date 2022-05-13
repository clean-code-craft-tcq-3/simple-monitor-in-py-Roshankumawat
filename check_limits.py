def battery_is_ok(temperature, soc, charge_rate):
    return(check_temperature(temperature) and check_soc(soc) and check_charge_rate(charge_rate))
       
def check_temperature(temperature):
    check_lower_threshold_limit(0,45,temperature)
    check_upper_threshold_limit(45, temperature)
    if ( 0 >temperature or temperature> 45):
        print_text('Temperature is out of range!')
        return False
    else:
       return True
      
def check_soc(soc):
    check_lower_threshold_limit(20, 80, soc)
    check_upper_threshold_limit(80, soc)
    if ( 20 > soc or soc > 80):
        print_text('State of Charge is out of range!')
        return False
    else:
        return True
        
def check_charge_rate(charge_rate):
    check_lower_threshold_limit(0,0.8, charge_rate)
    check_upper_threshold_limit(0.8, charge_rate)
    if charge_rate >0.8:
        print_text('Charge rate is out of range!')
        return False
    else:
        return True
        
def print_text(text):
    print(text)

def check_lower_threshold_limit(lower_limit, upper_limit, value):   
    if((value<=(lower_limit+(upper_limit*5)/100) and value>=lower_limit)):
        print_text('Warning: Approaching discharge') 

def check_upper_threshold_limit(upper_limit, value):
    if((value>=(upper_limit-(upper_limit*5)/100) and value<=upper_limit)):
        print_text('Warning: Approaching charge-peak')
     
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
