# Error displaying embedded IBM Content
Navigator window in coach

If you are using IBM® Business Automation
Workflow
V19.0.0.3 or V20.0.0.1 with embedded IBM Content
Navigator topology, when you embed an
IBM Content
Navigator window into a coach using
a custom HTML iFrame, an error message appears.

```
Refused to display 'https://localhost:12319/navigator/?desktop=bawadmin'; in a frame because it set 'X-Frame-Options' to 'deny'.
```

## About this task

```
<outbound-rules>
<add-header name="Cache-Control" value="no-cache, no-store" path=".*/|.*\.jsp|.*/jaxrs/.*|.*/api/.*"/>
<add-header name="Content-Security-Policy"
value="default-src 'self' blob: https:; font-src 'self' data: blob: https:; img-src 'self' data: blob: https:; script-src 'self' 'unsafe-inline' 'unsafe-eval' https:; worker-src 'self' blob: https:; style-src 'self' 'unsafe-inline' https:; frame-ancestors 'self'"
path="/.*"/>
<add-header name="Referrer-Policy" value="same-origin" path="/.*"/>
<add-header name="Strict-Transport-Security" value="max-age=7776000; includeSubdomains" path="/.*"/>
<add-header name="X-Content-Type-Options" value="nosniff" path="/.*"/>
<add-header name="X-Frame-Options" value="sameorigin" path="/.*"/>
<add-header name="X-Permitted-Cross-Domain-Policies" value="none" path="/.*"/>
<add-header name="X-XSS-Protection" value="1; mode=block" path="/.*"/>
</outbound-rules>
```

## Procedure

1. Stop the environment.
2. Update the ESAPIWafPolicy.xml file under the
DmgrProfile path, with the expected policies: 
profile\_root\_name\Dmgr profile\config\cells\Cell\_Name\applications\navigatorEAR\_app\_cluster\_name.ear\deployments\navigatorEAR\_app\_cluster\_name\navigator.war\WEB-INF\ESAPIWafPolicy.xml
3. Restart the environment.