# Accessing the SharePoint CMIS provider

## About this task

```
http://hostName:portNumber/fncmis/RepositoryService
```

However,
a SharePoint CMIS web service URL does not follow the same naming convention because the URL is not
appended with the service name. Instead, the URL uses a naming convention that is similar to the
following
examples:

```
http://hostName:portNumber/\_vti\_bin/cmis/soap/RepositoryService.svc/basic
http://hostName:portNumber/\_vti\_bin/cmis/soap/RepositoryService.svc/kerberos
http://hostName:portNumber/\_vti\_bin/cmis/soap/RepositoryService.svc
```

When an attempt is made to contact the SharePoint server using the
following URL, a connection cannot be made because the web service address is not
known:

```
http://hostName:portNumber/\_vti\_bin/cmis/soap/RepositoryService
```

To
enable the workflow system to accommodate the naming convention used in SharePoint, Microsoft URL
Rewrite Module 2.0 for Internet Information Services (IIS) 7 is required. The URL Rewrite Module
provides a rules-based mechanism to rewrite the incoming request URL from the workflow system before
it is processed by the web server. For example, consider the following request
URL:

```
http://hostName:portNumber/\_vti\_bin/cmis/soap/RepositoryService
```

The
URL Rewrite Module enables the URL to be rewritten in the SharePoint format that is shown in the
following
example:

```
http://hostName:portNumber/\_vti\_bin/cmis/soap/RepositoryService.svc
```

To
enable the URL Rewrite Module to rewrite incoming request URLs from the workflow system, the
following tasks need to be completed:

- Download URL Rewrite Module 2.0 for Microsoft IIS 7
- Define the rewrite rules in IIS Manager
- Access the SharePoint CMIS Provider from the designer

To perform these tasks:

## Procedure

1 Download URL Rewrite Module 2.0 for IIS 7 by completingthe following steps:
    1. Verify that you have IIS 7 installed.
    2 If Microsoft URL Rewrite Module 2.0 is not already installedin your IIS 7 installation, download it from one of the followingweb pages and then install it using the instructions that are foundat one of the following web pages:
        - (x64) http://www.microsoft.com/en-us/download/details.aspx?id=7435
        - (x86) http://www.microsoft.com/en-us/download/details.aspx?id=5747
2 Define the rewrite rules in IIS Manager by completing thefollowing steps:

1. On your desktop, select Start > Administrative
Tools > Internet Information Services (IIS) Manager. IIS
Manager opens.
2. Select a connection.
3. Select IIS > URL Rewrite.
4. Select Rule > Inbound rules > Blank rule.
5. In the Name area, specify CMIS
URL rewrite rule.
6 In the Match URL section, completethe following steps:
    1. In the Requested URL drop-down list, select Matches
the Pattern.
    2. In the Using drop-down list, select Regular
Expressions.
    3. In the Pattern field, specify the following
pattern:^.*cmis/soap/(.*)$
    4. Select Ignore case.
7 In the Conditions section, completethe following steps:

1. Click Add. The Add Condition dialog box
opens.
2. In the Condition input field, specify the
following condition input:{R:1}
3. In the Check if input string drop-down
list, select Does Not Match the Pattern.
4. In the Pattern field, specify the following
pattern:(.*).svc(.*)
5. Select Ignore case.
6. Click OK.
8 In the Actions section, completethe following steps:

1. In the Action type drop-down list, select Rewrite.
2. In the Rewrite URL field, specify a rewrite
URL that is appropriate for your configuration. For example:{R:0}.svc
3. Select Append query string.
9. On the right side of the page, click Apply to
save the changes.
3 Access the SharePoint CMIS Provider from the designer by completing the followingsteps:

1. Open the Process App Settings editor and select the Servers tab.
2. In the Server Details and Server
Locations sections, specify the appropriate server information for your SharePoint
installation. Ensure that you specify Enterprise Content Management Server in
the Type field. Also ensure that you specify the correct context path in the
Context Path field. The default context path is: 
\_vti\_bin/cmis/soap
3. Click Test Connection to ensure that a successful connection
exists.