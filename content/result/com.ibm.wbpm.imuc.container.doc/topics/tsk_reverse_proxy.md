# Using a reverse proxy for Business Automation Workflow on
containers

## About this task

## Procedure

1. The external reverse proxy endpoint must be used as the deployment hostname suffix for
stand-alone Business Automation Workflow
on containers. Update the property
shared\_configuration.sc\_deployment\_hostname\_suffix to the hostname suffix value of
the reverse proxy endpoint.

shared\_configuration:
   sc\_deployment\_hostname\_suffix: <namespace>.proxy.external.com 

Tip: To route inner HTTPS requests successfully, with a hostname
endpoint format like *-<namespace>.proxy.external.com, you can update your cloud
platform DNS hostname IP address mappings. This tip applies to the stand-alone Business Automation Workflow on containers
ingress controller in cloud platform nodes and pods.
2. Optional: 
Define the customized hostname as the separate external service endpoint for each
component.

baw\_configuration:
  - name: bawins1
    service\_type: "Route" 
    hostname: mybaw-<namespace>.proxy.external.com

If you leave the field value of the component hostname as null or empty in your deployed CR, the
workflow operator sets the default values.
baw-bawins1-<namespace>.proxy.external.com
     cmis-<namespace>.proxy.external.com
     cpe-<namespace>.proxy.external.com
     cpe-stless-<namespace>.proxy.external.com
     graphql-<namespace>.proxy.external.com
     navigator-<namespace>.proxy.external.com
     rr-<namespace>.proxy.external.com
     ums-profiles-<namespace>.proxy.external.com
     ums-scim-<namespace>.proxy.external.com
     ums-sso-<namespace>.proxy.external.com
     ums-teams-<namespace>.proxy.external.com
     ae-workspace-<namespace>.proxy.external.com
     ums-<namespace>.proxy.external.com
     pfs-<namespace>.proxy.external.com
     ………

You can view the service external hostname values, by using the command kubectl get
route -n <workflow namespace>
3. After you get the route hostname for each component service, make sure that the DNS mappings to
the reverse proxy server are configured for each external client. Then each client can use the same
route hostname endpoints to access the reverse proxy server.

<Reverse Proxy IP Address>        baw-bawins1-<namespace>.proxy.external.com
<Reverse Proxy IP Address>        cmis-<namespace>.proxy.external.com
<Reverse Proxy IP Address>        cpe-<namespace>.proxy.external.com
<Reverse Proxy IP Address>        cpe-stless-<namespace>.proxy.external.com
<Reverse Proxy IP Address>        graphql-<namespace>.proxy.external.com
<Reverse Proxy IP Address>        navigator-<namespace>.proxy.external.com
<Reverse Proxy IP Address>        rr-<namespace>.proxy.external.com
<Reverse Proxy IP Address>        ums-profiles-<namespace>.proxy.external.com
<Reverse Proxy IP Address>        ums-scim-<namespace>.proxy.external.com
<Reverse Proxy IP Address>        ums-sso-<namespace>.proxy.external.com
<Reverse Proxy IP Address>        ums-teams-<namespace>.proxy.external.com
<Reverse Proxy IP Address>        ae-workspace-<namespace>.proxy.external.com
<Reverse Proxy IP Address>        ums-<namespace>.proxy.external.com
<Reverse Proxy IP Address>        pfs-<namespace>.proxy.external.com

In this example, <Reverse Proxy IP Address> is the external reverse proxy
server IP address and the component service hostnames are the same as your end-point routes on
workflow deployment. To view the component service hostname, use the kubectl get route -n
<your namespace> command.
4. Configure the reverse proxy to pass HTTPS requests from the external client to its backend
cloud platform ingress controller. Configure the HTTPS upstream forwarding, as in the following
example using Nginx.

server {
……………
location / {
………..
        rewrite ^ $request\_uri;
        rewrite ^/(.*) $1 break;
            proxy\_pass https://baw-server/$uri;
………….. }
……}
upstream baw-server {
      server <cloud platform ingress controller IP Address>:443;
      …..
}
           …….
5 Configure the reverse proxy to pass headers from your external client. Set the host headervalue and forward the request to the backend workflow system, as shown in the following exampleusing Nginx. Otherwise, the external client browser page displays an application notfound error. proxy\_set\_header Host $host; Important: Be aware of the followingconsiderations for the reverse proxy:

```
proxy\_set\_header Host $host;
```

    - Pass the header from the request. 
Otherwise, the redirect for the authentication fails due to the missing header and an exception
is shown. The system tries to re-create a header by using the internal URL. This attempt fails
because the endpoint is not known externally and is not registered in the UMS.
CWOAU0073E: An authentication error occurred.Try closing the web browser and authenticating again, or contact the site administrator if the problem persists.
    - If the file size is large when you upload files or install a workflow application from workflow
Swagger UI, you might see an
error.413 Request Entity Too LargeThe package
size for workflow application installations is larger than the allowed size for uploading a file to
the reverse proxy. To correct this, you can set a larger value for uploading file size limit in the
reverse proxy
server.client\_max\_body\_size 100M
    - Do not overwrite the referer on the header. 
Otherwise, UMS and Business Automation Workflow cannot correctly
load artifacts and an exception is raised. This security issue blocks the artifacts of the internal
web application firewall.
Cross-Site Request Forgery (CSRF) protection: unacceptable REFERER header: https:\/\/ums-sso-baw-prod.xxxxx\/ums\/login. Expected: host ums-sso-baw-prod.yyyyy and port 443
    - Do not activate compression.
IBM Business Automation
Navigator and IBM Administration Console for
Content Platform Engine (ACCE) are not
supported. Some artifacts do not load correctly because of mistakes on the path.