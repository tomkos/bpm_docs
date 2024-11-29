# Content object support

By default, content object support is enabled. If the Content Platform Engine version is earlier than
5.5.3, content object support is automatically disabled. However, if the Content Platform Engine version is 5.5.3 or later,
such as used in IBM Business Automation
Workflow
19.0.0.2 and later, content object support is automatically enabled. If the Content Platform Engine version is 5.5.3 or later,
you can manually enable content object support by using the BPMConfig command and
the -update and -enableContentObjectSupport parameters, as described in the topic BPMConfig command-line utility. You can also use
the same command and parameter to disable content object support regardless of the Content Platform Engine version.

If you are using Content Platform Engine as a container for
integration with Business Automation Workflow and the Content Platform Engine version is 5.5.3, you must run the
BPMConfig command and the -update and
-enableContentObjectSupport parameters to disable content object support.