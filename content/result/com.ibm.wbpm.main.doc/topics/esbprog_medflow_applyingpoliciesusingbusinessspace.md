<!-- image -->

# Applying policies using Business Space

## Module mediation policy administration

In the Lookup from different tables in database scenario, described in
Mediation policy usage scenarios, policies must be attached to the module containing
the Policy Resolution mediation primitive. This section describes how you can complete that task
using Business Space widgets.

### Before you begin

1. Set up a WSRR definition in the IBM® Business Automation Workflow
administrative console.
2. From IBM Integration
Designer export a mediation module
containing a Policy Resolution mediation primitive and primitives with promoted properties as a
.ear  file.
3. Deploy the .ear file to IBM Business Automation Workflow.
4. Load the .ear file into WSRR as an SCA module.

### Procedure

After you complete these steps policies can be attached to the module:

1. Log in to Business Space by navigating to
http://WESBHOST:WESBPORT/BusinessSpace.
2. Go to the Solution Administration space.

Figure 1. Selecting the Solution Administration space
3. Select the Module Administration tab.

Figure 2. The Module Administration tab

The Module Browser shows all SCA modules currently deployed to
IBM Business Automation Workflow.
4. Expand the module to which you want to apply policies. In this example, it is the
VacationFlow module.
5. Select Module Policies.

Figure 3. Finding the policies associated with your module.
6. Select the required WSRR instance, if necessary.
7. Specify the name of the new policy attachment and click Create.
8. In the Group Name list, select the property group associated with the
promoted property that you are setting.
9. Create a new policy by specifying a name and click Next.

Figure 4. Creating a new policy name.
10. In the Assertions panel, shown in Figure 5, set the value
that this policy will apply to the selected Property Name.
11. On the same panel, click Add Assertion.
12. In the Gate Conditions section of the panel, set the name of the gate
condition and enter the condition string in the Value field
13. Click Add Gate Condition.
14. Click  Save.

Figure 5. Adding assertions and gate conditions to your policy.

The new Policy Attachment is now listed in the table on the Module
Administration page.Figure 6. The Policy Attachment result page.

## Target Service mediation policy administration

In the Log a message depending on the target service scenario, described in
Mediation policy usage scenarios, policies must be attached to a target service. This
section describes how you can complete that task using Business Space widgets.

### Before you begin

1. Set up a WSRR definition in the IBM Business Automation Workflow
administrative console.
2. From IBM Integration
Designer export a mediation module
containing a Policy Resolution mediation primitive and primitives with promoted properties as a
.ear  file.
3. Deploy the .ear file to IBM Business Automation Workflow.
4. Load the .ear file into WSRR as an SCA module.

### Procedure

After you complete these steps policies can be attached to the module:

1. Log in to Business Space by navigating to
http://WESBHOST:WESBPORT/BusinessSpace.
2. Go to the Service Administration space.

Figure 7. Selecting the Service Administration space
3. Select the Service Administration tab. 
The Service Browser page shows all of the services loaded into the
specified WSRR instance.
4. Ensure that the correct WSRR instance is selected in the WSRR definition
used field.

Figure 8. The Service Administration tab
5. Expand the target service to which you want to apply policies
6. In the Mediation Policies section of the target service select the
Service, Endpoint or Operation to which to apply the policy.
7. Specify the name of the new policy attachment and click Create.

Figure 9. Finding the policies associated with your module and creating a policy attachment.
8. In the Group Name list select the property group associated with the
promoted property that you want to set.
9. Add a new policy name and click Next . 

Figure 10. Creating a new policy name
10. In the Assertions section select the property name and provide a
value.
.
11. Click Add Assertion.
12. If required, create a gate condition, as described in the Module mediation policy administration section.
13. Click  Save.

Figure 11. Adding assertions and gate conditions to your policy.
14. The new Policy Attachment is listed in a table on the Service
Administration page.

Figure 12. The Policy Attachment result page.