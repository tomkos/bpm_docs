# Troubleshooting a failure to access help topics

You can find the documentation for IBM Business Automation
Workflow on the
web at https://www.ibm.com/docs/baw/20.x. If you
use the embedded help system that is installed with the Business Automation Workflow product, you
are using this site to access the latest documentation. For example,
if you click the Help link in IBM Process
Designer, the
embedded help system accesses the help documentation at that link.

## Reconfiguring proxy settings

The product
documentation is found at https://www.ibm.com/docs/baw/20.x.
If you can access the product documentation at that URL in a browser,
but links to help topics from the product fail, you probably have
a proxy server between your product and the documentation site. Check
to see whether the browser is configured to use a proxy server. If
it is, you need to configure the WebSphere server to communicate with
that same proxy server.

In the WebSphere Application Server
admin console, set the http.proxyHost and http.proxyPort properties
to point to the proxy host and port that are in use. You can find
instructions in the following WebSphere® Application
Server topics: Configuring additional HTTP transport properties
using the JVM custom property panel in the administrative console and Configuring additional HTTP transport properties
using the wsadmin command-line tool.

## Downloading and installing IBM Business Automation
Workflow documentation

If
you need to work offline, you need to download the documentation files
and install them into the same location as the Business Automation Workflow product. Downloading
the documentation files requires a working Internet connection. When
there is a new release of the product, you need to update your installed
documentation to keep it current. For instructions on downloading
and installing the documentation, see Accessing the IBM Business Automation Workflow documentation offline.

## Configuring help for IBM Integration
Designer

If
you use the embedded help system that is installed with the Business Automation Workflow product, you
are using this site to access the current version of this information.
For example, if you click the Help link inside Integration Designer, the embedded
help system automatically accesses the help documentation at that
link. If you have access to the web but you are not seeing the Business Automation Workflow documentation,
check to see if the remote help is enabled. Select Window > Preferences > Help > Content.
If https://www.ibm.com/docs/baw/20.x/com.ibm.wbpm.auth.stp.doc/topics/cbpm\_stpovw.html is
not enabled, select it and click Enable. Click Apply and OK.
Help is then available.