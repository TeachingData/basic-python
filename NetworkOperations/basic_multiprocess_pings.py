from multiprocessing import Process
import os
import sys 

# run with: python basic_multiprocess_pings.py www.google.com www.python.org www.github.com

# just checking that it works
#print(f"Number of cpu : {multiprocessing.cpu_count()}")

def get_pings(ip):
    # limiting number of pings to 3 -c = count
    print(os.system(f'ping {ip} -c 3'))

if __name__ == '__main__':
    # Similar to other code we've done we start small
    # I'm going to get a list of addresses to ping and then ping them in a function
    # I'm going to use multiprocess to make those functions run in parallel
    for ip in sys.argv[1:]:
        Process(target=get_pings, args=(ip,)).start()
