<!-- image -->

# Considerations for deploying service applications on clusters

- Will users of the application require the processing power and
availability provided by clustering?If so, clustering is the correct
solution. Clustering will increase the availability and capacity of
your applications.
- Is the cluster correctly prepared for service applications?You
must configure the cluster correctly before deploying and starting
the first application that contains a service. Failure to configure
the cluster correctly prevents the applications from processing requests
correctly.
- Does the cluster have a backup?You must deploy the application
on the backup cluster also.

## Cross-cluster modules

- One module has a configured binding that generates JNDI resources.
- Another module is configured to use those generated JNDI resources.
- The modules are deployed in different clusters.