import re
#import googletrans
from googletrans import Translator
translator = Translator()

def battery_is_ok(temperature, soc, charge_rate):
    return(check_temperature(temperature) and check_soc(soc) and check_charge_rate(charge_rate))
       
def check_temperature(temperature):
    temperature= get_value_from_feature(temperature, 'Temperature')
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
        print_text(translator.translate('Warning: Approaching charge-peak', dest='de'))
        print_text('Warning: Approaching charge-peak')
        
def get_unit_from_feature(feature_value, feature):
    return re.sub('[0-9]',"", feature_value)
    
def get_value_from_feature(feature_value, feature):
    return int(re.sub('[A-Za-z]',"", feature_value))
    
def print_text(text):
    print(text)
    print(translate_warning(text, 'de'))
          
def translate_warning(text, language):
    translated_text= translator.translate( text,  src='en', dest=language)
    return(translated_text)
    
if __name__ == '__main__':
    
    assert(get_unit_from_feature('20F', 'Temperature')=='F')
    assert(get_value_from_feature('20C', 'Temperature') == 20)
    assert(check_temperature('1F') is True)
    assert(check_temperature('45C')is True)
    assert(check_temperature('46C')is False)
    assert(check_temperature('-1C')is False)
    assert(check_soc(20)is True)
    assert(check_soc(19)is False)
    assert(check_soc(80)is True)
    assert(check_soc(81)is False)
    assert(check_charge_rate(0.9)is False)
    assert(check_charge_rate(0.8)is True)
    assert(battery_is_ok('25F', 70, 0.7) is True)
    assert(battery_is_ok('50C', 85, 0) is False)
