def battery_is_ok(temperature, soc, charge_rate):
    return(check_tepmerature(temperature) and check_soc(soc) and check_charge_rate(charge_rate))
       
def check_tepmerature(temperature):
    if ( 0 >temperature or temperature> 45):
        print_text('Temperature is out of range!')
        return False
    else:
       return True
      
def check_soc(soc):
    if ( 20 > soc or soc > 80):
        print_text('State of Charge is out of range!')
        return False
    else:
        return True
        
def check_charge_rate(charge_rate):
    if charge_rate >0.8:
        print_text('Charge rate is out of range!')
        return False
    else:
        return True
        
def print_text(text):
    print(text)

if __name__ == '__main__':
    assert(check_tepmerature(1) is True)
    assert(check_tepmerature(45)is True)
    assert(check_tepmerature(46)is False)
    assert(check_tepmerature(-1)is False)
    assert(check_soc(20)is True)
    assert(check_soc(19)is False)
    assert(check_soc(80)is True)
    assert(check_soc(81)is False)
    assert(check_charge_rate(0.9)is False)
    assert(check_charge_rate(0.8)is True)
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
