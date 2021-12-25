from inputimeout import inputimeout, TimeoutOccurred
try:
    something = inputimeout(prompt='>>', timeout=5)
except TimeoutOccurred:
    print('Timeout!')
    something = 'something'