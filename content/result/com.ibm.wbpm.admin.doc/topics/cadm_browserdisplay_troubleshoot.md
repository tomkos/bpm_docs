# Resolving browser display problems with administration tools

## About this task

- To ensure all of the pages in these administration tools load correctly, run Internet Explorer
in Compatibility View. See the Internet Explorer documentation for details on enabling Compatibility
View. Note: This limitation does not apply to the WebSphere Application Server administrative
console.
Workflow Center and Process Admin
Console might require additional security configuration. If you are using Internet Explorer V9, the
browser might respond with security-related errors. If your browser returns security-related errors,
add Workflow Center and
Process Admin Console URLs to the set of trusted sites. Navigate to
Tools > Compatibility view
settings.
- When using Microsoft InternetExplorer to open Workflow Center or the Process Admin console, Internet Explorer might deliver thefollowing security warning: Do you want to view only the webpage content that was delivered securely? This webpage contains content that will not be delivered using a secure HTTPS connection, which could compromise the security of the entire webpage. Thisis caused by the fact that some of web based applications includedin Business Automation Workflow loadsome images using HTTP. To resolve the issue, do one of thefollowing:

```
Do you want to view only the webpage content that was delivered securely? 
This webpage contains content that will not be delivered using a secure HTTPS connection, which could compromise the security of the entire webpage.
```

This
is caused by the fact that some of web based applications included
in Business Automation Workflow load
some images using HTTP.

    - When presented the security warning pop-up window, click No.
    - Change the browser settings to enable mixed content by clicking Tools > Internet Options > Security > Custom Level > Display mixed content: Enable.
- When exporting a process application from Workflow Center using
an HTTPS URL like https://9.115.196.249:9443/ProcessCenter in Microsoft Internet Explorer,
you might receive the following error message: Unable to download ImportExportServlet from 9.115.196.249To
resolve this issue make sure that the Do not save encrypted
pages to disk option is not selected. Navigate to Tools > Internet Options > Advanced > Security.
- When exporting a process application snapshot from the Workflow Center repository
in Process Designer,
you might receive the following error message:Unable to download ImportExportServlet To
resolve this issue, you might need to clear the selected Internet
Explorer V9 Do not save encrypted pages to disk option.
See Microsoft Support.