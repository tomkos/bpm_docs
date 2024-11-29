# Configuring event emitters with IBM Cloud Pak for Business
Automation
Business Automation Insights

## Procedure

To start working with Business Automation Insights, follow the
instructions for installing and configuring the product to capture events emitted by your Business Automation Workflow instance.

1. Follow the installation instructions starting with Preparing to install Business Automation Insights.
2. Configure the BPM and Case emitters by follow the instructions in Configuring event emitters.

## Troubleshooting

- For troubleshooting the Business Automation Insights installation, see
Troubleshooting event emitters on Kubernetes.
- Enable tracing to troubleshoot event emitter issues, by following the instructions in Enabling tracing for BPM event emitter and Machine Learning Server and Enabling detailed tracing on the Case event emitter.

## Additional information

- Reference for BPMN events
- Reference for Case events
- Reference for BPEL events

If you use
Performance Data Warehouse to analyze process performance, you can
prime Business Automation Insights with
historical process-related data to give you more meaningful data for
your Business Automation Insights dashboards.
Use the Business Automation Workflow POST /std/bpm/historical\_data\_playback Operations
REST API to play back the process-related data in Performance Data
Warehouse, generate the corresponding events, and transfer them to Business Automation Insights for
further processing. For more information about the REST API, see Operations REST APIs.