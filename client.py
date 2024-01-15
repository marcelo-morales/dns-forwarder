import time
import socket

port_number = input("what port would u like to listen in ")
print("you entered " + str(port_number))

if not port_number:
    port_number = '53'


for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    message = b'testing' # bytes like object
    address = ("127.0.0.1", 12000)
    start = time.time()
    client_socket.sendto(message, address)

    try:
        data, server = client_socket.recvfrom(port_number) # passing in port number from user
        end = time.time()
        elapsed = end - start
        print(f'{data} {pings} {elapsed}')
    except socket.timeout:
        print('request has timed out')




def parse_packet():
    print('we will parse packet here')


def forward_request():
    print('forward request to DNS server to resolve the request')

def receive_DNS_then_forward():
    print('receive answer from DNS, unpack it, and forward answer to original client')

def cache_result():
    print('cache result of sucessful DNS resolution and respond to future request with local cache, watch out for TTL')
'''
Time to live (TTL) refers to the amount of time or “hops” that a
packet is set to exist inside a network before being discarded by a
router. TTL is also used in other contexts including CDN caching and
 DNS caching.
'''


