# Function to read
# last N lines of the file

def LastNlines(fname, N):
    with open(fname, 'rt') as file:
        # loop to read iterate
        # last n lines and print it
        for line in (file.readlines()[-N:]):
            print(line, end='')

fname = "/home/pi/josh/CTA_EWH/build/debug/log.csv"
N = 1
LastNlines(fname, N)
