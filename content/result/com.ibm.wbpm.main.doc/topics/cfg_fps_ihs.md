# Configuring load balancing and failover for federated environments

## About this task

<!-- image -->

Although Process Federation Server is
based on WebSphere Application Server Liberty Network Deployment,
a cluster of process federation servers does not require a configured
Liberty collective or the clusterMember-1.0 feature
on each process federation server. While a Liberty collective can
help to administer multiple servers, it is not necessary for a cluster
of process federation servers. The following procedure assumes that
a Liberty collective is not configured.

## Procedure

Although the specific configuration steps might differ
depending on your environment, the following procedure can help you
implement workload balancing and failover with IBM HTTP Server.

1 Install IBM HTTP Server and configure a web server plug-infor the IBM HTTP Server. Follow steps 1 - 7 for theinstallation and configuration on WebSphere Application Server LibertyNetwork Deployment: Configuring a web server plug-in forthe Liberty profile .Tips:
    - Use the WebSphere Customization Toolbox to configure the web server
plug-in for IBM HTTP Server.
    - Generate a plugin-cfg.xml plug-in file for
each Process Federation Server in
your environment.
2. Merge the plugin-cfg.xml files into
one plugin-cfg.xml plug-in file for the federated
environment.  Attention: Because the federated
environment configuration does not use Liberty collectives, you cannot
use the ClusterManager MBean generateClusterPluginConfig operation
to generate the merged plugin-cfg.xml file.
To
merge the files, use the pluginCfgMerge tool or
manually merge them. For more information, see Configuring simple load balancing across
multiple application server profiles.
3. Copy the merged plugin-cfg.xml file
to IBM HTTP Server.
4 Secure IBM HTTP Server. For a secure federatedenvironment, ensure that you configure at least the following securityaspects. For more information about configuring other security aspects,see Securing IBM HTTP Server .

1. Configure the Secure Socket Layer (SSL) protocol on
IBM HTTP Server. For more information, see Securing with SSL communications.
2. Configure the IBM HTTP Server to trust the Process Federation Server certificate
by importing the Process Federation Server signer
certificate into the IBM HTTP Server truststore. For production
environments, use a certificate authority certificate. For more information,
see Storing a certificate authority certificate.