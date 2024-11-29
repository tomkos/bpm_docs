# Installing a snapshot fails after message confirms installation

You may see the following sequence of messages in Workflow Center when you are installing a snapshot. First you
see Installation is progressing which is followed by Currently
installed. After these messages comes another message Installation terminated with an
exception.

This sequence can happen when you are using IBM Business Process Manager
Advanced. During the installation of a snapshot on a
workflow server, the content of the snapshot is first imported into the workflow server and then the
advanced artifacts, such as SCA modules and libraries, are deployed to the workflow server if they
are present. If this advanced deployment of a snapshot fails, you receive message CWLLG2163E, which
indicates that the process application snapshot content is imported on the workflow server but
advanced content failed to install. You can attempt to install the advanced content of the same
snapshot again from the Process Admin Console by activating the snapshot.