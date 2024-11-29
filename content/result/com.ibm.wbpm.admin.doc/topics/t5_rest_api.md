<!-- image -->

# REST API: The URL is not configured correctly

The Representational State Transfer (REST) API must be
configured correctly, otherwise you get an error when you try to use
the graphical process widget in the Business Process Choreographer
Explorer, Business Process Archive Explorer, or Business Space.

## Reason

- If you want to use the graphical process widget in a clustered
environment, you must set the endpoints for the Business Flow Manager
and Human Task Manager REST APIs manually.
- If you configured Business Process Choreographer Explorer or Business
Process Archive Explorer in a cluster, to achieve load balancing,
you must map the web modules to a web server and configure the correct
host name and port for this web server.
- If you change the context root or map web modules to a web server,
you might need to change the URL for the REST API.

## Resolution

- If you configured Business Process Choreographer Explorer or Business
Process Archive Explorer instances, check your log files for messages
CWWBZ0052W or CWWBZ0053W, which contain information about the URL
that the instance was configured to use.
- If you have multiple Business Process Choreographer or BusinessProcess Archive Manager configurations in a cell, and the REST APIweb modules for the following applications are mapped to the sameweb server, these web modules must have unique context roots:For the Business Process Choreographer Explorer: For the Business Process Archive Explorer:
    - Business Flow Manager BPEContainer application
    - Human Task Manager TaskContainer application
    - Business Flow Manager BPArchiveMgr application
    - Human Task Manager TaskArchiveMgr application
    1 To set the context roots for the Business Flow Manager, click Applications > Application Types > WebSphere enterprise applications then application \_suffix > Context Root for Web Modules ,where application is BPEContainer fora Business Process Choreographer configuration or BPArchiveMgr fora Business Process Archive Manager configuration, and suffix iseither node\_name \_server\_name orthe cluster\_name where Business Process Choreographeror Business Process Archive Manager is configured. Then make surethat the context roots for the following web modules and are correctand unique.
        - BFMIF\_scopeWeb
        - BFMJAXWSAPI
        - BFMRESTAPI
2 To set the context roots for the Human Task Manager, click Applications > Application Types > WebSphere enterprise applications then application \_suffix > Context Root for Web Modules ,where application is TaskContainer fora Business Process Choreographer configuration or TaskArchiveMgr fora Business Process Archive Manager configuration, and suffix iseither node\_name \_server\_name orthe cluster\_name where Business Process Choreographeris configured. Then make sure that the context roots for the followingweb modules and are correct and unique.
    - HTMIF\_scopeWeb
    - HTMJAXWSAPI
    - HTMRESTAPI
3 To change the REST URLs that the Business Process ChoreographerExplorer uses: .

1. Click Servers > Clusters > WebSphere application server clusters >  cluster\_name  or Servers > Server
Types > WebSphere application servers >  server\_name .
On the Configuration tab, in the Business Process Manager section,
expand Business Process Choreographer and click Business
Process Choreographer Explorer.  Update the Business Flow
Manager and Human Task Manager REST API URLs.
2. Update the endpoints in config-rest.xml using a command similar
to the following example, which uses PS.AppTarget as
the cluster name:wsadmin>AdminTask.updateRESTServiceProvider(['-clusterName',  'PS.AppTarget', '-appName', 'BPEContainer\_PS.AppTarget', '-webModuleName','bfmrestapi.war', '-contextRoot', '/rest/bpm/bfmPS2/'])

wsadmin>AdminTask.updateRESTServiceProvider(['-clusterName',  'PS.AppTarget', '-appName', 'TaskContainer\_PS.AppTarget', '-webModuleName','taskrestapi.war', '-contextRoot', '/rest /bpm/htmPS2/'])