import gpiod  
  
def setup_gpio_pin(chip_name, line_offset, consumer="my_app"):  
    """  
    Set the GPIO pin to output mode
  
    :param chip_name: The name of the GPIO chip
    :param line_offset: The offset of the pin on the chip (not the pin number, but the index starting from 0)
    :param consumer: The consumer name to use when requesting pins
    :return: GPIO row object 
    """  
    chip = gpiod.chip(chip_name)  
    line = chip.get_line(line_offset)  
    	
    config = gpiod.line_request()
    config.consumer = "buzzer"
    config.request_type=gpiod.line_request.DIRECTION_OUTPUT
    line.request(config, 1)  
    return line

def set_gpio_value(line, value):  
    """  
    Set the value of a GPIO pin 
  
    :param line: GPIO row object  
    :param value: The value to set (True for high level, False for low level)  
    """  
    line.set_value(value)  
  
def main():  
    # GPIO chip names and pin offsets (adjust according to your hardware and system)
    chip_name = "gpiochip0"  
    line_offset = 95  # NOTE: This is an offset, not a pin number
  
    try:  
       # Set the GPIO pin to output mode
        gpio_line = setup_gpio_pin(chip_name, line_offset)  
  
        # Set the GPIO pin to high level
        set_gpio_value(gpio_line, 1)  
        print(f"GPIO {chip_name}:{line_offset} set to High")  
  
        # Wait for a while (optional) 
        import time  
        time.sleep(1)  
  
        # Set the GPIO pin to low level
        set_gpio_value(gpio_line, 0)  
        print(f"GPIO {chip_name}:{line_offset} set to Low")  
  
    except Exception as e:  
        print(f"Error: {e}")  
  
if __name__ == "__main__":  
    main()
