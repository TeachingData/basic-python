from multiprocessing import Process
import os
import sys 

# just checking that it works
#print(f"Number of cpu : {multiprocessing.cpu_count()}")

def get_pings(ip):
    print(os.system(f'ping {ip}'))

if __name__ == '__main__':
    # Similar to other code we've done we start small
    # I'm going to get a list of addresses to ping and then ping them in a function
    # I'm going to use multiprocess to make those functions run in parallel
    for ip in sys.argv[1:]:
        Process(target=get_pings, args=(ip,)).start()
