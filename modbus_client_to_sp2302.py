# modbus_client_to_sp2302.py

from pymodbus.client.sync import ModbusTcpClient
import time

# --- Configuration ---
SP2302_IP = '192.168.2.50'  # Replace with SP2302 IP address
PORT = 502                  # Default Modbus TCP port
UNIT_ID = 1                 # Modbus slave/unit ID
REGISTER_ADDRESS = 0        # Start address to read/write
REGISTER_COUNT = 2          # Number of registers to read

def read_registers(client):
    result = client.read_holding_registers(REGISTER_ADDRESS, REGISTER_COUNT, unit=UNIT_ID)
    if result.isError():
        print("[!] Failed to read registers")
    else:
        print(f"[✓] Read Registers: {result.registers}")

def write_registers(client, values):
    result = client.write_registers(REGISTER_ADDRESS, values, unit=UNIT_ID)
    if result.isError():
        print("[!] Failed to write registers")
    else:
        print(f"[>] Wrote Registers: {values}")

def main():
    client = ModbusTcpClient(SP2302_IP, port=PORT)
    if not client.connect():
        print(f"[X] Could not connect to SP2302 at {SP2302_IP}:{PORT}")
        return

    print("[✓] Connected to SP2302 Modbus TCP")

    # Write values to SP2302
    write_values = [100, 200]
    write_registers(client, write_values)

    # Read back the same registers
    time.sleep(1)
    read_registers(client)

    client.close()
    print("[*] Connection closed")

if __name__ == "__main__":
    main()
