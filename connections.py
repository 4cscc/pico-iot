import network
from configs import network_configs
import utime

# wifi 

class Networker:
    def __init__(self): self._connection = None
    
    @set_timeout(10)
    def establish_connection(self):
        try:
            wlan = network.WLAN(network.STA_IF)
            wlan.active(True)
            time.sleep_ms(100)
            wlan.connect(network_configs.wifi.SSID, network_configs.wifi.PASSWORD)
            
            while wlan.isconnected() is not True:
                time.sleep_ms(500)
                
            return wlan
        
        except Exception as e:
            raise e #("Unable to establish wireless network connection.")
        
        
    @property
    def connection(self):
        if self._connection is None:
            self.establish_connection()
        return self._connection

# mqtt

# I2C