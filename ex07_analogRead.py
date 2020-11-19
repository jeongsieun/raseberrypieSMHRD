import spidevRead as sr

while True:
readData = sr.analog_read(0)
print(f'readData : {readData}')
