<!-- image -->

# Deploying the client: Exporting to a deployment file

## About this task

## Deploying HTML-Dojo pages for Heritage Process Portal
spaces

You might want to deploy an HTML-Dojo client for use in Heritage Process Portal spaces.

### Procedure

To deploy an HTML-Dojo client for use in Heritage Process Portal spaces, perform the following
steps:

1. If you have not already done so, generate a user interface
for your human task. The files that you need to deploy
are generated automatically as part of the client generation.
2 Export the generated client files into a WAR file as follows:
    1. In the business integration view right-click the web
project in which you generated your client, and select Export > WAR file from the list.
    2. In the WAR export window, identify
the web project and provide a Destination where
your WAR will be stored and click Finish.
3. Install the WAR file to the Heritage Process Portal in
the Advanced
deployment environment, and you will
be able to start the client.

## Deploying a JSF client

To deploy a JSF client, proceed as follows, perform the following steps:

### Procedure

1. If you have not already done so, generate a user interface
for your human task. The ClientNameEAR.ear file
is generated automatically as part of the client generation. In addition,
the ProjectNameApp.ear is also created for your
module, and contains the human tasks.
2 Export the generated client files into an EAR file as follows:
    1. In the business integration view right-click your ClientNameEAR,
 and select Export > EAR from the list.
    2. In the EAR export window, select
an ClientNameEAR  name,
provide a Destination where your EAR will be
stored and click Finish.
3. Install these two EAR files on your server, and you will
be able to start the client.

## Deploying a portlet

To deploy a portlet, perform the following steps::

### Procedure

1. In the business integration view right-click your portlet
project, and select Export > WAR.
2. In the WAR export window, select a
WAR file name, provide a Destination where
your WAR will be stored and click Finish.
3. Install this WAR file on your server, and you will be able
to start the client.