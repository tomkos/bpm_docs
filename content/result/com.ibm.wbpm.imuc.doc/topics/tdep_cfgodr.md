# Configuring Business Automation Workflow for on-demand
routing and dynamic clustering

## About this task

## Procedure

1 Configure the ODR as a proxy server for Business Automation Workflow :
    1 Set up Business Automation Workflow withthe IBM HTTP Server (IHS):
        1. Install Business Automation Workflow on
three systems, for example, SUSE130, SUSE131, SUSE132. For more information,
see Planning your network deployment environment.
        2. Create one deployment manager node on SUSE130, and two custom
nodes on each of the SUSE131 and SUSE132 systems.
        3. Generate a three-cluster Business Automation Workflow deployment
environment on these nodes using IBM
DB2®.
2 Create the ODR: You can now log in to the ProcessAdmin/portal/bpc using the host name and the port numberof the ODR server.
    1. Create another custom node on SUSE130, which is the system that
has the deployment manager, and then federate this node to the deployment
manager.
    2. Point your browser to http://<dmgr\_host>:<dmgr\_port>/ibm/console and
log in to the administrative console.
    3. Click Servers > Server
Types > On Demand Routers,
and then click New. Select the node that corresponds
to the ODR and complete the steps in the wizard to create and save
the new ODR server.
    4. On the On-Demand Routers page, click Start to
start the ODR server.
3 Configure the ODR server to work with IHS: Note: Ignorethis step if you chose not to configure the IBM HTTP Server for Business Automation Workflow . Note: For more information about ODR configuration, see Creating and configuring ODRs . You can now log in to the Process Admin/portal/bpc usingthe host name and the port number of the IHS server.

1. In the administrative console, click Servers > Server Types > On Demand Routers > On Demand Router Settings > On Demand
Router Properties > On Demand Router Settings > Trusted security proxies and
add the IHS server host name to the corresponding field.
2. Click Servers > Server
Types > On Demand Routers > On
Demand Router Settings > On Demand Router Properties > On Demand Router Settings > Proxy Plugin
Configuration Policy and set the plug-in
scope to Cell.
3. Click OK and then click Save.
4. Restart the ODR server.
5. Copy the <WAS\_HOME>/profiles/ODR\_profiles\_name/etc/Plugin-cfg.xml file
to the <IHS\_Plugin\_Location>/Plugins/config/webserver1 directory
on the IHS server. If the Plugin-cfg.xml file
already exists, replace it with the latest version.
6. Restart the IHS server.
2. Configure the Business Automation Workflow topology with dynamic clusters as described in
Creating dynamic clusters.

Tip:  When configuring the dynamic clusters, to ensure that you can exploit all of the
dynamic cluster features, it is recommended that you convert each static cluster to a dynamic
cluster and set the Minimum number of cluster instances to keep one instance
started at all times for each dynamic cluster. For example, in your Business Automation Workflow configuration with a three-cluster network
deployment environment, convert all three static clusters to dynamic clusters, and then set the
Minimum number of cluster instances to keep at least one instance started at
all times for each dynamic cluster.
3. To monitor the environment, configure the health management for Business Automation Workflow. For more information, see Configuring health management.