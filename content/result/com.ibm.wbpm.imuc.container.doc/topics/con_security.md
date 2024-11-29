# Red Hat OpenShift security and compliance

You can use monitoring and compliance enforcement tools on your clusters to check that your
security policies are working the way that you expect them to work. You can also define a
ResourceQuota for each namespace to address common attack scenarios. A
ResourceQuota object can restrict the number of pods and the CPU consumption and in
doing so set hard limits on the amount of node resource usage.

- SECCOMP (Secure Computing Mode) profiles
- Service account tokens

On OpenShift Container Platform 4.11+, all containers now use the RuntimeDefault
seccomp profile by default. The RuntimeDefault profile provides a list of system
calls that are allowed. For example, depending on your corporate policy, you might want to set the
seccomp profile to be Unconfined or create a custom Localhost
profile. However, your pods might fail if your custom profile is more restrictive than the default
setting. To use a custom profile, complete the following steps.

1. Create a seccomp profile in Machine Config.
2. Set the seccomp\_profile.type to Localhost for selected
pods in the custom resource, and assign the new profile (for example
<my\_profile>.json) to the localhost\_profile
parameter.seccomp\_profile:
  type:  'Localhost'
  localhost\_profile: 'profile/<my\_profile>.json'The
sc\_seccomp\_profile parameter can be set for all workloads in a deployment. Set
the seccomp\_profile at the component level to affect only that workload. 
Learn more...

In Kubernetes, a ServiceAccount is granted permissions to access Kubernetes APIs
and is associated with one or more pods. Calling a Kubernetes API requires that a
ServiceAccount token is passed for authentication and authorization. For easy
access to Kubernetes APIs, the ServiceAccount token is mounted into all associated
pods even though many pods have no requirement to call these APIs. Business Automation Workflow configures service
accounts and pods to avoid automatically mounting the ServiceAccount token to
reduce attack surface.