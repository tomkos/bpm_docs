# Setting the time zone in Business Automation Workflow on containers

## Before you begin

## Procedure

1 Choose one of the following methods to set the time zone:
    - In the custom resource (CR) file, change the timezone parameter to the
time zone you want. For example:baw\_configuration:
  - name: bawins1
    ## JVM options separated with spaces, for example: -Dtest1=test -Dtest2=test2.
    environment\_config:
        timezone: Etc/UTC
    - In the custom resource (CR) file, change the jvm\_customize\_options
parameter to the time zone you want. For example:
baw\_configuration:
  - name: bawins1
    ## JVM options separated with spaces, for example: -Dtest1=test -Dtest2=test2.
    jvm\_customize\_options: "-Duser.timezone=America/Chicago"
2. Modify the existing containers by running the kubectl apply command on the
custom resources .yaml file.

kubectl apply -f custom\_resources.yaml

## Results

The operator modifies the application to use the new configmap and updates
the /config/configDropins/overrides/jvm.options file.

## Related information

- Runtime and Workstream Services
parameters