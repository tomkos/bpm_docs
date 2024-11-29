<!-- image -->

# How BPEL process and human task applications are deployed in
a network deployment environment

1. The deployment of the application starts on the deployment manager.During this stage, the BPEL process templates and human task templates
are configured in the WebSphere® configuration repository.
 The application is also validated. If errors occur, they are reported
in the System.out file, in the System.err file, or as FFDC entries on the deployment manager.
2. The application deployment continues on the node agent.During
this stage, application is deployed on one application server instance.
This application server instance is either part of, or is, the deployment
target. If the deployment target is a cluster with multiple cluster
members, the server instance is chosen arbitrarily from the cluster
members of this cluster. If errors occur during this stage, they are
reported in the SystemOut.log file, in the SystemErr.log file, or as FFDC entries on the node agent.
3. The application runs on the server instance.During this stage,
the process templates and human templates are deployed to the Business
Process Choreographer database on the deployment target. If errors occur, they are reported in the System.out file, in the SystemErr.log file, or as FFDC entries on this server instance.