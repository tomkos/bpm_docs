# Enabling or disabling logging for terminating or deleting process instances

- REST API (including PAC Process Inspector)
- JavaScript API
- Web service API

```
[12/02/19 16:57:02:072 EST] 00000148 BPDEngineUtil I   CWTDM0191I: The process instance with InstanceId: 162 was 
terminated by User: tw\_admin from REST API.
```

- REST API  (including PAC Process Inspector)
- WSAdmin command

## Enabling or disabling logging

```
<server>
      <log-terminate-delete-instances merge="replace">false</log-terminate-delete-instances>
  </server>
```

For more information about deleting process instances, see Deleting process instances. For more information about the actions that are available
in the Process Inspector, see Actions in the Process Inspector.