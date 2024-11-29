<!-- image -->

# Importing an SSL security certificate into Integration Designer

## Before you begin

## About this task

To install copy of the SSL security certificate into Integration Designer, perform the following
steps:

## Procedure

1. Launch your web browser and enter
https://hostname:secure\_port/ProcessCenter/login.jsp
where hostname is the fully-qualified domain name of the process center server, and
secure\_port is the process center secure SSL port number.
2. On the Security Alert window, click View Certificate.
3. On the Certificate window, click the Details tab.
4. Click Copy to File to specify where to save the certificate file
on your system.
5. In the wizard, click Next, accept the default values, and then
click Next again.
6. Enter a file name for the security certificate, for example,
pc\_cert.cer, and click Next.
7. Click Finish. After you have created the SSL certificate, you can
import it into the Java JRE that you will be using for Integration Designer.
8. Copy the certificate to IIDInstall\jdk\jre\bin where
IIDInstall is the directory where you installed Integration Designer.
9 Switch to the same location on the command line and run the keytool command:
    1. keytool.exe -import -v -file <certificate file> -keystore
..\lib\security\cacerts If you previously imported SSL certificates into the
Integration Designer, add the -alias <key name> parameter to specify a different
key name to avoid name conflicts. The default value is mykey.
    2. Enter the keystore password: changeit (this is usually the
default password)
    3. Enter y at the prompt to trust the certificate.