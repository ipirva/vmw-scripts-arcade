# NSX UA Manager - Change T-shirt Size

We want to automate the change of the t-shirt size of an existing NSX-T Manager (GM or LM) UA cluster.
The end result will be a new NSX-T Manager cluster with its VMs appliances with the new size. The new NSX-T Manager cluster (target) will replace the existing one (source). The target cluster will synchronize its data from the source cluster. The source cluster will be deleted and the source NSX-T Manager VMs will be shut down.
[NSX Manager VM Resource Requirements](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.1/installation/GUID-AECA2EE0-90FC-48C4-8EDB-66517ACFE415.html)

The supported target NSX-T cluster can have 1, 2 or 3 VMs appliances.
The target NSX-T Manager VM appliances will be deployed on the specified vCenter(s).

## Prerequisites

1. The source/initial NSX-T cluster must be in a stable state, with 1 or 3 VMs appliances.
2. NSX-T backup must be configured and enabled.
3. The new NSX-T appliance VM (OVF) must be made available on a web (http/https) server reachable from vCenter.
4. All the new NSX-T Manager VM(s) (1, 2 or 3) must be in the same IPv4 subnet. Make sure that the IPv4 subnet has free IPv4 addresses: target NSX-T Manager VM number + 1 IPv4 for the NSX-T Manager cluster VIP.
5. Make sure that the runner can resolve the NSX-T Manager DNS hostnames.
6. Make sure that there is IP connectivity and [the right TCP/UDP flows](https://ports.esp.vmware.com/home/NSX-T-Data-Center) are allowed between the new NSX-T Manager VM appliances and the rest of the infrastructure. During the change of the NSX-T Manager VM appliances, the target NSX-T Manager VM appliances must be able at least to communicate with the source/initial NSX-T Manager VM appliances.
7. Identify the ESXi(s) hosts on which the NSX-T Manager VM Appliance(s) will be installed
8. Prepare the values for the following variables for each target NSX-T Manager VM appliance: VM name, VM hostname, VM deployment size, VM OVA remote path (HTTP/HTTPS), vSphere hosts for the VM deployement, VM IPv4 interface prefix, VM IPv4 gateway, DNS server list, NTP server list
9. Have VM Folder and Resource Pool created on vSphere for the target NSX-T Manager VM Appliance
10. Bring your own license

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
