# On the Edge 42 browser, the process playback window blocks content

When using the Microsoft Edge 42 browser in an IBM® Business Automation
Workflow environment, the process playback window blocks
content due to an invalid security certificate. The problem is restricted to processes in the
process playback window and does not affect client-side human services.

When the process playback window blocks content in the Edge 42 browser due to an invalid security
certificate, the following message typically appears:

Content was blocked because it was not signed by a valid security
certificate

To resolve this problem, install a trusted root certificate for the Edge 42 browser by completing
the following instructions:

1. In the Edge 42 browser, connect to the Workflow Center server of IBM Business Automation
Workflow by using the server host name rather than the IP
address.
2. In the browser URL field, click the Show site information icon (or click
the Certificate error link if it appears). Depending on whether you click the
Show site information icon or the Certificate error
link, either the Website Identification panel or the Website Problem panel opens.
3. In the panel, select the View certificate link. The Certificate
Information pane opens in the Process Designer window.
4. In the Certificate Information pane, select the root certificate and then click
Export to file.
5. In the file system window, select the folder where you want to export the certificate and then
click Save.
6. Close the Edge 42 browser and its windows (including the window used to connect to the Workflow Center server of IBM Business Automation
Workflow).
7. In the folder where you exported the certificate, double-click the certificate and then click
Open in the Open File – Security Warning dialog box.
8. In the Certificate dialog box, click Install Certificate.
9. In the Certificate Import wizard, select Local Machine and then click
Next.
10. Select the Place all certificates in the following store radio
button.
11. Click Browse and select Trusted Root Certification
Authorities as the certificate store for the certificate that you will import and then
click OK.
12. Click Next and then click Finish.
13. If a dialog box opens to indicate that the certificate was imported successfully, click
OK.
14. Start the Edge 42 browser and connect to the Workflow Center server of IBM Business Automation
Workflow by using the server host name rather than the IP
address.
15 If you attempt to use the process playback window and you receive another message that indicatesthat content was blocked because it was not signed by a valid security certificate, theetc/hosts file may need to include a mapping of the IP address to the host namefor the server. To specify a mapping, complete the following steps:
    1. In the file system, navigate to the following folder:
C:\Windows\System32\drivers\etc
    2. Edit the hosts file and add a mapping statement. For example:
9.37.136.102 workflowserver.domain
    3. Save the file.
    4. Close and then restart the Edge 42 browser and connect to the Workflow Center server of IBM Business Automation
Workflow by using the server host name rather than the IP
address.