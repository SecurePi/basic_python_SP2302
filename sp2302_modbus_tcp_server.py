# sp2302_modbus_tcp_server.py

from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.datastore import ModbusSequentialDataBlock
import logging
from threading import Thread
import time

# Optional: Enable debug logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

# --- Setup Data Store (Holding Registers) ---
# Initialize 10 holding registers with values 0-9
store = ModbusSlaveContext(
    hr=ModbusSequentialDataBlock(0, [i for i in range(10)])
)
context = ModbusServerContext(slaves=store, single=True)

# --- Optional: Background task to change values ---
def dynamic_register_updater():
    while True:
        # Increment holding register 0
        value = context[0x00].getValues(3, 0, count=1)[0]
        context[0x00].setValues(3, 0, [(value + 1) % 1000])
        time.sleep(5)

# Start the updater in background
Thread(target=dynamic_register_updater, daemon=True).start()

# --- Start Modbus TCP Server ---
def run_modbus_server():
    print("[✓] Modbus TCP server running on 0.0.0.0:502")
    StartTcpServer(context, address=("0.0.0.0", 502))

if __name__ == "__main__":
    run_modbus_server()

