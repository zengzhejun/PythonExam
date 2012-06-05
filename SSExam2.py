import socketserver;
from win32com.client import Dispatch;
from ctypes import *;

class MyTCPHandler(socketserver.StreamRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        #req = self.rfile.readline().strip()
        req = str(self.request.recv(1024).strip(),'ascii');
        #req = socket.recv(1024);
        #print("{} wrote:".format(self.client_address[0]))
        print(req)
        if req == "movethemouse":
             windll.user32.SetCursorPos(1024, 0);
        elif req == "startpowerpoint":
            app = Dispatch("powerpoint.Application");
            #app.ActivePresentation.SlideShowWindow.View.Next;
            #app.ActivePresentation.SlideShowWindow.View.Exit;
            app.Visible = True;
        else:
            windll.user32.SetCursorPos(5, 5);
            #print("dsfasfd");

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 7799

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()