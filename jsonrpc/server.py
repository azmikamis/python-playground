'''
Created on 1 May, 2015

@author: azmi
'''

from twisted.internet.protocol import ServerFactory, ClientFactory
from twisted.internet import reactor
from protocol import Protocol

class EchoServer(ServerFactory):
    class protocol(Protocol):
        def jsonrpc_echo(self,*args):
            largs = len(args)
            if largs == 1:
                print self.factory.__class__.__name__,'receive:',args[0]
                return args[0]
            elif largs > 1:
                print self.factory.__class__.__name__,'receive:',args
                return args
        def jsonrpc_bounce(self,*args):
            print self.factory.__class__.__name__,'bounce'
            self.notifyRemote('echo',*args)
            largs = len(args)
            if largs == 1:
                return args[0]
            elif largs > 1:
                return args

reactor.listenTCP(8000,EchoServer())
reactor.run()