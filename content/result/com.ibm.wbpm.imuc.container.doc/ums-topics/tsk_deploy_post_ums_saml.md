# Delegating authentication to a Security Assertion Markup Language (SAML) identity
provider

## Before you begin

## Procedure

To configure UMS to delegate authentication to a SAML IdP, perform the following steps:

1 Enable the samlWeb-2.0 feature in UMS.
    1. Edit your custom resource ums\_configuration.custom\_xml file to include the
following snippet:

custom\_xml: |
  <server>
    <featureManager>
      <feature>samlWeb-2.0</feature>
    </featureManager>
    <samlWebSso20 id="defaultSP" httpsRequired="true">
      <authFilter>
        <userAgent id="disable" matchType="equals" agent="samldefault" />
      </authFilter>
    </samlWebSso20>
     <samlWebSso20 id="umsSP" httpsRequired="true" idpMetadata="/opt/ibm/wlp/usr/shared/resources/custom-binaries/idpMetadata.xml" >
      <authFilter>
        <requestUrl id="authorizeEndpoint" urlPattern="/oidc/endpoint/ums/authorize" matchType="contains"/>
        <requestHeader id="allowBasicAuth" matchType="notcontain" name="Authorization" value="Basic" />
      </authFilter>
    </samlWebSso20>
  </server>
Important: Because the SAML configuration is not yet complete, the
authFilter configuration is used to prevent UMS from delegating authentication at
this point. The defaultSP configuration is included to prevent the SAML feature
from creating an incomplete (but active) default configuration.
    2. Apply the UMS configuration, by running the following command:
oc apply -f ums-saml.yamlWhere
ums-saml.yaml is the full custom resource file that includes the previous
snippet.
2 Configure UMS to delegate authentication to the IdP.

1 Create a persistent volume (PV) and a persistent volume claim (PVC) to make theidpMetadata.xml file available to UMS.
    1. Create a ums-saml-pvc.yaml file based on the following
sample:kind: PersistentVolume
apiVersion: v1
metadata:
  name: data-pv
  labels:
    type: icp4a-pv
spec:
  capacity:
    storage: 1Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Retain
  storageClassName: inf-node
  mountOptions:
    - nolock
  nfs:
    path: /data
    server: NFS\_server\_hostname\_or\_IP\_address
---
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: data-pvc
spec:
  accessModes:
    - ReadWriteMany
  volumeMode: Filesystem
  storageClassName: inf-node
  resources:
    requests:
      storage: 1Gi
  selector:
    matchLabels:
      type: icp4a-pv
  volumeName: data-pv
    2. Create the PV and PVC, by running the following command:
oc apply -f ums-saml-pvc.yaml
2. Copy the idpMetadata.xml metadata file for your IdP to the
custom-binaries:

    /data
       +-- custom-binaries
          +-- idpMetadata.xml
During deployment, the operator mounts idpMetadata.xml from this location
into the /opt/ibm/wlp/usr/shared/resources/custom-binaries/ directory on the
file system where UMS is installed.
3 Edit the custom resource file.

1. In the section ums\_configuration, configure the parameter
existing\_claim\_name to point to the persistent claim that you defined in the
previous step and set the parameter use\_custom\_binaries to
true:

ums\_configuration:
    …
    existing\_claim\_name: data-pvc
    …
    use\_custom\_binaries: true
    …
2 Modify the ums\_configuration.custom\_xml property to point to the location ofthe idpMetadata.xml file and configure the authFilter todelegate authentication to the IdP for all URLs that contain the string/oidc/endpoint/ums/authorize . custom\_xml: | <server> <featureManager> <feature>samlWeb-2.0</feature> </featureManager> <samlWebSso20 id="defaultSP" httpsRequired="true"> <authFilter> <userAgent id="disable" matchType="equals" agent="samldefault" /> </authFilter> </samlWebSso20> <samlWebSso20 id="umsSP" httpsRequired="true" idpMetadata="/opt/ibm/wlp/usr/shared/resources/custom-binaries/idpMetadata.xml" > <authFilter> <requestUrl id="authorizeEndpoint" urlPattern="/oidc/endpoint/ums/authorize" matchType="contains"/> <requestHeader id="allowBasicAuth" matchType="notcontain" name="Authorization" value="Basic" /> </authFilter> </samlWebSso20> </server>
    - If you use dedicated pods for UMS capabilities, add the following configuration information to
the custom\_xml parameter in the configuration of the sso pod in
the ums\_configuration section.
    - If you deploy all UMS capabilities in one pod, add the following configuration information to
the custom\_xml parameter in the ums\_configuration section.

```
custom\_xml: |
  <server>
    <featureManager>
      <feature>samlWeb-2.0</feature>
    </featureManager>
    <samlWebSso20 id="defaultSP" httpsRequired="true">
      <authFilter>
        <userAgent id="disable" matchType="equals" agent="samldefault" />
      </authFilter>
    </samlWebSso20>
     <samlWebSso20 id="umsSP" httpsRequired="true" idpMetadata="/opt/ibm/wlp/usr/shared/resources/custom-binaries/idpMetadata.xml" >
      <authFilter>
        <requestUrl id="authorizeEndpoint" urlPattern="/oidc/endpoint/ums/authorize" matchType="contains"/>
        <requestHeader id="allowBasicAuth" matchType="notcontain" name="Authorization" value="Basic" />
      </authFilter>
    </samlWebSso20>
  </server>
```

3. Apply the updated configuration by running the following command:

oc apply -f ums-saml.yaml
4. After the resources are updated, verify that UMS delegates authentication to the identity
provider by navigating your browse to one of the Business Automation Workflow resources that use UMS SSO, for
example UMS Teams:
https:/ums-teams-route/teamserver/ui/Where
ums-teams-route is the host name of the UMS Teams
server.Verify that you are redirected to the SAML endpoint of your identity provider, and that
after entering correct credentials, you are successfully logged into the UMS Teams UI.
5. If UMS does not delegate authentication to the identity provider, verify that the
idpMetadata.xml file is available in the  custom-binaries
directory of the UMS pod by running the following command:
oc exec <ums-pod> -- ls /opt/ibm/wlp/usr/shared/resources/custom-binaries/If
necessary, modify the custom resource to point to that directory, and apply the
changes:<samlWebSso20 
   id="umsSP"
   httpsRequired="true" 
   idpMetadata="/opt/ibm/wlp/usr/shared/resources/custom-binaries/idpMetadata.xml" />

## Results

## What to do next