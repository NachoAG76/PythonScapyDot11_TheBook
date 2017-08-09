
# This example is a simple 'hello world' for scapy-fakeap.
# An open network will be created that can be joined by 802.11 enabled devices.

from fakeap import *

ap = FakeAccessPoint('mon0', 'WLAN_WL55')
ap.run()
