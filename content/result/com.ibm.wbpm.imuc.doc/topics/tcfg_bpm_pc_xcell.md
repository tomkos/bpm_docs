# Configuring cross-cell security for IBM Workflow
Center

## Before you begin

Before you configure a cross-cell setup, install and configure Business Automation Workflow in another cell.

## About this task

This topic does not apply to IBM® BPM Express.

In simple proof-of-concept scenarios where you want to
demonstrate Workflow Center registration and sharing capabilities without
setting up security trust, HTTP protocol can be specified during the
Workflow Center registration step. This type of setup assumes that
same set of users exist in the user registry of both Workflow Centers.
For proof of concept scenarios, the primary username and password
should be the same on both Workflow Centers.

This document describes
the minimum security setup required to establish trust among the cells
participating in Workflow Center sharing. The setup in a production
environment can be as simple as described here or can be more complex
based on the specific security guidelines for your environment.

## Procedure

1 Configure SSL by exchanging the server SSL certificates. Extract the root SSL certificate from Workflow Center serverB. Perform the following actions using the administrative consoleon Workflow Center server A. Alternately, Workflow Center administrators can extract the rootsigner to a file, copy the file to the file system of the other ProcessCenter, and import the signer certificate from the file. Note: Ifyou are using a remote host to access the administrative console,the extracted certificate will be saved on the standalone server ordeployment manager server, not the remote host.

Extract the root SSL certificate from Workflow Center server
B. Perform the following actions using the administrative console
on Workflow Center server A.

    1. Click Security  > SSL certificate and key management > Key
stores and certificates > DefaultTrustStore > Signer certificates.
    2. Click Retrieve from port.
    3. Specify the host name and secure socket layer port (for
example, the admin host secure port) of the remote Workflow Center
server.
    4. Specify an alias name you want to use for the root signer.
    5. Click Retrieve signer information and
verify that the retrieved signer information is correct.
    6. Click OK to save the
root signer in the local truststore.
    7. Repeat steps 1.a through 1.f on Workflow Center server B to
retrieve the root signer of Workflow Center server A.
2 Share the LTPA keys. The following steps describe how to export the LTPA key from Workflow Center server B and importing it in to the keystore ofWorkflow Center server A.Note: When there are multiplecells involved, one set of LTPA keys are shared among them. Because of this, administrators must: For more information, see Configuring LTPA and working with keys . Workflow Center s A and B now share the same LTPA keys.

- Plan which set of LTPA keys to use in the organization.
- Ensure that the automatic LTPA key generation is turned off. Otherwise, the cells can fall out
of synchronization for the keys if new set is generated.
- Ensure that you set the Maximum number of keys referenced value large
enough to keep the historic keys for as long as the longest lasting process instance is active. The
default setting is to hold one historic LTPA key only. You can find this setting in the
administrative console by navigating to Security > SSL certificate and key management > Key sets > CellLTPAKeyPair.

1. In the administrative console of the remote Process
Center server, click Security  > Global Security.
2. In the Authentication section,
click LTPA.
3. In the Cross-cell single sign-on section,
enter a new Password and a Fully
qualified key file name.
4. Click Export keys then OK.
5 Transfer the exported key file in binary mode to thefile system of the local Workflow Center cell.
    1. In the administrative console of the remote Workflow Center server,
click Security  > Global
Security.
    2. In the Authentication section, click LTPA.
    3. In the Cross-cell single sign-on section,
enter a new Password and a Fully
qualified key file name.
    4. Click Import keys then OK.
6. If your setup includes additional cells, repeat the
previous steps for each additional cell.