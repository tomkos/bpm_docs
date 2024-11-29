# Federating Business Automation Workflow on
containers

After you configure IBM® Process Federation
Server, you can deploy
and federate IBM Business Automation
Workflow on
containers servers when Process Federation Server is in the same
namespace.

## Before you begin

## Procedure

1. Add the following configuration to Cloud Pak for Business Automation CR to enable
federation. 
baw\_configuration:
  - name: "<Required>"
    ## Whether the Business Automation Workflow instance hosts federated Process Portal.
    ## The value is either true or false.
    host\_federated\_portal: <Required>
    elasticsearch:
      endpoint: "<Required>"
      admin\_secret\_name: "<Required>"
    process\_federation\_server:
      # Hostname of PFS. You could get it from external URL in PFS CR status.
      hostname: "<Required>"
      # context root prefix, e.g. "/pfs". You could get it from external URL in PFS CR status.
      context\_root\_prefix: "<Required>"
2. Apply your custom resource.
3 Verify your configuration by running the Process Federation Server federation APIto make sure Business Automation Workflow is federated.
    1. To get the Process Federation Server REST base URL,
run the command. 
oc get pfs cr\_name -o=jsonpath='{.status.endpoints[1].uri}'
    2. Run the systems metadata REST API to get the federated systems and make sure that the
deployed workflow is federated. For example, the URL might look
like:https://pfsEndpointBaseUrl/rest/bpm/federated/v1/systems
    3. Indexing case instances If you plan to enable
case federation then, create your index by using full indexer rest api. For more
information see, Indexing case instances