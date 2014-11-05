import SocketServer
from random import randint

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        self.msg_pool =  [
                        "Hacking is fun", 
                        "Next time we will learn how to break into a website",
                        "We did a good job in the last CTF hacking competetion!", 
                        "We will keep doing CTFs in the spring semester.",
                        "Hacking as a career? Check out the options:\nhttp://www.cs.gwu.edu/academics/graduate_programs/master/cybersecurity/cybersecurity-jobs",
                        "Let me know what topics you're interested."    
                    ]
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        # just send back the same data, but upper-cased
        self.request.sendall("Your message in caps:\t" + self.data.upper())
        # send another message
        self.request.sendall("A random message from server: \n" + self.msg_pool[randint(0, len(self.msg_pool)-1)])


if __name__ == "__main__":
    HOST, PORT = "128.118.102.44", 9999
    #HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    print 'Server started!'

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()