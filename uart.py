import serial
import time
import sys

def serial_read(port, baud_rate, timeouts):
    ser = serial.Serial(port, baud_rate,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=timeouts)
    
    print(f"UART {port} opened! bps {baud_rate}.")
    print("Start Reading, input 'CTRL-C' to exit...")

    data = ""
    try:
        while True:
            data = ser.readline()
            print(data)
            ser.write(data.encode('utf-8'))
            data = ""
    except KeyboardInterrupt:
        print("Interrupted by user！")
    finally:
        ser.close()
        print("UART {} closed!".format(port))
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        port_name = "/dev/ttyMH2"
        print("Using UART {} as default!".format(port_name))
    else:
        port_name = sys.argv[1]
    baud_rate = 9600
    serial_read(port_name, baud_rate, None)
