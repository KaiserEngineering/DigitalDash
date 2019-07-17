"""Serial handler class."""
import serial

class Serial():

    def __init__(self):
        super(Serial, self).__init__()
        self.ser = serial.Serial(
            port='/dev/ttyAMA0',
            baudrate=57600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
	    timeout=0.25
        )
        self.ser_val = [0, 0, 0, 0, 0, 0]


    def Start(self):
        """Loop for checking Serial connection for data."""
        # Handle grabbing data
        data_line = ''
        try:
            data_line = self.ser.read(8)
        except Exception as e:
            print("Error occured when reading serial data: " + str(e))
        if ( len(data_line) < 8 ):
            print("Data packet of length: " + str(len(data_line)) + " received: " + str(data_line))
            return self.ser_val

        count = 0
        data_line = data_line.decode('utf-8')
        for val in data_line.split(';'):
            try:
                val = float(val)
                self.ser_val[count] = self.ser_val[count] + 1
                self.ser_val[count] = self.ser_val[count] % 100
                count = count + 1
            except ValueError:
                print("Value error caught for: " + str(val))
                count = count + 1

        return self.ser_val

    def UpdateRequirements(self, requirements):
        pass
        # TODO Write byte data to micro
        # STUB string with encoding 'utf-8'
        # STUB arr = bytes(requirements, 'utf-8')
        # STUB print(arr)

        # STUB Write our data to the micro
        # STUB ser.write(arr)
