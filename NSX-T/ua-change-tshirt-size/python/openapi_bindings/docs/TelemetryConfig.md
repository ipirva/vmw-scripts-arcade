# TelemetryConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_enabled** | **bool** | Enable this to schedule data collection and upload times. If enabled, and a schedule is not provided, a default schedule (WEEKLY, Sunday at 2:00 a.m) will be applied.  | 
**telemetry_proxy** | [**TelemetryProxy**](TelemetryProxy.md) |  | [optional] 
**ceip_acceptance** | **bool** | Enable this flag to participate in the Customer Experience Improvement Program.  | 
**telemetry_schedule** | [**TelemetrySchedule**](TelemetrySchedule.md) |  | [optional] 
**proxy_enabled** | **bool** | Enable this flag to specify a proxy, and provide the proxy settings. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

