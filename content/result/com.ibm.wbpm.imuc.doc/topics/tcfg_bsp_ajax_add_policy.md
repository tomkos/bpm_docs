# Adding proxy policies to the Business Space Ajax proxy

## About this task

The Business Space Ajax
proxy contains predefined policies to some IBM URLs, but is not open
to all URLs. If you use resources from remote sites in Business Space,
add new policies in the proxy-config.xml file
following the formatting of one of the predefined policies, such as
the <proxy:policy url="http://www-03.ibm.com/*" acf="none"
basic-auth-support="true">, to allow content from the
remote sites to work properly in the Web Feed widget and the Google
Gadgets widget.

If you had a previous version of Business Space,
and you want the Ajax proxy to continue to be open to all URLs as
it was in the previous version, change <proxy:policy url="endpoint://*"
acf="none" basic-auth-support="true"> to <proxy:policy
url="*" acf="none" basic-auth-support="true">.

## Procedure

1. Open the proxy-config.xml file.
 For information about where to find the Ajax proxy file, see Configuring the Business Space Ajax proxy.
2. To restrict the Ajax proxy so that it allows access to
only specific endpoints, make sure that the proxy-config.xml file
contains <proxy:policy url="endpoint://*" acf="none" basic-auth-support="true"> instead
of <proxy:policy url="*" acf="none" basic-auth-support="true">.
3. Add policies for remote content. The following
predefined policies allow access to web feeds from specific remote
sites so that they work properly in the Web Feed widget.
<proxy:policy url="http://www.ibm.com/*" acf="none" basic-auth-support="true">
<proxy:actions>
<proxy:method>GET</proxy:method>
</proxy:actions>
</proxy:policy>

<proxy:policy url="http://www-03.ibm.com/*" acf="none" basic-auth-support="true">
<proxy:actions>
<proxy:method>GET</proxy:method>
</proxy:actions>
</proxy:policy>

<proxy:policy url="http://www.redbooks.ibm.com/*" acf="none" basic-auth-support="true">
<proxy:actions>
<proxy:method>GET</proxy:method>
</proxy:actions>
</proxy:policy>To allow access to additional
web feeds, Google Gadgets, or other remote content, add a policy like
the following example:
<proxy:policy url="http://your\_URL" acf="none" basic-auth-support="true">
<proxy:actions>
<proxy:method>GET</proxy:method>
</proxy:actions>
</proxy:policy>
4. Complete the Ajax proxy configuration to fit your environment.
 See Configuring the Business Space Ajax proxy.