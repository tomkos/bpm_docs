# Configuring a proxy server

You can use the configureProxyServer.py script
to create the routing server functionality for the Workflow Center cluster
or the Workflow Server clusters
when you have more than one node in your topology.

Use
this information to configure the WebSphere proxy server. Alternately,
you can use any other proxy server or HTTP server. For information
about configuring a different proxy server or an HTTP server, see
the documentation for the product that you use.

## Before you begin

## About this task

The configureProxyServer script provides a simple way
to create the routing server functionality for Workflow Center server
or Workflow Server when
you have more than one node in your topology.

## Procedure

- To configure a WebSphere proxy server by running a script,perform the following actions.
    1 Change to the directory were the proxy scripts are located. This directory contains the following scripts. The .sh and .bat filesprovide a convenient way to run the .py script.
        - cd install\_root/BPM/Lombardi/tools/proxy
        - cd install\_root\BPM\Lombardi\tools\proxy
        - configureProxyServer.py
        - configureProxyServer.sh
        - configureProxyServer.bat
2 Create and configure the WebSphere proxy server by runningone of the following commands. Where options can include any of the followingparameters:-d, --deployment-environment environment\_name Optionally specifies the name of the deployment environment toconfigure a proxy server for. If you do not specify a deployment environment,a proxy server will be created for each deployment environment. -n, --node node\_name Optionally specifies the name of the node to deploy the proxyservers to. If you do not specify a node, one will be selected foryou. --no-save Optionally specifies not to save changes to the configuration. --no-sync Optionally specifies not to synchronize changes across all nodes.
    - wsadmin -f configureProxyServer.py options
    - configureProxyServer.sh options
    - configureProxyServer.bat options
3. You must restart all clusters in the deployment environment
after running the configureProxyServer script.
- To configure a WebSphere proxy server manually using theadministrative console, perform the following actions.

1. Decide which node will host the proxy server.  If
necessary, create and federate a new managed node. Make a note of
the node's host name as proxy\_host\_name.
2. Create the proxy server using the administrative
console by clicking Servers > Server types > WebSphere proxy servers > New.
3. Identify the proxy server's port numbers. Click Servers > Server types > WebSphere proxy servers > your\_proxy\_server > Ports and note the port values proxy\_http\_port and proxy\_https\_port that
correspond to the port values of the end points named PROXY\_HTTP\_ADDRESS and PROXY\_HTTPS\_ADDRESS.
4. If proxy\_http\_port and proxy\_https\_port are
using the default values 80 and 443,
skip to step 8.
5 Add the following host aliases to the default\_host virtualhost:
    - Host name: * Port: proxy\_http\_port
    - Host name: * Port: proxy\_https\_port
6. For each cluster member in the application
deployment cluster in your deployment environment, note the port value
of the end point named WC\_defaulthost\_secure as cluster\_member\_https\_port.
7 Add rewrite rules. Click Servers > Server types > WebSphere proxy servers > your\_proxy\_server > HTTP Proxy Server Settings > Rewritingrules , then for each value of cluster\_member\_https\_port thatyou noted in step 6 ,add the following re-writing rule to the proxy server that you createdin step 2 :

- From URL Pattern: https://proxy\_host\_name:cluster\_member\_https\_port/*
- To URL Pattern: https://proxy\_host\_name:proxy\_https\_port/*
8 Set the cache.query.string customproperty. Click Servers > Server types > WebSphere proxy servers > your\_proxy\_server > HTTP Proxy ServerSettings > Proxy settings > Customproperties , and add the following customproperty to the proxy server settings:

- Name: cache.query.string
- Value: true
9. Restart all the clusters in your deployment environment.
10. Start the proxy server.
- To configure a different type of routing server or an existing
routing server, such as a web server, proxy server, or reverse proxy
server, use the documentation for the product that you are using for
routing requests.

## Results

You have a routing server that is configured to support
a topology with more than one node.

## What to do next

After configuring the proxy server and depending on your
network topology, the firewall and web clients can access only through
the proxy server ports, you must customize Business Automation Workflow to work
with a web server, which will complete the endpoint configuration.

If
you are using a third-party authentication product, make sure that
it works correctly with the new proxy. For more information, see Configuring third-party authentication products.

- Deleting a proxy server

To remove a proxy server, delete the proxy server, remove host aliases, and delete the virtual host.
- Verifying Process Portal

After configuring Process Portal, use the Process Portal Verification pages to make sure that the applications used by Process Portal are all accessible and that Process Portal is working. For federated environments, you can also check that Process Portal can access Process Federation Server and all the Business Automation Workflow servers.