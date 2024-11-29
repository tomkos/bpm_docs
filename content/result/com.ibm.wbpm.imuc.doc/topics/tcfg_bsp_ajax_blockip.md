# Blocking IP addresses using the Business Space Ajax proxy

## About this task

If
you want to restrict access to specific IP addresses, you can edit
the Ajax proxy to filter IP addresses to allow or deny access. You
define blocklist or allowlist rules in the proxy-config.xml file.

## Procedure

1. Open the proxy-config.xml file.
 For information about where to find the Ajax proxy file, see Configuring the Business Space Ajax proxy.
2 Add filter rules that allow or deny access. Todefine a blocklist rule for a particular IP address or set of addresses,use a proxy:deny element. To define an allowlistrule for a particular IP address or set of addresses, use a proxy:allow element.The filter rules are applied in order, with the last applicable filterrule taking precedence over previous filter rules. Addthe <proxy:ipfilter> information under theproxy rules of the proxy-config.xml file (afterproxy policies and before </proxy-rules> ). <proxy:ipfilter><proxy:deny>9.6.0.0/255.255.0.0</proxy:deny><proxy:allow>9.6.1.0/255.255.255.0</proxy:allow><proxy:deny>9.6.1.4</proxy:deny></proxy:ipfilter> In this example, the IP filter performs the followingfilters: So, in this case, the proxy would not allow access toIP address 9.6.2.5 or 9.6.120.7 and would respond with the followingmessage: BMWPX0018E: The specified target hosts IP-address is prohibitedby rule. The proxy would allow access to 9.6.1.5 or 9.6.1.120but would deny access to 9.6.1.4. As you add new filter rules,you can combine them in several ways, but the proxy always handlesthem in order. The last matching rule will always take effect, regardlessof any allow and deny rules that come before it.

To
define a blocklist rule for a particular IP address or set of addresses,
use a proxy:deny element. To define an allowlist
rule for a particular IP address or set of addresses, use a proxy:allow element.
The filter rules are applied in order, with the last applicable filter
rule taking precedence over previous filter rules.

Add
the <proxy:ipfilter> information under the
proxy rules of the proxy-config.xml file (after
proxy policies and before </proxy-rules>).

```
<proxy:ipfilter>
<proxy:deny>9.6.0.0/255.255.0.0</proxy:deny>
<proxy:allow>9.6.1.0/255.255.255.0</proxy:allow>
<proxy:deny>9.6.1.4</proxy:deny>
</proxy:ipfilter>
```

    - blocks all 9.6.*.* IP addresses
    - allows 9.6.1.* but blocks the specific IP address 9.6.1.4

So, in this case, the proxy would not allow access to
IP address 9.6.2.5 or 9.6.120.7 and would respond with the following
message: BMWPX0018E: The specified target hosts IP-address is prohibited
by rule.

The proxy would allow access to 9.6.1.5 or 9.6.1.120
but would deny access to 9.6.1.4.

As you add new filter rules,
you can combine them in several ways, but the proxy always handles
them in order. The last matching rule will always take effect, regardless
of any allow and deny rules that come before it.

3. Complete the Ajax proxy configuration to suit your environment.
For information, see Configuring the Business Space Ajax proxy.