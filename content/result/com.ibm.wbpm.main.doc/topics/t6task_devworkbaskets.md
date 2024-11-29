<!-- image -->

# Developing client applications for work baskets and business
categories

## Before you begin

## About this task

## Procedure

1. Add a reference to the interface of the session bean to
the application deployment descriptor. Add the reference to one of
the following files: For example, a reference to the local
interface might look like the following example:<ejb-local-ref>
  <ejb-ref-name>
     ejb/LocalHumanTaskManagerHome
  </ejb-ref-name>
  <ejb-ref-type>Session</ejb-ref-type>
  <local-home>
    com.ibm.task.api.LocalHumanTaskManagerHome
  </local-home>
  <local>
    com.ibm.task.api.LocalHumanTaskManagerHome
  </local>
</ejb-local-ref>
2. Use the JNDI to look up the appropriate home interface
EJB API.  The following example shows how you might access
the local home interface.// Obtain the default initial JNDI context
Context initialContext = new InitialContext();

// Lookup the local home interface of the local EJB API
Object result = initialContext.lookup
   ("java:comp/env/ejb/LocalHumanTaskManagerHome");

// Convert the lookup to the proper type
LocalHumanTaskManagerHome home = 
  (LocalHumanTaskManagerHome)
    javax.rmi.PortableRemoteObject.narrow(result,  
     LocalHumanTaskManagerHome.class);
3. Create the EJB object. Tip: To reduce
the number of methods that you need to use in your client application,
cast the EJB proxy that you retrieve from the lookup to the corresponding
service interface, 
WorkBasketManagerService interface
or BusinessCategoryManagerService interface. The
following example shows this step for a work basket:WorkBasketManagerService wbmSvc = home.create();
The following example shows this step for a business category.BusinessCategoryManagerService bcmSvc = home.create();
4. Use the EJB APIs to interact with the work baskets and
business categories.