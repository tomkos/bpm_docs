# Configuring third-party authentication products

To use a third-party authentication product,
you must customize various configuration settings.

This topic describes features that help
you to configure as a participant in an SSO landscape, as well as
limitations in the context of third-party authentication.

## Before you begin

## Procedure

1 Configure your third-party authentication product so thatit does not intercept URLs that Business Automation Workflow usesfor server to server communication. For information abouthow to configure your third-party authentication product, see thedocumentation for that product.
    1. Configure your third-party authentication product to
allow basic access authentication for the context roots that are listed
in the following table. 
Table 1. Context roots that require
basic authentication for technical user IDs

Context roots that require basic authentication
Description

/ProcessCenterInternal/* 	
Workflow Server uses
this context root on Workflow Center to
register or unregister with Workflow Center.

/ProcessServerInternal/*
Workflow Center uses
this context root on Workflow Server for
online deployment. 

/bpm/repo/v1/ejbproxy/*
Desktop Process Designer (deprecated) and Workflow Server use
this context root during debugging and for retrieving version information.

rest/bpm/wle/v1/event
When using document handlers in remote document management systems, ensure
that the document handler can reach this REST API and authenticate as a system account.

Tip: Some forms of third party authentication, such as SPNEGO, use regular expressions
to exclude specific URLs or allow basic authentication. /ProcessCenterInternal/*
starts with /ProcessCenter. In the case of SPNEGO, you cannot configure a filter
criteria of request-url^=ProcessPortal|ProcessCenter|ProcessAdmin. Instead, you
would use
request-url!=ProcessCenterInternal;request-url!=rest/bpm/wle/v1/event;request-url!=ProcessServerInternal;request-url^=ProcessPortal|ProcessCenter|ProcessAdmin.
See SPNEGO web authentication filter values.
    2. Configure your third-party authentication product so
that it does not intercept communications with the web services that
are listed in the following table. 
Table 2. Web service context roots that
must not be intercepted by third-party authentication products

Web service context roots that must not be intercepted
Associated service

/bpmjaxws/*
Business Automation Workflow JAX-WS
Web Services API

/fncmis/*
The embedded Enterprise Content Management Content
Management Interoperability Service (ECM CMIS) web service provider

/RemoteALWeb/*
Remote artifact loader

/teamworks/webservices/*
Teamworks web services

/webapi/*
Business Automation Workflow legacy
web service API
2. Ensure that your third-party authentication product allows
URLs to contain all characters that Business Automation Workflow uses.
The default configuration of your third-party authentication product
might not allow the characters< and >, which Process
Inspector uses. For information about such restrictions
and how you can configure the product to allow these characters, see
the documentation for your third-party authentication product.
3 If your third-party authentication product requires thatall logout actions in clients are redirected to special URLs, youmust change the configuration settings for each Business Automation Workflow clientthat you use. You can set a single consistent logout exitpage by setting the DE level custom property Security.CommonLogoutExitPage ,which is described in Security-hardening properties .If you want to set individual logout exit pages per web application,perform the following actions:

1. Identify the IBM Business Automation
Workflow clients
that you use. For the list of clients, see the following table, noting
that AppCluster is the name of
your application cluster and SupportCluster is
the name of your support cluster. 
Table 3. IBM Business Automation
Workflow client
logout page configuration paths and attribute names

Business Automation Workflow client
AdminConfig command configuration object containment
path
Attribute name for the custom logout page URL
Notes 

Business Process Archive Explorer
 /ServerCluster:SupportCluster

/BPMClusterConfigExtension:

/BPMBPCArchiveExplorer:/

customLogoutPage
This client is available only in the Advanced
deployment environment.

Business Process Choreographer Explorer
 /ServerCluster:SupportCluster

/BPMClusterConfigExtension:

/BPMBPCExplorer:/

customLogoutPage
This client is available only in the Advanced
deployment environment.

Business Rules Manager
 /ServerCluster:AppCluster

/BPMClusterConfigExtension:

/BPMBusinessRules:/

customLogoutPage 
 

Performance Data Warehouse Performance
Admin Console
 /ServerCluster:SupportCluster

/BPMClusterConfigExtension:

/BPMPerformanceDataWarehouse:/

customLogoutPage
 

Process Admin Console
 On Workflow Center:

/ServerCluster:AppCluster

/BPMClusterConfigExtension:

/BPMProcessCenter:/ 

On Workflow Server:

/ServerCluster:AppCluster

/BPMClusterConfigExtension:

/BPMProcessServer:/

processAdminCustomLogout 
 Tip: If you use Process
Inspector in the Process Admin Console, when you log out of Process
Inspector you are redirected to the custom logout page that you specify
for the Process Admin Console.

Workflow Center
 /ServerCluster:AppCluster

/BPMClusterConfigExtension:

/BPMProcessCenter:/

customLogoutPage 
 

Process Portal, Heritage Process Portal
 /ServerCluster:AppCluster

/BPMClusterConfigExtension:

/BPMPortal:/

customLogoutPage 
 

REST API Tester
 On Workflow Center:

/ServerCluster:AppCluster

/BPMClusterConfigExtension:

/BPMProcessCenter:/ 

On Workflow Server:

/ServerCluster:AppCluster

/BPMClusterConfigExtension:

/BPMProcessServer:/

restApiTesterCustomLogout
2 For each Business Automation Workflow clientthat you use, identify the URL of the custom logout page that youwant logout actions to be redirected to. Important: The URLs of the custom logout pages might be misinterpretedif they include the following characters. To ensure that each URL is parsed correctly, you must replacespecial characters with a suitable encoding, such as %20 forspaces, %25 for percent signs, and %26 forampersands. Substituting the predefined symbol &amp; forampersands might not work for all clients. If a URL is difficult toconvert, you can submit it to an online URL encoder to convert itto a suitable string.
    - Spaces
    - Percent signs (%) that are not part of a character
coding, such as %25
    - Ampersand characters (&) that are not part
of a predefined entity, such as &amp;
    - Other special characters
3. If any of the URLs of the custom logout pages are not
on the same host as the Business Automation Workflow server
or do not belong to the same domain, you must set one of the com.ibm.websphere.security.allowAnyLogoutExitPageHost or com.ibm.websphere.security.logoutExitPageDomainList global
security custom properties. Tip: For more information about these custom properties, see Security custom properties.
4 For each Business Automation Workflow clientthat you use, run the necessary administrative commands to set theappropriate custom logout page property to point to the custom logoutpage. For example, to set the custom logout page URL forWorkflow Center to https://security.example.com/pclogout.html ona Windows platform, enter the following commands.

1. Connect to the wsadmin client:D:\IBM\bpm8600\WAS\AppServer\profiles\AdPCDmgr0Profile\bin>wsadmin.bat -conntype NONE -lang jython
WASX7357I: By request, this scripting client is not connected to any server process. Certain 
configuration and application operations will be available in local mode.
WASX7031I: For help, enter: "print Help.help()"
2. Using the appropriate path from Table 3,
get the Workflow Center object
and display its value: wsadmin>path='/ServerCluster:AppCluster/BPMClusterConfigExtension:/BPMProcessCenter:/'
wsadmin>object=AdminConfig.getid(path)
wsadmin>object
'(cells/PCCell1/clusters/AppCluster|cluster-bpm.xml#BPMProcessCenter\_1374114772846)'
3. Using the appropriate attribute name for the custom logout page
URL from Table 3,
display the current value of the custom logout page URL attribute:wsadmin>clp='customLogoutPage'
wsadmin>print AdminConfig.showAttribute(object,clp)
None
4. Set the value of the custom logout page URL attribute:wsadmin>AdminConfig.modify(object,[[clp,'https://security.example.com/pclogout.html']])
''
5. Display the new value to verify that it is correct:wsadmin>print AdminConfig.showAttribute(object,clp)
https://security.example.com/pclogout.html
6. Save the changes.wsadmin>AdminConfig.save()
''
5 Configure logout for IBM ContentNavigator :

1. Create an SSOLogoutPlugin by following the instructions in  Creating Single Sign-on Logout Action in IBM Content
Navigator.
2. Log in to the IBM Content
Navigator
administration.
3. Click the Plug-ins link in the category list.
4. Click New Plug-in.
5. For JAR file path, provide the path to the
SSOLogoutPlugin.jar file.
6. Click Load to load the plug-in.
7. If the plug-in path is correct, you are prompted for the SSO logout redirect URL, for example,
if you are using the User Management Service:
https://<UMS>:<port>/oidc/endpoint/ums/logout.
8. Save the plug-in.
9. iIn the category list, click Desktops.
10. Select IBM Business Automation Workflow Desktop and click
Edit.
11. Select the General tab.
12. Scroll down to the Plug-ins section and select the plug-in that you just
created, which has the default name SSO Logout Plug in.
13. Select the Menus tab.
14. Scroll down to find Banner user session context menu and use the
drop-down to change this menu to the new BannerUserSessionSSOLogoutMenu.
15. Save the Desktop.
4 If you use a third-party Trust AssociationInterceptor (TAI), complete the following actions:

1 If you do not use dedicated security domains, completethe following actions on the global security level:
    1 Enable trust association.
        1. Using the administrative console, navigate to Security > Global Security > Web and SIP Security > Trust Association.
        2. Select Enable trust association.
        3. Click Interceptors, then click New and
enter the name of the TAI Java class name for your third-party authentication
product. For example, for CA SiteMinder, the Java class name is com.netegrity.siteminder.websphere.auth.SmTrustAssociationInterceptor.Tip:  For information about the TAI Java class name for other
third-party authentication products, see the documentation for those
products.
2. Optional: To
ensure that TAI is invoked before Single Sign-On (SSO), set the custom
property InvokeTAIbeforeSSO. Using the administrative
console, navigate to Security > Global Security > Custom properties and click New. Enter the custom
property name com.ibm.websphere.security.InvokeTAIbeforeSSO,
and the name of the TAI Java class for your third-party authentication
provider.
2 If you use dedicated security domains, complete thefollowing actions at the security domain level:

1 Enable trust association for each security domain. For each securitydomain, security\_domain\_name , complete the followingactions in the administrative console:
    1. Navigate to Security > Security
domains > security\_domain\_name > Trust Association.
    2. Select Customize for this domain.
    3. Select Enable trust association.
    4. Click Interceptors, then click New and
enter the name of the TAI Java class name for your third-party authentication
product. For example, for CA SiteMinder, the Java class name is com.netegrity.siteminder.websphere.auth.SmTrustAssociationInterceptor.Tip:  For information about the TAI Java class name for other
third-party authentication products, see the documentation for those
products.
2. Optional: To
ensure that TAI is invoked before Single Sign-On (SSO), set the custom
property InvokeTAIbeforeSSO. Use the administrative
console to set the custom property for each security domain, security\_domain\_name.
Navigate to Security > Security
domains > security\_domain\_name > Custom properties and click New.
Enter the custom property name com.ibm.websphere.security.InvokeTAIbeforeSSO,
and the name of the TAI Java class for your third-party authentication
provider.
5. Complete the actions that are described
in Configuring the propagation of HTTP headers and cookies for a third-party authentication environment.
6. Complete the actions that are described
in Configuring endpoints to match your topology.
7 Verify that Business Automation Workflow workscorrectly with your third-party authentication product. For each Business Automation Workflow clientthat you use, verify that you can log on, that the client is fullyfunctional, and that logging out redirects correctly. Thefollowing table describes some possible problems and how to solvethem.Table 4. Diagnosing possible problems with third-party authenticationproducts Problem Possible causes Solutions When you are logged on to a Workflow Center , Workflow Server isnot visible. If you have separate web servers for internaland external traffic, Workflow Server mightnot be accessible from the Workflow Center Check and adapt the endpointsto suit your setup as described in Customizing the Workflow Server settings used to connect to Workflow Center . Clients do not display all IBM Business AutomationWorkflow datacorrectly. The desktop Process Designer (deprecated) does not workproperly. Your third-party authentication product mightuse a login form that desktop Process Designer cannotprocess. Either make sure that your third-party authenticationproduct is not intercepting calls to the Workflow Center URLthat is used by desktop Process Designer orimplement an authenticator plug-in to handle the login form. For more information about creatinga plug-in for the desktop Process Designer loginauthenticator extension point, see Configuring a custom authenticator plug-in .Tip: Thedesktop Process Designer normally uses only HTTP calls although if httpProtocolOnly is set to false, amixture of HTTP, RMI, and JMS calls are used, as described in Configuring the httpProtocolOnly property for ProcessDesigner . Using this setting can simplify how your third-party authentication product must beconfigured.

| Problem                                                                      | Possible causes                                                                                                                                                                                                           | Solutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| When you are logged on to a Workflow Center, Workflow Server is not visible. | If you have separate web servers for internal and external traffic, Workflow Server might not be accessible from the Workflow Center                                                                                      | Check and adapt the endpoints to suit your setup as described in Customizing the Workflow Server settings used to connect to Workflow Center.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Clients do not display all IBM Business Automation Workflow data correctly.  | Calls to the remote artifact loader are being intercepted. If you have multiple deployment environments, each one has its own remote artifact loader, and the endpoints might not be configured to reflect your topology. | Make sure that your third-party authentication product is not intercepting calls to the RAL context root /RemoteALWeb. You might need to configure the REMOTE\_AL endpoint for each deployment environment, as described in Configuring endpoints to match your topology.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| The desktop Process Designer (deprecated) does not work properly.            | Your third-party authentication product might use a login form that desktop Process Designer cannot process.                                                                                                              | Either make sure that your third-party authentication product is not intercepting calls to the Workflow Center URL that is used by desktop Process Designer or implement an authenticator plug-in to handle the login form. For more information about creating a plug-in for the desktop Process Designer login authenticator extension point, see Configuring a custom authenticator plug-in.Tip: The desktop Process Designer normally uses only HTTP calls although if httpProtocolOnly is set to false, a mixture of HTTP, RMI, and JMS calls are used, as described in Configuring the httpProtocolOnly property for Process Designer. Using this setting can simplify how your third-party authentication product must be configured. |

## Results

- Configuring a custom authenticator plug-in

IBM Business Automation Workflow Workflow Center supports the use of a custom authenticator plug-in to work with your third-party authentication single sign-on (SSO) environment.
- Configuring the propagation of HTTP headers and cookies for a third-party authentication environment

If you use a third-party authentication solution with Business Automation Workflow, you can specify a list of headers and cookies that the federated REST API must propagate.
- Configuring SAML in IBM Business Automation Workflow

You can configure Security Assertion Markup Language (SAML) in IBM Business Automation Workflow Version 19.0.0.3 and later.