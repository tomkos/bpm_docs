<!-- image -->

# Configuring the LDAP people directory provider

## Before you begin

## About this task

The LDAP people directory provider configuration is initialized
with a URL that points to a local LDAP server. You must change the
URL later to point to the actual LDAP server, which is normally remote
to the application server. The LDAP people directory provider is configured
for an LDAP server that allows anonymous access.

## Procedure

1 Make a copy of the standard transformationfile for LDAP, and give it another name. For example, myLDAPTransformation.xsl . Copy it from the followinglocation:
    - install\_root/ProcessChoreographer/Staff/LDAPTransformation.xsl.
    - install\_root\ProcessChoreographer\Staff\LDAPTransformation.xsl.
2. Adapt the copy of the transformation file
to suit the schema for your organization, as described in Adapting the LDAP transformation file.  CAUTION: Do not modify the original version of the transformation
file because it can be overwritten without warning when you apply
a service pack or fix pack.
3. If Business Process Choreographer is configured on a cluster,
place the copy of the transformation file in the ProcessChoreographer/Staff directory
to make it available on each Workflow Server installation
that hosts members of the cluster.
4. In the administrative console, click Resources  > People directory provider.
5 Create an LDAP configuration on the application cluster.

1. Select the application cluster for
your deployment environment.
2. Click LDAP People Directory Provider.
3. Under Additional Properties,
click People directory configuration.
4. Click New > Browse, and select the copy of the XSL transformation file
that you adapted in step 2. If the node agent is running, you can browse the file
system of remote nodes to select the file.
5. Click Next to copy the file to
the ProcessChoreographer\Staff directory on the selected
node.
6. Enter an administrative name for the new people directory
configuration, and optionally, a description
7. Enter a unique Java™ Naming
and Directory Interface (JNDI) name for human tasks to use to reference
this provider.  For example, bpe/staff/ldapserver1.
8. Click Apply, then click Custom
Properties.
9 For each of the required properties and for any optionalproperties that you planned in Planning for the people directory provider , choose whicheveroption applies and complete the following steps:
    - To change an existing property, click the name of the property,
enter a value, and click OK.
    - To create an additional property, edit one pair of additionalParameterName<number> and additionalParameterValue<number> customproperties as required, for example:
        - Set the value of additionalParameterName1 to java.ldap.referral.
        - Set the value of additionalParameterValue1 to follow.
10. To apply the changes, click Save.
6. To activate the provider configuration, stop and start
the cluster where you configured the provider.

## Results

- Adapting the LDAP transformation file

Describes how to adapt the LDAP transformation XSL file to suit your organization's LDAP schema.