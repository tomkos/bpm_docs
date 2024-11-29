# Isolating deployment environments

## Before you begin

## Procedure

1. Create the deployment environments.
2 Select one of the following methods to create unique HTTPendpoints:
    - Use a dedicated virtual host for each deployment environment.
See Step
3.
    - Use dedicated context root prefixes for each deployment environment.
See Step
4.
    - Use dedicated web servers for each deployment environment.
See Customizing Business Automation Workflow to work with a web server.
3 If you have multiple deployment environments in a single cell, and ifyou want to use the same web server, create a dedicated virtual host for each deploymentenvironment. For each deployment environment (dep\_env\_name ) in the cell, completethe following actions. For more information, see Virtual hosts in the WebSphere® ApplicationServer information center.

1. Decide on the virtual host name, virtual\_host\_name.
2. Create a dedicated virtual host. Using the administrative console, navigate to
Environment > Virtual hosts and click New.
3. Specify a name for the new virtual host. For example,
vh\_de1.
4. If you are using an external HTTP server, you must add the HTTP server's virtual host
alias. Navigate to Environment > Virtual hosts > Name of the virtual host created in previous step > Host Aliases and click New. For example,
navigate to vh\_de1 and click New. Then enter the host name
of your HTTP server and associate it with the HTTP or HTTPS port.
5 If you want to access the web container of the cluster members, add the host name ofthe cluster member as a host alias. Navigate toEnvironment > Virtualhosts > Name of the virtual host created in previousstep > Host Aliases and click New . Enter the host name of the cluster member andassociate it with the WC\_defaulthost\_secure port. Here is an example of the host aliases that must be added for a single cluster deploymentenvironment that contains two members: Deployment environment name: de1 Cluster name: de1.AppTarget Cluster member 1: de1.AppTarget.Member1 Cluster member 2: de1.AppTarget.Member2 Virtual host name: vh\_de1 Virtual host aliases in vh\_de1 :

Here is an example of the host aliases that must be added for a single cluster deployment
environment that contains two members:

Deployment environment name: de1

Cluster name: de1.AppTarget

Cluster member 1: de1.AppTarget.Member1

Cluster member 2: de1.AppTarget.Member2

Virtual host name: vh\_de1

    - To access IBM® Business AutomationWorkflow overHTTPS, add the cluster member host names and WC\_defaulthost\_secure ports tothe host alias:
        - Cluster member host name for de1.AppTarget.Member1 on
the WC\_defaulthost\_secure port . For example
9443.
        - Cluster member host name for de1.AppTarget.Member2 on
the WC\_defaulthost\_secure port. For example
9443.
- To access IBM Business AutomationWorkflow overHTTP, add the WC\_defaulthost ports.
    - Cluster member host name for de1.AppTarget.Member1 on the
WC\_defaulthost port. For example
9080.
    - Cluster member host name for de1.AppTarget.Member2 on the
WC\_defaulthost port. For example
9080.
- If you use an external HTTP server, add the HTTP server's virtual host alias. This is mandatoryif you are using an external HTTP server.

- Virtual host that corresponds to your HTTP server. For example
ihs.virtual.host.for.de1.ibm.com on port
80
- Virtual host that corresponds to your HTTP server. For example
ihs.virtual.host.for.de1.ibm.com on port
443.
6. Map the virtual host name, virtual\_host\_name, to the deployment
environment, dep\_env\_name, by running the BPMConfig
command: 
install\_root/bin/BPMConfig.sh -update -profile profile\_name -de dep\_env\_name -virtualHost virtual\_host\_name
install\_root\bin\BPMConfig.bat -update -profile profile\_name -de dep\_env\_name -virtualHost virtual\_host\_name
Tip: If there is only one deployment environment in the WebSphere cell, you can omit the
-de option. For more information about the BPMConfig command,
see BPMConfig command-line utility. For information on the Business Automation Workflow virtual host, see Configuring endpoints to match your topology.
7 If you are using an external HTTP server, regenerate and propagate the HTTP serverplug-in.

1. In the administrative console, navigate to Servers > Server Types > Web Servers.
2. Select the name of your HTTP server, then click Generate Plug-in.
3. Select the name of your HTTP server, then click Propagate Plug-in. Tip: The administration service must be running on your HTTP server.
4. Configure dedicated context root prefixes
for each deployment environment by running the BPMConfig command.
For more information about the BPMConfig command,
see BPMConfig command-line utility.
5. Configure an endpoint for the remote
artifact loader (REMOTE\_AL scenario) in each deployment
environment. See Configuring endpoints to match your topology.
6 Optional: If you plan touse applications containing advanced content, such as BPEL process,or that have been imported into IBM Integration Designer and you areadding more than one deployment environment to the cell, provide away to distinguish between the advanced content in these business-levelapplications across the deployment environments. You do this by settingthe AdvancedDeploymentDEScoped property on thesecond and subsequent deployment environments: Important: This topology can impact application maintenance,deployment, and administration. For information, see Considerations for multiple deployment environments in the same cell .

1. At a command prompt, navigate to the bin folder
of the BPM installation.
2. Launch the wsadmin command line and set it to use Jython:
 wsadmin -username adminuser -password mypassword -lang jython
3. Set the AdvancedDeploymentDEScoped property:
 AdminTask.setBPMProperty( [ "-de", "DE\_NAME", "-name", "ProcessCenter.AdvancedDeploymentDEScoped", "-value", "true"] ) DE\_NAME is
the name of the deployment environment for which you are setting the
property. By setting the property to true, business level-applications
in the deployment environment have the deployment environment name
added as an appendix to their name when they are installed into the
deployment environment.
4. Save the change:  AdminConfig.save()
5. Restart the deployment environment and the deployment
manager.
6. If Integration Designer is running, restart it.

## Related information

- setBPMProperty command