# Error responses

```
#Response
HTTP/1.1 500 Internal Server Error
Content-Type: application/json;charset-UTF-8
{
  "UserMessage":
  {
    "UniqueId":"FNRPA0024E",
    "Text":"FNRPA0024E IBM Case Builder cannot connect to the Process 
    Engine.",
    "Severity":"ERROR"
  }
  "UnderlyingDetails":
  {
    "Causes":
    [
      "Failed to connect to vworbbroker on hq-liquent:32776[100].  Check server
      connection.\nfilenet.pe.peorb.client.ORBServiceHelper$VWORBBrokerNotStarted: 
      Failed to retrieve an IOR for vworbbroker. URL=http:\/\/hq-liquent:32776\
      /IOR\/FileNet.PE.vworbbroker.  Check PE server to make sure that vworbbroker
      process is started.",
      "Failed to retrieve an IOR for vworbbroker. URL=http:\/\/hq-liquent:32776\
      /IOR\/FileNet.PE.vworbbroker.  Check PE server to make sure that vworbbroker
      process is started."
    ]
  },
}
```

Use the value of the UniqueId element to search for message information in the workflow
documentation.