# Configuring your environment to use the Content Platform Engine Java API

## About this task

## Procedure

1. Include xlxpScanner.jar, xlxpScannerUtils.jar,
and stax-api.jar in the CLASSPATH.
2. Define a system property to reference the appropriate JAAS configuration file as follows:
-Djava.security.auth.login.config=C:\CE\_API\config\jaas.conf.CEWS.