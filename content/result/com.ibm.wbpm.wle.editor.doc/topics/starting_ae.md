# Problems starting the desktop Process Designer (deprecated)

```
Unable to establish a connection with the Process Center.
```

When you start Process Designer, you
must log in using your Business Automation Workflow user
name and password. If you do not already have a user account, contact
your  administrator. When you log in, you are connected to the Workflow Center designated
during installation of Process Designer.

| Indicator color   | Connection to Workflow Center server status                                                         |
|-------------------|-----------------------------------------------------------------------------------------------------|
| Green             | Good connection                                                                                     |
| Yellow            | Slow connection that might cause issues with concurrent edits                                       |
| Orange            | Even slower connection and more potential issues with concurrent editing                            |
| Red               | No connection; check with your administrator to ensure the Workflow Center server is up and running |

- Confirm that you are using the correct user name and password.
- Confirm that Workflow Center is
running by accessing it through a browser using the URL in the form http://hostname:port/ProcessCenter.
The default port is 9080.
- Check the eclipse.ini file (in the Process Designer installationdirectory) to confirm that the Workflow Center connectioninformation is correct:
    1. Find the installation folder of Process Designer on
your local computer, for example C:\IBM\ProcessDesigner\v8.5.
    2. Open the eclipse.ini file and locate -Dcom.ibm.bpm.processcenter.url.
Ensure that the URL prefix (http://hostname:port) is the same as the Workflow Center URL
prefix.
- Confirm that your Process Designer version
matches the Workflow Center version.
If your administrator upgraded Workflow Center, you
need to upgrade Process Designer to
the same version by accessing Workflow Center from
a browser and downloading Process Designer.If
the two versions are different, you might see a message similar to
the following message: The versions of Process Center("BPM8501-20130922-000036") and Process Designer ("BPM8500-20130525-092636") do not match.
- If you see a blank white Process Designer view
or the view does not display fully, or if you see an HTTP error, press F5  to
refresh. If the display continues to be blank, enable a security option
as described in Process Designer window is blank.
- If you have a firewall or proxy server, or are running a service
that forwards the ports, check that communication to make sure the
required ports are open. For information about Workflow Center ports
that are accessed by Process Designer, see
the table in the topic Connections from IBM Process Designer to Workflow Center.

- Enabling error logging in the desktop Process Designer (deprecated)

 Traditional: 
You can configure IBM® Process Designer to log errors by using java.util.log. You can then examine the logs to troubleshoot problems with Process Designer.