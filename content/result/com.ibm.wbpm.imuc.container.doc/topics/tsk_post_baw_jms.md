# Customizing an independent JMS server for Business Automation Workflow on containers

## About this task

The embedded JMS server, running on the Workflow server pod, is configured by default. You can
update the custom resource (CR) file to deploy an independent JMS server.

## Procedure

To deploy an independent JMS server:

1. Edit the CR and add is\_embedded: false to
baw\_configuration.jms for IBM® Business Automation
Workflow Runtime, as shown in the
following example:

baw\_configuration:
-  name: instance1
   jms:
      is\_embedded: false
2. You can customize the JMS parameters, edit the CR file, and add the customized parameters
to baw\_configuration.jms, as shown in the following example: 
baw\_configuration:
-  name: instance1
   jms:
      is\_embedded: false
      ## Enable/disable logging where logs can be sent to Elasticsearch, default is 'false'
      logging\_enabled: false
      ## Specify the group which Kubernetes will change the permissions of all files in volumes to when volumes are mounted by a pod, which is specified on the pod level. With scc(on OCP) or psp(on Kubernetes), you need to map the service account to proper scc or psp, for example on OCP, use commnad line: `oc adm policy add-scc-to-user anyuid -z wfps-instance1-sa -n NAMESPACE`
      fs\_group: ""
      image:
        ## Image name for Java Messaging Service container.
        repository: cp.icr.io/cp/cp4a/baw/jms
        ## Image tag for Java Messaging Service container.
        tag: "24.0.0"
        ## Pull policy for Java Messaging Service container. Default value is IfNotPresent. Possible values are IfNotPresent, Always.
        pull\_policy: IfNotPresent
      tls:
        ## TLS secret name for Java Message Service (JMS)
        tls\_secret\_name: ibm-jms-tls-secret
      resources:
        limits:
          ## Memory limit for JMS configuration
          memory: "1Gi"
          ## CPU limit for JMS configuration
          cpu: "1000m"
        requests:
          ## Requested amount of memory for JMS configuration
          memory: "512Mi"
          ## Requested amount of CPU for JMS configuration
          cpu: "100m"
      storage:
        ## Whether to enable persistent storage for JMS
        persistent: true
        ## Size for JMS persistent storage
        size: "1Gi"
        ## Whether to enable dynamic provisioning for JMS persistent storage
        use\_dynamic\_provisioning: true
        ## Access modes for JMS persistent storage
        access\_modes:
        - ReadWriteOnce
        ## Storage class name for JMS persistent storage
        storage\_class: "{{ shared\_configuration.storage\_configuration.sc\_fast\_file\_storage\_classname }}"
      node\_affinity:
        # Values in this field will be used as kubernetes.io/arch selector values. Default values are ['amd64','s390x','ppc64le']
        deploy\_arch: []
        #-------------------------------------
        # custom\_node\_selector\_match\_expression will be added in node selector match expressions.
        # It accepts array list inputs. You can assign multiple selector match expressions except (kubernetes.io/arch)
        # Example input:
        # - key: kubernetes.io/hostname
        #   operator: In
        #   values:
        #     - worker0
        #     - worker1
        #     - worker3
        #-------------------------------------
        custom\_node\_selector\_match\_expression: []
      # Values in this field will be used as annotations in all generated pods.
      # They must be valid annotation key-value pairs.
      # Example:
      # custom\_annotations:
      #   key1: value1
      #   key2: value2
      custom\_annotations: {}
      # Values in this field will be used as labels in all generated pods
      # It must be valid label key value pairs
      # Example:
      # custom\_labels:
      #   key1: value1
      #   key2: value2
      custom\_labels: {}
      ##  JMS Server custom plain XML snippet
      ##  custom\_xml: |+
      ##    <server>
      ##      <!-- custom propeties here -->
      ##    </server>
      custom\_xml:
      ## JMS custom XML secret name that contains custom configuration in Liberty server.xml,
      ## put the custom.xml in secret with key "sensitiveCustom.xml"
      ## kubectl create secret generic jms-custom-xml-secret --from-file=sensitiveCustom.xml=./custom.xml
      custom\_secret\_name:
3. Apply the updated CR.