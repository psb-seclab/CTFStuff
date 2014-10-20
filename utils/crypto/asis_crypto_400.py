import socket

host = 'asis-ctf.ir'
port = 12445

# cut_between('smth: 123; adsf; ', 'smth: ', '; ') == '123'
def cut_between(source, before, after):
    pos1 = source.find(before)
    pos2 = source.find(after, pos1 + len(before) + 1)
    assert pos1 != -1
    assert pos2 != -1
    return source[pos1 + len(before) : pos2]

# decrypts or encrypts given input, mode: 'E' or 'D'
def ask(input, mode):
    global conn
    while True:
        try:
            conn.sendall(mode + '\r\n')
            data = conn.recv(1024) # 'Tell us your message to encrypt: '
            conn.sendall('%d\r\n' % input)
            data = ''
            while '[D]ecrypt:' not in data:
                data += conn.recv(1024)
            if 'too long' in data:
                return -1
            if 'None' in data:
                return None
            return int(cut_between(data, 'Your secret is: ', '\n'))
        except IOError:
            print 'Connection failed!'

def E(input):
    return ask(input, 'E')

def D(input):
    return ask(input, 'D')

def find_N():
    # length of N should be similar to the length of the secret
    start = 10**307
    end = 10**311

    assert ask(p, 'E') != -1
    assert ask(k, 'E') == -1

    # binary search
    while start < end:
        mid = (start + end) / 2
        res = ask(mid, 'E')
        if res == None:
            # server sends 'None' for 0 and n-1
            return mid + 1
        if res == -1:
            end = mid
        else:
            start = mid + 1

        print '[%d, %d]' % (start,end)
    return start

if __name__ == '__main__':
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((host, port))
    print conn.recv(1024) # riddle
    print conn.recv(1024) # question
    answer = 'Paillier'
    print answer
    conn.sendall(answer + '\r\n')
    data = conn.recv(1024)
    secret = int(cut_between(data, 'is: ', '\n'))
    data = conn.recv(1024)

    n = find_N()

    secret_plaintext = D((E(1) * secret) % (n**2)) - 1
    # flag: ASIS_85c9febd4c15950ab1f19a6bd7a94f85
    print hex(secret_plaintext)[2:].rstrip('L').decode('hex')