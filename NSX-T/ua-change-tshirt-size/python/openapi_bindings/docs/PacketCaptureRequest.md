# PacketCaptureRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **str** | Define the transport node to capture data. | [optional] 
**direction** | **str** | Define the capture direction. Support three types INPUT/OUTPUT/DUAL. | [optional] 
**capduration** | **int** | Define the packet capture duration time. After the capture duration time, the capture process will stop working. | [optional] 
**capamount** | **int** | Define the packet capture amount size. | [optional] 
**capsource** | **str** | This type is used to differenite the incoming request from CLI/UI. | 
**node_ip** | **str** | Define the transport node to capture data. | [optional] 
**capvalue** | **str** | Define the capture value of given capture point. | [optional] 
**filtertype** | **str** | Define the capture filter type. Support PRE/POST mode. | [optional] 
**cappoint** | **str** | Define the point to capture data. | 
**capfilesize** | **int** | Define the packet capture file size limit. | [optional] 
**options** | [**PacketCaptureOptionList**](PacketCaptureOptionList.md) |  | [optional] 
**streamport** | **int** | Set the stream port to receive the capture packet. The STREAM mode is based on GRE-in-UDP Encapsulation(RFC8086). Packets are sent to UDP port 4754. | [optional] 
**caprate** | **int** | Define the rate of packet capture process. | [optional] 
**capcore** | **int** | The CPU core id on Edge node. | [optional] 
**capsnaplen** | **int** | Limit the number of bytes captured from each packet. | [optional] 
**streamaddress** | **str** | Set the stream address to receive the capture packet. | [optional] 
**capmode** | **str** | Define the capture streaming mode. The STREAM mode will send the data to given stream address and port. And the STANDALONE mode will save the capture file in local folder. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

