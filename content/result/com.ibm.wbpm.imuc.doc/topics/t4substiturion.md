<!-- image -->

# Configuring people substitution

## Before you begin

## About this task

## Procedure

1 Add the attributes, isAbsent , substitutes , substitutionStartDate ,and substitutionEndDate to the VMM definitionfor PersonAccount :
    1 Locate the wimxmlextension.xml file:
        - profile\_root/config/cells/cell\_name/wim/model/wimxmlextension.xml
        - profile\_root\config\cells\cell\_name\wim\model\wimxmlextension.xml
2. Make a backup copy of the wimxmlextension.xml file.
3. Edit the original copy of the wimxmlextension.xml file,
and make sure that it contains the following definitions, which add
the two attributes that are needed for user substitution to the PersonAccount entity
type: <wim:propertySchema nsURI="http://www.ibm.com/websphere/wim" 
     dataType="STRING" multiValued="false" propertyName="isAbsent">
   <wim:applicableEntityTypeNames>PersonAccount
   </wim:applicableEntityTypeNames>
</wim:propertySchema>

<wim:propertySchema nsURI="http://www.ibm.com/websphere/wim"
     dataType="STRING" multiValued="true" propertyName="substitutes">
   <wim:applicableEntityTypeNames>PersonAccount
   </wim:applicableEntityTypeNames>
</wim:propertySchema>
<wim:propertySchema nsURI="http://www.ibm.com/websphere/wim"
     dataType="STRING" multiValued="false" propertyName="substitutionStartDate">
   <wim:applicableEntityTypeNames>PersonAccount
   </wim:applicableEntityTypeNames>
</wim:propertySchema>

<wim:propertySchema nsURI="http://www.ibm.com/websphere/wim"
     dataType="STRING" multiValued="false" propertyName="substitutionEndDate">
   <wim:applicableEntityTypeNames>PersonAccount
   </wim:applicableEntityTypeNames>
</wim:propertySchema>If you are using a file registry, fileRegistry.xml,
skip to step 4.
2 Set up the property extension repository. Formore information about setting up a property extension repository,see Configuring a property extension repository in afederated repository configuration .

1. Make sure that a database is available to store the
property extensions.
2. Make sure that the JDBC driver class
is available on the server class path. Click Environment > WebSphere variables to
check. If necessary, add the DataServer JDBC driver to the class path.
For DB2®, add db2jcc4.jar , db2jcc\_license\_cu.jar,
and db2jcc\_license\_cisuz.jar to the server's
class path, and click Apply > Save
3. Configure a DB2 Universal JDBC driver provider
and type-4 data source for VMM using the administrative console. 
Set the webSphereDefaultIsolationLevel custom
property for the data source to the value 2. For
more information about changing the default isolation level, see Changing the default isolation level for non-CMP
applications and describing how to do so using a new custom property
webSphereDefaultIsolationLevel.
4. Restart the server.
5 Make a backup copy of the wimlaproperties.xml file.
    - install\_root/etc/wim/setup/wimlaproperties.xml
    - install\_root\etc\wim\setup
6. Edit the original copy of the wimlaproperties.xml file,
and add the following definitions: <wimprop:property wimPropertyName="isAbsent" dataType="String"
     valueLength="128" multiValued="false">
    <wimprop:applicableEntityName>
  <wimprop:entityName>PersonAccount</wimprop:entityName>
    </wimprop:applicableEntityName>
</wimprop:property>

<wimprop:property wimPropertyName="substitutes" dataType="String"
     valueLength="128" multiValued="true">
    <wimprop:applicableEntityName>
  <wimprop:entityName>PersonAccount</wimprop:entityName>
    </wimprop:applicableEntityName>
</wimprop:property>

<wimprop:property wimPropertyName="substitutionStartDate" dataType="String"
     valueLength="128" multiValued="false">
    <wimprop:applicableEntityName>
  <wimprop:entityName>PersonAccount</wimprop:entityName>
    </wimprop:applicableEntityName>
</wimprop:property>

<wimprop:property wimPropertyName="substitutionEndDate" dataType="String"
     valueLength="128" multiValued="false">
    <wimprop:applicableEntityName>
  <wimprop:entityName>PersonAccount</wimprop:entityName>
    </wimprop:applicableEntityName>
</wimprop:property>
7. Make sure that the application server (or in a network
deployment environment, the deployment manager) is running. Be aware
not to use the -conntype NONE option for the wsadmin utility.
8. Use the VMM administrative task setupIdMgrPropertyExtensionRepositoryTables to
create the substitution properties in the Property Extension Repository
database. For more details, see Setting up an entry mapping
repository, a property extension repository, or a custom registry
database repository using wsadmin commands.
For example, using a DB2 database
on a Windows platform:$AdminTask setupIdMgrPropertyExtensionRepositoryTables { 
-reportSqlError true 
-schemaLocation install\_root\etc\wim\setup 
-laPropXML  install\_root\etc\wim\setup\wimlaproperties.xml 
-databaseType db2 
-dbURL jdbc:DB2://host:port/name 
-dbDriver com.ibm.db2.jcc.DB2Driver 
-dbAdminId userID 
-dbAdminPassword password }For example,
using a DB2 database on a Linux or UNIX platform:$AdminTask setupIdMgrPropertyExtensionRepositoryTables { 
-reportSqlError true 
-schemaLocation install\_root/etc/wim/setup 
-laPropXML  install\_root/etc/wim/setup/wimlaproperties.xml 
-databaseType db2 
-dbURL jdbc:DB2://host:port/name 
-dbDriver com.ibm.db2.jcc.DB2Driver 
-dbAdminId userID 
-dbAdminPassword password }Where host is
the host name of the database server, port is the
service port for the DB2 instance, and name is
the name of the database, and userID and password provide
database administrator rights.
9 If you are using a Lightweight Directory Access Protocol(LDAP) user repository, locate the wimconfig.xml file. Edit the file and add the following entries to exclude the substitutionattributes from the LDAP repository:<config:repositories xsi:type="config:LdapRepositoryType" adapterClassName="com.ibm.ws.wim.adapter.ldap.LdapAdapter" id="ldaprepo1" ...> ... <config:attributeConfiguration> <config:propertiesNotSupported name="isAbsent"/> <config:propertiesNotSupported name="substitutes"/> <config:propertiesNotSupported name="substitutionEndDate"/> <config:propertiesNotSupported name="substitutionStartDate"/> </config:attributeConfiguration>

- profile\_root/config/cells/cellName/wim/config/wimconfig.xml
- profile\_root\config\cells\cellName\wim\config\wimconfig.xml

```
<config:repositories xsi:type="config:LdapRepositoryType"
      adapterClassName="com.ibm.ws.wim.adapter.ldap.LdapAdapter"
      id="ldaprepo1" ...>
      ...
      <config:attributeConfiguration>
         <config:propertiesNotSupported name="isAbsent"/>
         <config:propertiesNotSupported name="substitutes"/>
         <config:propertiesNotSupported name="substitutionEndDate"/> 
         <config:propertiesNotSupported name="substitutionStartDate"/>
      </config:attributeConfiguration>
```

10 Activate the extension propertyrepository:

1. Using the setIdMgrPropertyExtensionRepository command.
For more details, see Setting up an entry mapping
repository, a property extension repository, or a custom registry
database repository using wsadmin commands.
For example, using a DB2 database named VMMDB,
a data source named VMMDS: $AdminTask setIdMgrPropertyExtensionRepository { 
-dataSourceName jdbc/VMMDS
-databaseType db2 
-dbURL jdbc:DB2://host:port/VMMDB 
-dbAdminId userID
 -dbAdminPassword password
 -JDBCDriverClass com.ibm.db2.jcc.DB2Driver 
-entityRetrievalLimit 10 }
2. Verify that the wimconfig.xml file contains
an entry similar to the following example:<config:propertyExtensionRepository
   adapterClassName="com.ibm.ws.wim.lookaside.LookasideAdapter"
   id="LA" 
   databaseType="db2" 
   dataSourceName="jdbc/VMMDS" 
   dbAdminId="userID"
   dbAdminPassword="{xor}PasswordXOR" 
   dbURL="jdbc:DB2://host:port/VMMDB" 
   entityRetrievalLimit="10"
   JDBCDriverClass="com.ibm.db2.jcc.DB2Driver"/>>
3 If you use an LDAP schema to hold the substitutioninformation: It may or may not already have definitionsfor isAbsent , substitutes , substitutionStartDate ,and substitutionEndDate (possibly with differentnames). Whether you have existing definitions, or you will createnew ones, make sure the following items are set:

1. The LDAP directory must allow write operations.
2. The attribute for absence information (isAbsent)
must be of type Boolean or a String.
3. The attribute that defines who the person can substitute
for (substitutes) must be of type String,
multi-valued, and permit a length up to 128 characters.
4. If your existing or chosen attribute names are not isAbsent, substitutes, substitutionStartDate,
and substitutionEndDate, you must define
your attribute names in the administrative console by clicking Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer, and click Human Task Manager,
on the Configuration tab select Custom
properties then set the names for the custom properties Substitution.SubstitutesAttribute, Substitution.AbsenceAttribute, Substitution.StartDateAttribute,
and Substitution.EndDateAttribute.
4. Restart the server.
5 Enable substitution in the Human Task Manager:

1. Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer, and click Human Task Manager,
and click Human Task Manager, then either Runtime or Configuration.
2. To enable substitution, select Enable substitution.
3. If non-administrators are allowed to perform substitution
for other users, clear the Restrict substitute management
to administrators option. Note: This settings
does not affect the ability of users to change substitution for themselves.
4. Click Apply.
5. If you selected Configuration in
step 5.a,
restart the server to activate the substitution settings.
6. If you have problems with any of these steps,
refer to Troubleshooting people assignment.

## Results

<!-- image -->

## Related information

- Selecting a registry or repository
- Setting up an entry mapping repository, a property extension repository, or a custom registry database repository using wsadmin commands
- Configuring a property extension repository in a federated repository configuration