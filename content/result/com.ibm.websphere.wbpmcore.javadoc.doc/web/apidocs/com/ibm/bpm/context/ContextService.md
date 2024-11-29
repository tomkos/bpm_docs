- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Interface ContextService

- public interface ContextService The ContextService interface represents the programming model for the context service in IBM Business Automation Workflow. The IBM Business Automation Workflow context service provides the ability to access and modify protocol headers and execution context.It also propagates the execution context to downstream components. The following code is used to locate context service: ContextService contextService = (ContextService) ServiceManager.INSTANCE .locateService("com/ibm/bpm/context/ContextService"); The following features are supported: The above two features can be accessed by ContextObject too. The data which is set into the execution context by context service can be propagated across modules. Assuming there are two modules, Module A and Module B. Component A is in module A, component B is in module B, and, component A calls component B. In component A, the context data can be set like this: //Get the HeaderInfoType from contextService HeaderInfoType headers = contextService.getHeaderInfo(); if(headers == null){ //Create new HeaderInfoType if its null and you want to propagate additional properties using headers headers = ContextObjectFactory.eINSTANCE.createHeaderInfoType(); } //Propagating custom properties through headers //Create a new property PropertyType prop = ServiceMessageObjectFactory.eINSTANCE.createPropertyType(); prop.setName("Name"); //Set the name of the property prop.setValue("value"); //Set the value of the property prop.setPropertyType("java.lang.String"); //Set the type the property List properties = headers.getProperties(); properties.add(prop); //Add the property to the list of header properties // Set header info back to the current execution context. contextService.setHeaderInfo(headers); //Propagating custom data through UserDefinedContext // Get user defined context in current execution context UserDefinedContextType userDefinedContext = contextService.getUserDefinedContext(); if(userDefinedContext == null){ // create a new context if context is null userDefinedContext = ContextObjectFactory.eINSTANCE.createUserDefinedContextType(); } // Modifying the userDefinedContext //Create a new property with the data that needs to be propagated ComplexPropertyType customerData = ServiceMessageObjectFactory.eINSTANCE.createComplexPropertyType(); customerData.setName("customer"); //Set the name of the property //The value of the data must be of type DataObject. //Use BusinessObject Factory service to create a DataObject BOFactory boFactory = (BOFactory) ServiceManager.INSTANCE.locateService("com/ibm/websphere/bo/BOFactory"); //Pass the targetNameSpace of the business object and the ComplextTypeName DataObject dataObject = boFactory.create("http://www.ibm.com/xmlns/customer", "Customer"); customerData.setValue(dataObject);//Set the value on the property //Get the UserContextType from UserDefinedContextType UserContextType userContext = userDefinedContext.getUserContext(); if(userContext == null) //If the userContext is null, create a new instance and set in on the userDefinedContext { userContext = ServiceMessageObjectFactory.eINSTANCE.createUserContextType(); userDefinedContext.setUserContext(userContext); } //Add the property to the userContext userContext.getEntries().add(customerData); // Set user defined context back to the current execution context. contextService.setUserDefinedContext(userDefinedContext); The context data will be propagated from component A to component B. In component B, the context data can be accessed like below: //Getting headers data HeaderInfoType headers = contextService.getHeaderInfo(); //Retrieving the property if(headers != null) { List headerProperties = headers.getProperties(); if(headerProperties !=null) { for(Iterator i = headerProperties.iterator(); i.hasNext();){ PropertyType p = i.next(); if(p.getName().equals("Name")){ //Check for the name of the property or directly get the property based on the index in which it was stored p.getValue(); return; } } } } //Reading protocol specific headers //Reading http protocol headers HTTPHeaderType httpHeader = headers.getHTTPHeader(); HTTPControl control = httpHeader.getControl(); int contentLength = control.getContentLength(); String method = control.getMethod(); //Getting data from user defined context object UserDefinedContextType userDefinedContext = contextService.getUserDefinedContext(); if(userDefinedContext != null) { List properties = userDefinedContext.getUserContext().getEntries(); for (Iterator userContextProperties = properties.iterator(); userContextProperties.hasNext();) { ComplexPropertyType p = userContextProperties.next(); if(p.getName().equals("customer")){ //Check for the name of the property or directly get the property based on the index in which it was stored p.getValue(); return; } } } Context access and propagation can make the business logic more clean, but setting large data in execution context or headers would impact the performance. Because once the data is set to current execution context, it will be propagated to downstream components. So, it is recommended to not put large data into current execution context. The ContextService API should not be used within a mediation flow. The SMO API should be used instead. com.ibm.websphere.sibx.smobo.ContextType context = smo.getContext(); If the updated context data is not set back by setHeaderInfo, setUserDefinedContext, or setContextObject, the context service will NOT propagate the updated data to the downstream. Refer to Service Message Object documentation for more details on HeaderInfoType and UserDefinedContext APIs.

```
public interface ContextService
```

The following code is used to locate context service:
 

        ContextService contextService = (ContextService) ServiceManager.INSTANCE
                .locateService("com/ibm/bpm/context/ContextService");
        

 The following features are supported:
 

 HeaderInfoType 
  contains protocol headers.
   UserDefinedContextType 
  contains user defined context data.
  

  The above two features can be accessed by
  ContextObject too.
  

  The data which is set into the execution context by context service can be propagated across modules.
  Assuming there are two modules, Module A and Module B. Component A is in module A,
  component B is in module B, and, component A calls component B.
  In component A, the context data can be set like this:
  

   //Get the HeaderInfoType from contextService
         HeaderInfoType headers = contextService.getHeaderInfo();
         if(headers == null){ //Create new HeaderInfoType if its null and you want to propagate additional properties using headers
                headers = ContextObjectFactory.eINSTANCE.createHeaderInfoType();
         }

   //Propagating custom properties through headers
   //Create a new property
                PropertyType prop = ServiceMessageObjectFactory.eINSTANCE.createPropertyType();
                prop.setName("Name"); //Set the name of the property
                prop.setValue("value"); //Set the value of the property
                prop.setPropertyType("java.lang.String"); //Set the type the property

                List properties = headers.getProperties();
            properties.add(prop); //Add the property to the list of header properties

   // Set header info back to the current execution context.
   contextService.setHeaderInfo(headers);

   //Propagating custom data through UserDefinedContext
   // Get user defined context in current execution context
   UserDefinedContextType userDefinedContext = contextService.getUserDefinedContext();
   if(userDefinedContext == null){ // create a new context if context is null
        userDefinedContext = ContextObjectFactory.eINSTANCE.createUserDefinedContextType();
   }
   // Modifying the userDefinedContext

   //Create a new property with the data that needs to be propagated
         ComplexPropertyType customerData = ServiceMessageObjectFactory.eINSTANCE.createComplexPropertyType();
         customerData.setName("customer"); //Set the name of the property

         //The value of the data must be of type DataObject.
         //Use BusinessObject Factory service to create a DataObject
         BOFactory boFactory = (BOFactory) ServiceManager.INSTANCE.locateService("com/ibm/websphere/bo/BOFactory");
         //Pass the targetNameSpace of the business object and the ComplextTypeName
         DataObject dataObject = boFactory.create("http://www.ibm.com/xmlns/customer", "Customer");

         customerData.setValue(dataObject);//Set the value on the property

         //Get the UserContextType from UserDefinedContextType
         UserContextType userContext = userDefinedContext.getUserContext();
         if(userContext == null) //If the userContext is null, create a new instance and set in on the userDefinedContext
         {
                userContext = ServiceMessageObjectFactory.eINSTANCE.createUserContextType();
                userDefinedContext.setUserContext(userContext);
         }
         //Add the property to the userContext
         userContext.getEntries().add(customerData);

   // Set user defined context back to the current execution context.
   contextService.setUserDefinedContext(userDefinedContext);

   

  The context data will be propagated from component A to component B.
  
  In component B, the context data can be accessed like below:
  

   //Getting headers data
   HeaderInfoType headers = contextService.getHeaderInfo();
   //Retrieving the property
   if(headers != null)
         {
                List headerProperties = headers.getProperties();
                if(headerProperties !=null)
                {
                        for(Iterator i = headerProperties.iterator(); i.hasNext();){
                                PropertyType p = i.next();
                                if(p.getName().equals("Name")){ //Check for the name of the property or directly get the property based on the index in which it was stored
                                        p.getValue();
                                        return;
                                }
                        }
                }
         }

         //Reading protocol specific headers
         //Reading http protocol headers
         HTTPHeaderType httpHeader = headers.getHTTPHeader();
         HTTPControl control = httpHeader.getControl();
         int contentLength = control.getContentLength();
   String method = control.getMethod();

   //Getting data from user defined context object
   UserDefinedContextType userDefinedContext = contextService.getUserDefinedContext();
   if(userDefinedContext != null)
   {
        List properties = userDefinedContext.getUserContext().getEntries();
            for (Iterator userContextProperties = properties.iterator(); userContextProperties.hasNext();)
                {
                        ComplexPropertyType p = userContextProperties.next();
                        if(p.getName().equals("customer")){ //Check for the name of the property or directly get the property based on the index in which it was stored
                                p.getValue();
                                return;
                        }
                }
         }

   

  Context access and propagation can make the business logic more clean, but
  setting large data in execution context or headers would impact the performance.
  Because once the data is set to current execution context, it will be propagated to
  downstream components. So, it is recommended to not put large data into current
  execution context.
  

  The ContextService API should not be used within a mediation flow.  The SMO API should be used instead.
  

      com.ibm.websphere.sibx.smobo.ContextType context = smo.getContext();
  

  If the updated context data is not set back by setHeaderInfo, setUserDefinedContext, or
  setContextObject, the context service will NOT propagate the updated data to the downstream.

  Refer to Service Message Object documentation for more details on HeaderInfoType and UserDefinedContext APIs.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
Copyright
    - Method Summary

Methods 

Modifier and Type
Method and Description

ContextObject
getContextObject()
Get context object from current execution context.

HeaderInfoType
getHeaderInfo()
Get the protocol headers in the current execution context
 

 The protocol headers type is represented by
 HeaderInfoType.

UserDefinedContextType
getUserDefinedContext()
Get the user defined context data from the current execution context.

void
setContextObject(ContextObject contextObject)
Set context object to current execution context.

void
setHeaderInfo(HeaderInfoType headerInfo)
Set the protocol headers to the current execution context.

void
setUserDefinedContext(UserDefinedContextType userDefinedContext)
Set user defined context data to the current execution context.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
Copyright
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getHeaderInfo
HeaderInfoType getHeaderInfo()
Get the protocol headers in the current execution context
 

 The protocol headers type is represented by
 HeaderInfoType.
Returns:the protocol header's information in current execution contextSee Also:HeaderInfoType
    - setHeaderInfo
void setHeaderInfo(HeaderInfoType headerInfo)
Set the protocol headers to the current execution context.
 

 If the input headers value is null, the protocol headers in current execution
 context will be removed.
 

 The context service will not propagate the updated context data if it
 is not set to current execution context.
Parameters:headerInfo - the protocol header's information.See Also:HeaderInfoType
    - getUserDefinedContext
UserDefinedContextType getUserDefinedContext()
Get the user defined context data from the current execution context.
 

 The user context type is presented by
 UserDefinedContextType
Returns:the user defined context data in current execution contextSee Also:UserDefinedContextType
    - setUserDefinedContext
void setUserDefinedContext(UserDefinedContextType userDefinedContext)
Set user defined context data to the current execution context.
 

 If the input context value is null, the user defined context data in the current context
 will be removed.
 

 The context service will not propagate the context data if it
 is not set to current execution context.
Parameters:userDefinedContext - the user defined context data.See Also:UserDefinedContextType
    - getContextObject
ContextObject getContextObject()
Get context object from current execution context.
 

 ContextObject is the container of header info and user defined context.

 It provides xpath like style to access and modify context data. For
 example:
 

        ContextObject contextObject = contextService.getContextObject();
        HeaderInfoType headers = contextObject.getHeaderInfo();
        UserDefinedContextType userDefinedContext = contextObject.getUserDefinedContext();

        

Returns:context objectSee Also:ContextObject
    - setContextObject
void setContextObject(ContextObject contextObject)
Set context object to current execution context.
 

 If the modified context object is not set to current execution context,
 context service will not propagate the modified data.
 So, after the context object is modified, please set it back to current
 execution context:
 

        // get context object
        ContextObject contextObject = contextService.getContextObject();
        // Retrieve HeaderInfoType/UserDefinedCotextType objects and modify the data like specified above
        ... ...
        // Set the modified context object back to current execution context
        contextService.setContextObject(contextObject);
 

Parameters:contextObject - the context object.See Also:ContextObject