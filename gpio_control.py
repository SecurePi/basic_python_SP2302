import gpiod  
  
def setup_gpio_pin(line_offset, consumer="my_app"):  
    """  
    Set the GPIO pin to output mode 
  
    :param line_offset: Pin offset on chip 
    :param consumer: The consumer name to use when requesting pins
    :return: GPIO row object
    """  
    chip = gpiod.chip("gpiochip0")  
    line = chip.get_line(line_offset)  
      
    if line.is_requested():  
        raise ValueError(f"GPIO {line_offset} is not requestable")  
    else:  
        config = gpiod.line_request()
        config.consumer = "gpio_test"
        config.request_type=gpiod.line_request.DIRECTION_OUTPUT
        line.request(config, 1)
        return line 
  
def set_gpio_value(line, value):  
    """  
    Set the value of a GPIO pin
  
    :param line: GPIO row object
    :param value: The value to set (True for high level (Turn On), False for low level (Turn Off))  
    """  
    line.set_value(value)  
  
def control_gpio(pin_number, value):  
    """  
    Control GPIO pin output high (Turn On) and low (Turn Off) level 
  
    :param pin_number: Pin number (actually should be offset)
    :param value: The value to set (True for high level (Turn On), False for low level (Turn Off))  
    """  
    try:  
        # Assuming pin_number is already the correct offset
        gpio_line = setup_gpio_pin(pin_number)  
        set_gpio_value(gpio_line, value)  
        if value:  
            print(f"GPIO {pin_number} set to High")  
        else:  
            print(f"GPIO {pin_number} set to Low")  
    except Exception as e:  
        print(f"Error controlling GPIO {pin_number}: {e}")  
  
def main(pin_number, value):  
    """  
    The main function accepts the GPIO chip name, pin number and output value as parameters 
    """  
    control_gpio(pin_number, value)  
  
if __name__ == "__main__":  
    import sys  
  
    # Get pin_number, value from command line parameters
    if len(sys.argv) != 3:  
        print("Usage: python script.py <pin_number> <value>")  
        sys.exit(1)  
    
    pin_number = int(sys.argv[1])  # Convert the pin number to an integer
    value = int(sys.argv[2]) # Convert the input high and low to integers 
  
    main(pin_number, value)
