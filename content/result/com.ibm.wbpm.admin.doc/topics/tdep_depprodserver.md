<!-- image -->

# Deploying a module or mediation module

## Before you begin

Before deploying a service application to a production server, assemble and test
the application on a test server. After testing, export the relevant files as described in Preparing to deploy to a server
 and bring the files to the production system to deploy. For more
information, see the Integration Designer and WebSphere® Application
Server documentation.

## Procedure

1. Copy the module and other files onto the production server.

The modules and resources (EAR, JAR, RAR, and WAR files) needed by the application are moved to
your production environment.
2 Run the serviceDeploy command to create an installable EAR file. This step defines the module to the server in preparation for installing the application intoproduction.

This step defines the module to the server in preparation for installing the application into
production.

    1. Locate the JAR file that contains the
module to deploy.
    2. Issue the serviceDeploy command
using the JAR file from the previous step as input.
3. Install the EAR file from step 2.
How you install the applications depends on whether you are installing the application on a
stand alone server or a server in a cell.Note: You can either use the administrative console or a
script to install the application. See the WebSphere Application
Server documentation for additional information.
4. Save the configuration.
The module is now installed as an application.
5. Start the application.

## Results

## What to do next