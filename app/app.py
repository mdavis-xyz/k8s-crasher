import time

log_fname = 'logs.txt'
def log(s):
    with open(log_fname,'a') as f:
        f.write(s + '\n')

log("starting up")
with open('Data.txt') as f:
    data = f.read()
log("sucessfully started")
while True:
    time.sleep(50)


