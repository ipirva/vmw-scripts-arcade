# LbCookiePersistenceProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie_garble** | **bool** | If garble is set to true, cookie value (server IP and port) would be encrypted. If garble is set to false, cookie value would be plain text.  | [optional] [default to True]
**cookie_secure** | **bool** | If cookie secure flag is true, it prevents the browser from sending a cookie over http. The cookie is sent only over https. Only available for insert mode.  | [optional] [default to False]
**cookie_fallback** | **bool** | If fallback is true, once the cookie points to a server that is down (i.e. admin state DISABLED or healthcheck state is DOWN), then a new server is selected by default to handle that request. If fallback is false, it will cause the request to be rejected if cookie points to a server  | [optional] [default to True]
**cookie_mode** | **str** | cookie persistence mode | [optional] [default to 'INSERT']
**cookie_domain** | **str** | HTTP cookie domain could be configured, only available for insert mode.  | [optional] 
**cookie_httponly** | **bool** | If cookie httponly flag is true, it prevents a script running in the browser from accessing the cookie. Only available for insert mode.  | [optional] [default to False]
**cookie_name** | **str** | cookie name | 
**cookie_time** | [**LbCookieTime**](LbCookieTime.md) |  | [optional] 
**cookie_path** | **str** | HTTP cookie path could be set, only available for insert mode.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

