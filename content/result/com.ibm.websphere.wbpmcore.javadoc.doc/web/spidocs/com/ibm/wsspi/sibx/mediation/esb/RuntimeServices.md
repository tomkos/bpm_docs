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

## Interface RuntimeServices

- public interface RuntimeServices
Provides WebSphere runtime related services to ESB mediation primitives. The
 only service provided is the access to JDBC Data sources.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

javax.sql.DataSource
getDataSource(java.lang.String jndiName)
Deprecated.  

javax.sql.DataSource
getDataSourceForProperty(java.lang.String propertyName)
Provides access to a JDBC data source.

java.lang.String
getSubflowName()
Provides access to the name of the current subflow

java.lang.String
getSubflowPrimitiveName()
Provide access to the name of the current subflow primitive

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- $sccsid
static final java.lang.String $sccsid
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getDataSource
javax.sql.DataSource getDataSource(java.lang.String jndiName)
                                   throws DataSourceException
Deprecated. 
Provides access to a JDBC data source. The ESB mediation primitive 
 specifies a fully qualified JNDI name which this method will then use to
 lookup and return the JDBC DataSource bound to that JNDI name.
 
 This method is deprecated in favour of the
Parameters:jndiName - the JNDI name of the data source
Returns:the data source
Throws:
DataSourceException - if there is a problem when obtaining the 
         data source.
    - getDataSourceForProperty
javax.sql.DataSource getDataSourceForProperty(java.lang.String propertyName)
                                              throws DataSourceException
Provides access to a JDBC data source. The ESB mediation primitive
 specifies the property name of the primitive property on which a global
 JNDI name was specified as the value. This method will then use that
 property name to perform a local JNDI lookup of the environment
 resource reference to which that global JNDI name was bound.
Parameters:propertyName - the name of the property
Returns:the data source
Throws:
DataSourceException - if there is a problem when obtaining the 
         data source
    - getSubflowName
java.lang.String getSubflowName()
Provides access to the name of the current subflow
Returns:the name of the current subflow
    - getSubflowPrimitiveName
java.lang.String getSubflowPrimitiveName()
Provide access to the name of the current subflow primitive
Returns:the name of the current subflow mediation primitive