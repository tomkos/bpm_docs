# Deprecated and removed features of IBM Business Automation Workflow
24.0.0.0

The deprecations and removals that are made in IBM Business Automation Workflow
24.0.0.0 are summarized in the
following sections.

## Deprecated features

If a feature is listed as deprecated, or certain system requirements are indicated as deprecated
on the Software Product Compatibility Reports website, IBM might
remove this capability or support in a subsequent release of the product to focus on follow-on
technologies or the strategic feature that is listed under Action. Typically, a feature is not
deprecated unless an equivalent alternative is provided or available. A feature is not removed for
at least two releases after the deprecation of the feature is declared. In rare cases, it might be
necessary to remove features sooner; such cases are indicated in the descriptions of these removed
features.

The following features from previous releases are deprecated in IBM Business Automation
Workflow versions 24.0.0.0.

| Deprecated features                                                      | Description                                                                                                                                                                                                                                                                                  | Action                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CM8 integration support for Business Automation Workflow case management | CM8 integration support as part of the Case Management feature in Business Automation Workflow is deprecated in the current and previous releases.                                                                                                                                           | Customers should look at other integration capabilities in Extending your case management system                                                                                                                                                                      |
| Process Federation Server BPD indexing                                   | A new indexing implementation has been provided as part of Business Automation Workflow which can now index directly in the Federated Data Repository (Elasticsearch/Opensearch). Using this new implementation provides better performance than the Process Federation Server BPD indexing. | Customers can upgrade their Business Automation Workflow federated system to 24.0.0.0 as usual and then disable the indexer in Process Federation Server to replace it with the new federated data repository BPD indexing as documented in Enabling the BPD indexing |

## Removed features

The following features from previous releases are removed in IBM Business Automation Workflow
24.0.0.0.

| Removed features                          | Description                                                                         | Action                                                                                                                                                                                                                                                 |
|-------------------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Download link to desktop Process Designer | The download link for desktop Process Designer is removed from IBM Workflow Center. | Customers can log in to IBM Process Center and download the zip file containing the installer for the desktop Process Designer. For more information on how to download and install the desktop Process Designer, see Installing IBM Process Designer. |