# Preventing cross site request forgery

```
{
  "refresh-groups": false,
  "requested-lifetime": 7200
}
```

The token is returned as a string in the csrf\_token property of the response
object. Every call to Workflow  REST API operations must include a valid token in the HTTP header
BPMCSRFToken.

Any attempt to call a Workflow REST API with an expired token fails with HTTP response code 403
and error\_number CWTBG0651E in the response, which indicates that the token could
not be verified and that the token must be renewed. To retrieve a new token, the client application
must call the /bpm/system/login API again. The client application can then use the
new token to resubmit the failed request.

```
https://subscription\_hostname/cloud\_offering/environment/bpm/system/login
```

- subscription\_hostname can be one of the following values:
bpm.ibmcloud.com or automationcloud.ibm.com
- cloud\_offering can take one of the following values:
    - baw for Business Automation Workflow on Cloud
    - dba for cloud subscriptions with multiple IBM® Cloud Pak for
Business Automation as a Service offerings,
including Business Automation Workflow on Cloud
- environment has the value dev for the development
environment, test for the test environment, or run for the
production (runtime) environment. A token for one environment is not valid for another
environment.