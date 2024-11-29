# Troubleshooting the IBM Business Automation
Machine Learning Server

## Checking the status of Machine Learning Server

```
./bin/ba-ml-server-status
```

## Viewing Machine Learning Server
logs

```
Service-issuing-log | message
```

```
./bin/ba-ml-server-logs
```

## Running Intelligent Task Prioritization model training

```
The data retrieved from BAI server has size 0. Please make sure you have enough data from BAI
nextbesttask.custom\_errors.InsufficientTrainingData: InsufficientTrainingData: the data retrieved from BAI server has size 0. Please make sure you have enough data from BAI 2023-11-03 14:09:24,012 - nbt - INFO - init - Please retrain the model later by accessing /nbt/train when there is sufficient data. Or wait for the regular training session which will happen automatically periodically
```

By
default, model training is automatically started every Sunday at 3:00 AM UTC and also when the
Machine Learning Server is
restarted. For more information about scheduling retraining, see IBM Business Automation Workflow Runtime and Workstream Services
parameters.

1. Get the credential information from the secret with the suffix
ibm-mls-itp-admin-secret.
2. Get the Intelligent Task Prioritization
server certificate file location from the Intelligent Task Prioritization pod. The Intelligent Task Prioritization server pod name has the
prefix <custom\_resource\_name>-mls-itp. For example, the JSON
path might look similar to:spec:
  containers:
    volumeMounts:
      ... ...
      - name: certificate-file
         mountPath: /nextbesttask/nextbesttask/certs/local-server.crt
         subPath: local-server.crt
      ... ...
3. Get the Intelligent Task Prioritization
server service name, which is in the format
<custom\_resource\_name>-mls-itp-service. Make sure that it
shows up in the list of created services.
4. Go to your Intelligent Task Prioritization
container in your OpenShift® Container
Platform console, or by using
the oc or kubectl command.
5. Using the information retrieved in the previous steps, complete your model training by running
the following
command:curl https://<Intelligent\_Task\_Prioritization\_service\_name>:8000/train?dataset=bai -u <admin\_username>:<admin\_password> --cacert <server\_certificate\_filepath>For
example, the resulting command might look similar
to:curl https://cpfc-pg-wfs-fvt-bai-2302-mls-itp-service.auto-6vlw1.svc.cluster.local:8000/train?dataset=bai -u ITP-kcAMgSjz:password --cacert /nextbesttask/nextbesttask/certs/local-server.crt

## Troubleshooting IBM Business Automation
Insights

## Troubleshooting Business Automation Workflow