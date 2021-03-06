##################################################
# file: SpaceService_client.py
#
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     D:\workspace\digsby\Digsby.py --no-traceback-dialog --multi --server=api5.digsby.org
#
##################################################

from SpaceService_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD
import ZSI

import util.callbacks as callbacks
import util.network.soap as soap

import ZSI.wstools.Namespaces as NS
from msn.SOAP import Namespaces as MSNS, MSNBindingSOAP

# Locator
class SpaceServiceLocator:
    GetXmlFeedPort_address = "http://cc.services.spaces.live.com/contactcard/contactcardservice.asmx"
    def getGetXmlFeedPortAddress(self):
        return SpaceServiceLocator.GetXmlFeedPort_address
    def getGetXmlFeedPort(self, url=None, **kw):
        return SpaceServiceBindingSOAP(url or SpaceServiceLocator.GetXmlFeedPort_address, **kw)

# Methods
class SpaceServiceBindingSOAP(MSNBindingSOAP):

    # op: GetXmlFeed
    @callbacks.callsback
    def GetXmlFeed(self, request, soapheaders=(), callback = None, **kw):
        if isinstance(request, GetXmlFeedMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        # TODO: Check soapheaders
        self.binding.RPC(None, None, request, soapaction="http://www.msn.com/webservices/spaces/v1/GetXmlFeed", soapheaders=soapheaders,
                         callback = callback,
                         **kw)

GetXmlFeedMessage         = GED(MSNS.MSWS.SPACES, "GetXmlFeed").pyclass
GetXmlFeedResponseMessage = GED(MSNS.MSWS.SPACES, "GetXmlFeedResponse").pyclass
