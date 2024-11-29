<!-- image -->

# Starting Business Process Choreographer Explorer

## Before you begin

## About this task

To start Business Process Choreographer Explorer, complete
the following steps.

## Procedure

1 Direct your web browser to the Business Process ChoreographerExplorer URL. The value of the URL depends on how thevirtual host and context root were configured for your installation.The URL takes the following form. https://application\_server\_host :port\_number /context\_root Important: Any attempts to access the Business ProcessChoreographer Explorer using the HTTP protocol are redirected to useHTTPS. In addition, you can extend the URL to go directlyto a list or details page for a process, task, or escalation. https://application\_server\_host :port\_number /context\_root [?oid\_type =oid [&view =graphic ]|?oids\_type =[oids ]] Where:application\_server\_host The network name for the host of the application server that providesthe Business Process Choreographer Explorer instance with which youwant to work. port\_number The port number used by Business Process Choreographer Explorer.The port number depends on your system configuration. The defaultport number is 9443 . context\_root The root directory for the Business Process Choreographer Explorerapplication on the application server. The default is bpc . oid\_type Optional. The type of object that you want to display. This parametercan take one of the following values:aiid Activity instance ID piid Process instance ID ptid Process template ID tkiid Task instance ID tktid Task template ID esiid Escalation instance ID oid Required if oid\_type is specified. The valueof the object ID. If you did not specify a view or you specified anunsupported value for the view, the details page of the object isdisplayed. view Optional. The type of view to be shown. graphic Optional. This parameter is used to display the ProcessState View page or the Process Structure View page. It requires that the value of the oid\_type parameter is piid, aiid, or ptid. oids\_type Optional. The type of the objects that you want display. Use thisparameter if you want to display a list of objects. If you specifythe oid\_type parameter, this parameter is ignored.This parameter can take one of the following values: aiids Activity instance IDs piids Process instance IDs ptids Process template IDs tkiids Task instance IDs tktids Task template IDs oids Optional. A comma-separated list of the object IDs that you wantto display in a list. If you do not specify a list of object IDs,all of the objects of the specified object type that you are authorizedto see are displayed.

```
https://application\_server\_host:port\_number/context\_root
```

```
https://application\_server\_host:port\_number/context\_root
       [?oid\_type=oid[&view=graphic]|?oids\_type=[oids]]
```

    - If the value of the oid\_type parameter is piid
or aiid, the Process State View page is displayed.
For activities, this is the Process State View page for the corresponding
process.
    - If the value of the oid\_type parameter is ptid,
the Process Structure View page is displayed.
2. Enter a user ID and password, then click Login.

## Results

## Example URLs

```
https://hostname:9443/bpc?piid=\_PI:90030109.7232ed16.d33c67f6.beb30076
```

```
https://hostname:9443/bpc?piid=\_PI:9003012b.f36b82cc.ee016df6.dde001ae&view=graphic
```

```
https://hostname:9443/bpc?aiid=\_AI:9004012b.f36bc92b.ee016df6.dde0021f&view=graphic
```

```
https://hostname:9443/bpc?ptid=\_PT:9001012b.fea5bcf.b076df6.abd502b4&view=graphic
```

```
https://hostname:9443/bpc?piids=\_PI:9003012c.3b615b8e.948c67f6.87ff010e,
                               \_PI:9003012c.3b617d5e.948c67f6.87ff016a
```

```
https://hostname:9443/bpc?ptids=
```

<!-- image -->