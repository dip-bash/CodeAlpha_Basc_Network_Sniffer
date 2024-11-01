import socket,struct

try:
    connect = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3)) #create a socket 
except socket.error:
    print("Error creating socket")  #error handling 
    exit


#format mac addr
def decode(addr):
    addr = map('{:02x}'.format, addr)
    mac = ':'.join(addr).upper()
    return mac

#infinite loop to sniff packets
while True:
    raw_data, addr = connect.recvfrom(65565)
    dest, source, eth = struct.unpack('! 6s 6s H', raw_data[:14])

    dest_mac = decode(dest)
    src_mac = decode(source)
    ethe_protocol = socket.htons(eth)
    data = raw_data[14:]

    print('\nEthernet Frame')
    print(f'Destination: {dest_mac}| Source: {src_mac}| Protocol:{ethe_protocol}')

# format row data into Hex
    print('\nData(Hex)')
    for i in range(0, len(data), 16):
        chunk = data[i:i+16]
        print(' '.join(f'{b:02x}' for b in chunk))
    

