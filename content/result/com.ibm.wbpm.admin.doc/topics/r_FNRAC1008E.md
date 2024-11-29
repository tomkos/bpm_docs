# FNRAC1008E error occurs if Java 2 Security is enabled

When you open the IBM Administration Console for
Content Platform Engine, you see the
following error message:

```
FNRAC1008E Unable to get data from server
User response: Check the error details for more information and contact IBM Software Support if necessary.
Exception details: null com.filenet.apiimpl.util.J2EEUtil (initialization failure)
```

To use the IBM Administration Console for
Content Platform Engine with Java™ 2 Security
enabled, update the server.policy file where the application runs to grant the
required permissions depending on which edition of Business Automation Workflow you are using.

1. Stop the cluster that has the Support capability.
2. On each node that has a cluster member for the cluster with the Support capability, edit the
PROFILE\_HOME/properties/server.policy file by replacing the
CELL\_NAME and CLUSTER\_NAME variables
in// Needed by IBM Administration Console for Content Platform Engine 
grant codeBase "file:${user.install.root}/installedApps/CELL\_NAME/IBM\_BPM\_DocStoreAdmin\_CLUSTER\_NAME.ear/acce\_navigator.war/plugins/nACCE.jar" 
{
permission java.security.AllPermission; 
}; with
your appropriate values, for
example // Needed by IBM Administration Console for Content Platform Engine         
grant codeBase "file:${user.install.root}/installedApps/PCCell1/IBM\_BPM\_DocStoreAdmin\_SupCluster.ear/acce\_navigator.war/plugins/nACCE.jar" 
{ 
permission java.security.AllPermission; 
};
3. Start the cluster that has the Support capability.

1. Stop the server.
2. Edit the file PROFILE\_HOME/properties/server.policy by replacing the
CELL\_NAME, NODE\_NAME and SERVER\_NAME variables
in// Needed by IBM Administration Console for Content Platform Engine 
grant codeBase "file:${user.install.root}/installedApps/CELL\_NAME/IBM\_BPM\_DocStoreAdmin\_NODE\_NAME\_SERVER\_NAME.ear/acce\_navigator.war/plugins/nACCE.jar" 
{ 
permission java.security.AllPermission; 
};
with your appropriate values, for
example // Needed by IBM Administration Console for Content Platform Engine 
grant codeBase "file:${user.install.root}/installedApps/PCCell1/IBM\_BPM\_DocStoreAdmin\_Node1\_server1.ear/acce\_navigator.war/plugins/nACCE.jar" 
{ 
permission java.security.AllPermission; 
};
3. Start the server.