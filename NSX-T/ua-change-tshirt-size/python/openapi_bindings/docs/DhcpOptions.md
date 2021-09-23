# DhcpOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option121** | [**DhcpOption121**](DhcpOption121.md) |  | [optional] 
**others** | [**list[GenericDhcpOption]**](GenericDhcpOption.md) | To define DHCP options other than option 121 in generic format. Please note, only the following options can be defined in generic format. Those other options will be accepted without validation but will not take effect. --------------------------   Code    Name --------------------------     2   Time Offset     6   Domain Name Server     13  Boot File Size     19  Forward On/Off     26  MTU Interface     28  Broadcast Address     35  ARP Timeout     40  NIS Domain     41  NIS Servers     42  NTP Servers     44  NETBIOS Name Srv     45  NETBIOS Dist Srv     46  NETBIOS Node Type     47  NETBIOS Scope     58  Renewal Time     59  Rebinding Time     64  NIS+-Domain-Name     65  NIS+-Server-Addr     66  TFTP Server-Name (used by PXE)     67  Bootfile-Name (used by PXE)     93  PXE: Client system architecture     94  PXE: Client NDI     97  PXE: UUID/UNDI     117 Name Service Search     119 Domain Search     150 TFTP server address (used by PXE)     175 Etherboot     209 PXE Configuration File     210 PXE Path Prefix     211 PXE Reboot Time  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

