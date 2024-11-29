# Configuring the propagation of HTTP headers and cookies for
a third-party authentication environment

## Procedure

1. Connect to the wsadmin client:

wsadmin.bat -conntype NONE -lang jython
wsadmin.sh -conntype NONE -lang jython
2. Get and display the BPMDispatchConfiguration object:

wsadmin>path='/Cell:%s/BPMFederationConfiguration:/BPMApiFederation:/BPMApiDomain:default
    /BPMDispatchConfiguration:/' % cellName
wsadmin>dc=AdminConfig.getid(path)
wsadmin>dc
3. Set the values of the denyForwardHttpHeader and
denyForwardHttpCookie attributes to deny the forwarding of all headers and
cookies:

wsadmin>AdminConfig.modify(dc,[['denyForwardHttpHeader','.*']])
wsadmin>AdminConfig.modify(dc,[['denyForwardHttpCookie','.*']])
wsadmin>AdminConfig.save()
4. Set the value of the allowForwardHttpHeader and
allowForwardHttpCookie attributes to forward only the specified headers and
cookies. For example, if you use CA SiteMinder, enter the following commands:
wsadmin>AdminConfig.modify(dc,[['allowForwardHttpHeader',
   'SM\_TRANSACTIONID|SM\_SDOMAIN|SM\_AUTHTYPE|SM\_USER|SM\_USERDN|
    SM\_SERVERSESSIONID|SM\_SERVERSESSIONSPEC|SM\_TIMETOEXPIRE|
    SM\_SERVERIDENTITYSPEC']])
wsadmin>AdminConfig.modify(dc,[['allowForwardHttpCookie','SMSESSION']])
wsadmin>AdminConfig.save()For
information about the header and cookie names that are used by other third-party authentication
products, see the documentation for those products.