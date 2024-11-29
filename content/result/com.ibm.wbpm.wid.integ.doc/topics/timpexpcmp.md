<!-- image -->

# Creating an import from an export using a JMS binding

## Before you begin

## About this task

## Procedure

1. Add a business object to the JMS Export module called CredentialsBO.
Right-click the module and from the menu select New >
Business Object. Add CredentialsBO to
the Name field. Click Finish. The business
object is created and opens in the business object editor.
2. Add the following fields.  
Table 1. Business
object fields

Name
Data Type
Property Description

userid
string
Required: yes, Minimum length: 8, Maximum length:
8

password
string
Required: yes, Minimum length: 4, Maximum length:
4
3. Create an interface for the component. Select the module
and from the menu, select New > Interface.
In the Name field, add Account. Click Finish.
The Account interface opens in the interface editor. Add the following
fields to it. 
Table 2. Interface fields

Operation
Input
Input Type
Output
Output Type
Fault
Fault Type

loginAccount
credentials
CredentialsBO
response
string
credentialsError
string

selectAccount
accountName
string
 
 
 
 

updateAccount 
performCredit 
boolean
balance
int
 
 

amount
int
4. Create a Java™ component
in the assembly editor. Right-click the module and from the menu select Open.
The assembly editor opens. From the palette, select a Java component and drag it onto the canvas.
From the icons, select Add Interface and add
the Account interface.
5. Add the Java implementation
to the component. Rename your component's display name and name AccountInfo.
Name determines what the first part of your class name will be. Impl
is added to it. So in this case your generated class name will be
AccountInfoImpl. Right-click the component and from the menu select Generate
implementation.
6. The Generate Implementation window
box opens. Click New Package and specify the
package name as accountrecord. Then select
it and click OK. A shell AccountInfoImpl class
is created and opens in a Java editor,
which means the code will be checked each time you save it. The operations
you created earlier in the interface editor have become methods in Java. Add the following field at
the class level: private String account;
7. Add the following code for the loginAccount method.
public String loginAccount(DataObject credentials) {
		
		String userid = credentials.getString("userid");
		String password = credentials.getString("password");
		
		return "Result from loginAccount(DataObject credentials) is userid: " + userid + " password: " + password;
	}
8. Add the following code for the selectAccount method.
public void selectAccount(String accountName) {
		account = accountName;
	}
9. Add the following code for the updateAccount method.
public Integer updateAccount(Boolean performCredit, Integer amount) {
		int balance = 0;
		if ("chequing".equals(account)) {
			int c\_balance = 1000;
			if (performCredit.booleanValue())
				balance = c\_balance + amount.intValue();
			else
				balance = c\_balance - amount.intValue();
		} else if ("savings".equals(account)) {
			int c\_balance = 5000;
			if (performCredit.booleanValue())
				balance = c\_balance + amount.intValue();
			else
				balance = c\_balance - amount.intValue();
		}
		
		return new Integer(balance);
	}
10. Save your implementation. From the menu, select File >
Save. Return to the assembly editor. Export the Java component with a JMS binding.
Select the component and from the menu, select Export >
JMS Binding. The JMS Export binding selection window
box opens. Change the Select how data is serialized between
Business Object and JMS Message field to Object.
Click OK.
11. The AccountInfoExport component is created. Save your work.
12. In the Business Integration navigation, copy CredentialsBO
and Account to the JMSImport module. Open the assembly editor of the
JMSImport module. Right-click module name and from the menu select Open.
Drag the AccountInfoExport component from the JMSExport module navigation
to the assembly editor canvas of the JMSImport module. A Manage
Project Dependencies message opens. Click OK.
An import component is created with a JMS binding.
13. Select the component and in the properties view select
the Binding tab. The JMS binding details open.
14. The Java code in
the example is provided as part of the steps as you go through it.
To test, create a stand-alone reference in the JMSExport module and
connect it to the Import1 import component. Stand-alone references
are used to represent components outside the Service Component Architecture
such as JSPs. Save your changes.
15. Create a Dynamic Web Project called TestImportClient, but
do not associate an EAR project with it. (Clear Add module to an EAR
project.)
16. In the JMSImport module, open the dependency editor. Right-click
the module and from the menu select Open Dependency Editor.
In the J2EE section, click Add and add
the TestImportClient project. Save your changes and close the editor.
17. Create a JSP in the TestImportClient project using the
following code: <P>Loggin in:
<BR>
<%
	com.ibm.websphere.sca.ServiceManager serviceManager = new com.ibm.websphere.sca.ServiceManager();
	com.ibm.websphere.sca.Service service = (com.ibm.websphere.sca.Service) serviceManager.locateService("AccountPartner");
	com.ibm.websphere.sca.scdl.Reference reference = service.getReference();
	com.ibm.websphere.sca.sdo.DataFactory dataFactory = com.ibm.websphere.sca.sdo.DataFactory.INSTANCE;
	com.ibm.websphere.bo.BOFactory boFactory = (com.ibm.websphere.bo.BOFactory)serviceManager.locateService("com/ibm/websphere/bo/BOFactory");

	String login = null;
	try {
		commonj.sdo.DataObject credentialsBO = boFactory.create("http://JMSInbound", "CredentialsBO");
		credentialsBO.setString("userid", "abcdXYZZ");
		 credentialsBO.setString("password", "1234");
		
		login = (String) service.invoke("loginAccount", credentialsBO);
	} catch (com.ibm.websphere.sca.ServiceBusinessException e) {
		Object error = e.getData();
	}

 %>
The login result is <%=login%> <BR>

<BR>
Changing account to chequing <BR>
<%
		 com.ibm.websphere.sca.scdl.OperationType selectAccountOp = reference.getOperationType("selectAccount");
		 service.invokeAsync(selectAccountOp, "chequing");
%>

Performing credit of 100 <BR>

<%
	com.ibm.websphere.sca.scdl.OperationType updateAccountOp = null;
	commonj.sdo.Type updateAccountOpInput = null;
	commonj.sdo.DataObject transaction = null;
	Integer balance = null;
	try {
		updateAccountOp = reference.getOperationType("updateAccount");
		updateAccountOpInput = updateAccountOp.getInputType();
		transaction = dataFactory.create(updateAccountOpInput);
		transaction.set(0, Boolean.TRUE);
		transaction.set(1, new Integer(100));
		
		balance = (Integer) service.invoke("updateAccount", transaction);
		%>
		The new balance is: <%= balance%> <BR>
		<%
	} catch (com.ibm.websphere.sca.ServiceBusinessException e) {
		commonj.sdo.DataObject error = (commonj.sdo.DataObject)e.getData();
		%>
		Error: <%= error.get("account")%> amount: <%= error.get("balance")%> <BR>
		<%
	}	
%>

<BR>

<BR>
Changing account to savings <BR>
<%
		 service.invokeAsync(selectAccountOp, "savings");
%>

Performing debit of 500 <BR>
<%
try {
		transaction.set(0, Boolean.FALSE);
		transaction.set(1, new Integer(500));
		
		balance = (Integer) service.invoke("updateAccount", transaction);
		%>
		The new balance is: <%= balance%> <BR>
		<%
	} catch (com.ibm.websphere.sca.ServiceBusinessException e) {
		commonj.sdo.DataObject error = (commonj.sdo.DataObject)e.getData();
		%>
		Error: <%= error.get("account")%> amount: <%= error.get("balance")%> <BR>
		<%
	}	
%>
<BR>

</P>
18. Add all your projects to the server. Right-click the server
in the servers view and from the menu select Add and remove
projects. Add your projects.
19. With the server running, select the JSP and run it. In IBM® Integration
Designer web
browser, enter the following URL: http://localhost:9080/TestImportClient/<JSPName>.
It will update the balance of an account.

## What to do next

## Related tasks

- Creating a JMS import to communicate with a JMS client
- Creating a JMS export to communicate with a JMS client
- Creating a JMS client to receive messages from a JMS import
- Creating a user-defined JMS data binding