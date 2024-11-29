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

## Interface RelationshipService

- public interface RelationshipService
The RelationshipService interface represents the client programming model for
 the Relationship Service.  The RelationshipService provides operations for Relationship and
 Role management.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

int
addParticipant(java.lang.String relationshipName,
              java.lang.String roleName,
              commonj.sdo.DataObject bo)
Adds a participant to a new relationship instance.

int
addParticipantBoolean(java.lang.String relationshipName,
                     java.lang.String roleName,
                     boolean dataSimpleType)
Adds a participant to a new relationship instance.

int
addParticipantBooleanWithID(java.lang.String relationshipName,
                           java.lang.String roleName,
                           int instanceID,
                           boolean dataSimpleType)
Adds a participant for an existing relationship instance.

int
addParticipantDouble(java.lang.String relationshipName,
                    java.lang.String roleName,
                    double dataSimpleType)
Adds a participant to a new relationship instance.

int
addParticipantDoubleWithID(java.lang.String relationshipName,
                          java.lang.String roleName,
                          int instanceID,
                          double dataSimpleType)
Adds a participant for an existing relationship instance.

int
addParticipantFloat(java.lang.String relationshipName,
                   java.lang.String roleName,
                   float dataSimpleType)
Adds a participant to a new relationship instance.

int
addParticipantFloatWithID(java.lang.String relationshipName,
                         java.lang.String roleName,
                         int instanceID,
                         float dataSimpleType)
Adds a participant for an existing relationship instance.

int
addParticipantInt(java.lang.String relationshipName,
                 java.lang.String roleName,
                 int dataSimpleType)
Adds a participant to a new relationship instance.

int
addParticipantIntWithID(java.lang.String relationshipName,
                       java.lang.String roleName,
                       int instanceID,
                       int dataSimpleType)
Adds a participant for an existing relationship instance.

int
addParticipantLong(java.lang.String relationshipName,
                  java.lang.String roleName,
                  long dataSimpleType)
Adds a participant to a new relationship instance.

int
addParticipantLongWithID(java.lang.String relationshipName,
                        java.lang.String roleName,
                        int instanceID,
                        long dataSimpleType)
Adds a participant for an existing relationship instance.

void
addParticipants(java.lang.String relationshipName,
               java.util.HashMap iid\_subMap)
Adds mulitple participants to multiple relationship instances for multiple roles.

void
addParticipants(java.lang.String relationshipName,
               java.lang.String roleName,
               java.util.HashMap iid\_value)
Adds multiple participants to multiple relationship instances for a role.

int
addParticipantString(java.lang.String relationshipName,
                    java.lang.String roleName,
                    java.lang.String dataString)
Adds a participant to a new relationship instance.

int
addParticipantStringWithID(java.lang.String relationshipName,
                          java.lang.String roleName,
                          int instanceID,
                          java.lang.String dataString)
Adds a participant for an existing relationship instance.

void
addParticipantsWithID(java.lang.String relationshipName,
                     int instanceid,
                     java.util.HashMap roleName\_value)
Adds multiple participants to a relationship instance for multiple roles.

int
addParticipantsWithoutID(java.lang.String relationshipName,
                        java.util.HashMap roleName\_value)
Adds multiple participants to a new relationship instance for multiple roles.

int
addParticipantWithID(java.lang.String relationshipName,
                    java.lang.String roleName,
                    int instanceId,
                    commonj.sdo.DataObject bo)
Adds a participant for an existing relationship instance that match this
 relationship, ASBO role and instance id.

void
correlate(java.lang.String relationshipName,
         java.lang.String inputRoleName,
         java.lang.String outputRoleName,
         commonj.sdo.DataObject inputBO,
         commonj.sdo.DataObject outputBO,
         commonj.sdo.DataObject originalInputBO,
         commonj.sdo.DataObject originalOutputBO,
         java.lang.String callingContext)
Correlates an inputBO of the given
 inputRoleName with the outputBO of the
 given outputRoleName and maintains the relationship between
 them according to the meta data contained in the inputBO
 (currently either verb or change summary information or both).

void
correlateFromList(java.lang.String relationshipName,
                 java.lang.String inputRoleName,
                 java.lang.String outputRoleName,
                 java.util.List inputBOs,
                 commonj.sdo.DataObject outputBO,
                 commonj.sdo.DataObject originalInputBO,
                 java.util.List originalOutputBOs,
                 java.lang.String callingContext)
Used to correlate a list of business objects of a simple input role
 with the children of parent/child output role.

void
correlateToList(java.lang.String relationshipName,
               java.lang.String inputRoleName,
               java.lang.String outputRoleName,
               commonj.sdo.DataObject inputBO,
               java.util.List outputBOs,
               java.util.List originalInputBOs,
               commonj.sdo.DataObject originalOutputBO,
               java.lang.String callingContext)
Used to correlate the children of a parent/child input role with
 a list of business objects of a simple output role.

int
createParticipant(java.lang.String relationshipName,
                 java.lang.String roleName,
                 commonj.sdo.DataObject bo)
Adds a participant to a new relationship instance.

int
createParticipantBoolean(java.lang.String relationshipName,
                        java.lang.String roleName,
                        boolean dataSimpleType)
Adds a participant to a new relationship instance.

int
createParticipantBooleanWithID(java.lang.String relationshipName,
                              java.lang.String roleName,
                              int instanceID,
                              boolean dataSimpleType)
Adds a participant for an existing relationship instance.

int
createParticipantDouble(java.lang.String relationshipName,
                       java.lang.String roleName,
                       double dataSimpleType)
Adds a participant to a new relationship instance.

int
createParticipantDoubleWithID(java.lang.String relationshipName,
                             java.lang.String roleName,
                             int instanceID,
                             double dataSimpleType)
Adds a participant for an existing relationship instance.

int
createParticipantFloat(java.lang.String relationshipName,
                      java.lang.String roleName,
                      float dataSimpleType)
Adds a participant to a new relationship instance.

int
createParticipantFloatWithID(java.lang.String relationshipName,
                            java.lang.String roleName,
                            int instanceID,
                            float dataSimpleType)
Adds a participant for an existing relationship instance.

int
createParticipantInt(java.lang.String relationshipName,
                    java.lang.String roleName,
                    int dataSimpleType)
Adds a participant to a new relationship instance.

int
createParticipantIntWithID(java.lang.String relationshipName,
                          java.lang.String roleName,
                          int instanceID,
                          int dataSimpleType)
Adds a participant for an existing relationship instance.

int
createParticipantLong(java.lang.String relationshipName,
                     java.lang.String roleName,
                     long dataSimpleType)
Adds a participant to a new relationship instance.

int
createParticipantLongWithID(java.lang.String relationshipName,
                           java.lang.String roleName,
                           int instanceID,
                           long dataSimpleType)
Adds a participant for an existing relationship instance.

int
createParticipantString(java.lang.String relationshipName,
                       java.lang.String roleName,
                       java.lang.String dataString)
Adds a participant to a new relationship instance.

int
createParticipantStringWithID(java.lang.String relationshipName,
                             java.lang.String roleName,
                             int instanceID,
                             java.lang.String dataString)
Adds a participant for an existing relationship instance.

int
createParticipantWithID(java.lang.String relationshipName,
                       java.lang.String roleName,
                       int instanceId,
                       commonj.sdo.DataObject bo)
Adds a participant for an existing relationship instance that has this
 instanceId.

void
deactivateParticipant(java.lang.String relationshipName,
                     java.lang.String roleName,
                     commonj.sdo.DataObject bo)
Deactivates all the participants of this relationship that match the
 specified BO.

void
deactivateParticipantBoolean(java.lang.String relationshipName,
                            java.lang.String roleName,
                            boolean dataSimpleType)
Deactivates all the participants of this relationship that match this
 data for the participant.

void
deactivateParticipantBooleanByID(java.lang.String relationshipName,
                                java.lang.String roleName,
                                int instanceID,
                                boolean dataSimpleType)
Deactivates all the participant instances of the relationship that match
 this data for the participant and have the specified relationship
 instanceID.

void
deactivateParticipantByID(java.lang.String relationshipName,
                         java.lang.String roleName,
                         int instanceId)
Deactivates all the participants of this relationship that matche the
 specified relationship instanceID.

void
deactivateParticipantByIDAndDO(java.lang.String relationshipName,
                              java.lang.String roleName,
                              int instanceId,
                              commonj.sdo.DataObject bo)
Deactivates all the partcipants that match this relationship, role, BO and
 instanceId.

void
deactivateParticipantDouble(java.lang.String relationshipName,
                           java.lang.String roleName,
                           double dataSimpleType)
Deactivates all the participants of this relationship that match this
 data for the participant.

void
deactivateParticipantDoubleByID(java.lang.String relationshipName,
                               java.lang.String roleName,
                               int instanceID,
                               double dataSimpleType)
Deactivates all the participant instances of the relationship that match
 this data for the participant and have the specified relationship
 instanceID.

void
deactivateParticipantFloat(java.lang.String relationshipName,
                          java.lang.String roleName,
                          float dataSimpleType)
Deactivates all the participants of this relationship that match this
 data for the participant.

void
deactivateParticipantFloatByID(java.lang.String relationshipName,
                              java.lang.String roleName,
                              int instanceID,
                              float dataSimpleType)
Deactivates all the participant instances of the relationship that match
 this data for the participant and have the specified relationship
 instanceID.

void
deactivateParticipantInt(java.lang.String relationshipName,
                        java.lang.String roleName,
                        int dataSimpleType)
Deactivates all the participants of this relationship that match this
 data for the participant.

void
deactivateParticipantIntByID(java.lang.String relationshipName,
                            java.lang.String roleName,
                            int instanceID,
                            int dataSimpleType)
Deactivates all the participant instances of the relationship that match
 this data for the participant and have the specified relationship
 instanceID.

void
deactivateParticipantLong(java.lang.String relationshipName,
                         java.lang.String roleName,
                         long dataSimpleType)
Deactivates all the participants of this relationship that match this
 data for the participant.

void
deactivateParticipantLongByID(java.lang.String relationshipName,
                             java.lang.String roleName,
                             int instanceID,
                             long dataSimpleType)
Deactivates all the participant instances of the relationship that match
 this data for the participant and have the specified relationship
 instanceID.

void
deactivateParticipantString(java.lang.String relationshipName,
                           java.lang.String roleName,
                           java.lang.String dataString)
Deactivates all the participants of this relationship that match this
 data for the participant.

void
deactivateParticipantStringByID(java.lang.String relationshipName,
                               java.lang.String roleName,
                               int instanceID,
                               java.lang.String dataString)
Deactivates all the participant instances of the relationship that match
 this data for the participant and have the specified relationship
 instanceID.

void
deleteAllParticipants(java.lang.String relationshipName,
                     java.lang.String roleName)
Deletes all the participants for this relationship and the ASBO role.

void
deleteParticipant(java.lang.String relationshipName,
                 java.lang.String roleName,
                 commonj.sdo.DataObject bo)
Deletes all the participants of this relationship that match the
 specified BO.

void
deleteParticipantBoolean(java.lang.String relationshipName,
                        java.lang.String roleName,
                        boolean dataSimpleType)
Deletes all the participants of this relationship that match this role
 and the specified data.

void
deleteParticipantBooleanByID(java.lang.String relationshipName,
                            java.lang.String roleName,
                            int instanceID,
                            boolean dataSimpleType)
Deletes all the participants that match this relationship name, role name,
 relationship instanceID and the data.

void
deleteParticipantByID(java.lang.String relationshipName,
                     java.lang.String roleName,
                     int instanceId)
Deletes all the participants of this relationship that matche the
 specified relationship instanceID.

void
deleteParticipantByIDAndDO(java.lang.String relationshipName,
                          java.lang.String roleName,
                          int instanceId,
                          commonj.sdo.DataObject bo)
Deletes all the partcipants that match this relationship, role, BO and
 instanceId.

void
deleteParticipantDouble(java.lang.String relationshipName,
                       java.lang.String roleName,
                       double dataSimpleType)
Deletes all the participants of this relationship that match this role
 and the specified data.

void
deleteParticipantDoubleByID(java.lang.String relationshipName,
                           java.lang.String roleName,
                           int instanceID,
                           double dataSimpleType)
Deletes all the participants that match the relationship name, role name,
 relationship instanceID and the data.

void
deleteParticipantFloat(java.lang.String relationshipName,
                      java.lang.String roleName,
                      float dataSimpleType)
Deletes all the participants of this relationship that match this role
 and the specified data.

void
deleteParticipantFloatByID(java.lang.String relationshipName,
                          java.lang.String roleName,
                          int instanceID,
                          float dataSimpleType)
Deletes all the participants that match the relationship name, role name,
 relationship instanceID and the data.

void
deleteParticipantInt(java.lang.String relationshipName,
                    java.lang.String roleName,
                    int dataSimpleType)
Deletes all the participants of this relationship that match this role
 and the specified data.

void
deleteParticipantIntByID(java.lang.String relationshipName,
                        java.lang.String roleName,
                        int instanceID,
                        int dataSimpleType)
Deletes all the participants that match the relationship name, role name,
 relationship instanceID and the data.

void
deleteParticipantLong(java.lang.String relationshipName,
                     java.lang.String roleName,
                     long dataSimpleType)
Deletes all the participants of this relationship that match this role
 and the specified data.

void
deleteParticipantLongByID(java.lang.String relationshipName,
                         java.lang.String roleName,
                         int instanceID,
                         long dataSimpleType)
Deletes all the participants that match the relationship name, role name,
 relationship instanceID and the data.

void
deleteParticipants(java.lang.String relationshipName,
                  java.util.List roleNames)
Deletes all the participants for the sepecified roles of a relationship.

void
deleteParticipantString(java.lang.String relationshipName,
                       java.lang.String roleName,
                       java.lang.String dataString)
Deletes all the participants of this relationship that match this role
 and the specified data.

void
deleteParticipantStringByID(java.lang.String relationshipName,
                           java.lang.String roleName,
                           int instanceID,
                           java.lang.String dataString)
Deletes all the participants that match this relationship name, role name,
 relationship instanceID and the data.

boolean
existsParticipant(java.lang.String relationshipName,
                 java.lang.String roleName,
                 commonj.sdo.DataObject bo)
Determines the existence of a participant that matches this relationship,
 ASBO role and BO.

boolean
existsParticipantByID(java.lang.String relationshipName,
                     java.lang.String roleName,
                     int instanceId)
Determines the existence of a participant that matches this relationship,
 ASBO role and owns the given relationship instanceID.

void
foreignKeyLookup(java.lang.String foreignRelationshipName,
                java.lang.String foreignInputRoleName,
                commonj.sdo.DataObject inputBO,
                java.util.List inputBOForeignKeys,
                java.lang.String foreignOutputRoleName,
                commonj.sdo.DataObject outputBO,
                java.util.List outputBOForeignKeys,
                commonj.sdo.DataObject originalInputBO,
                commonj.sdo.DataObject originalOutputBO,
                java.lang.String callingContext)
Performs a lookup in the foreign relationship table based on the
 foreign key of the source business object in normal calling contexts
 (SERVICE\_CALL\_REQUEST, EVENT\_DELIVERY and SERVICE\_CALL\_RESPONSE).

void
foreignKeyXref(java.lang.String foreignRelationshipName,
              java.lang.String foreignInputRoleName,
              commonj.sdo.DataObject inputBO,
              java.util.List inputBOForeignKeys,
              java.lang.String foreignOutputRoleName,
              commonj.sdo.DataObject outputBO,
              java.util.List outputBOForeignKeys,
              commonj.sdo.DataObject originalInputBO,
              commonj.sdo.DataObject originalOutputBO,
              java.lang.String callingContext)
Performs a lookup in this foreign relationship table based on the
 foreign key of this input business object in the calling context
 SERVICE\_CALL\_REQUEST, EVENT\_DELIVERY and SERVICE\_CALL\_RESPONSE.

java.util.List
getListOfChildren(commonj.sdo.DataObject parent,
                 java.lang.String pathToChildren) 

int
getNewInstanceId(java.lang.String relationshipName)
Gets a new instance id for a new relationship instance
 
 
 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int instanceId = relService.getNewInstanceId("http://www.ibm.com/CustomerRel");

java.util.List
getRelationshipProperties(java.lang.String relationshipName,
                         java.lang.String propertyName)
Gets the values of a user defined relationship property for all instances
  of a relationship.

java.lang.Object
getRelationshipProperty(java.lang.String relationshipName,
                       java.lang.String propertyName,
                       int instanceid)
Gets the value of the user defined property in this relationship instance.

java.util.List
getRoleProperties(java.lang.String relationshipName,
                 java.lang.String roleName,
                 java.lang.String propertyName)
Gets the values of a user defined role property for all instances
  of the specified relatinoship, role.

java.util.List
getRoleProperties(java.lang.String relationshipName,
                 java.lang.String roleName,
                 java.lang.String propertyName,
                 int instanceid)
Gets the values of a user defined role property for a instance based on the given relationship
 name, role name, property name and instance id.

java.lang.Object
getRoleProperty(java.lang.String relationshipName,
               java.lang.String roleName,
               java.lang.String propertyName,
               int instanceid,
               java.lang.Object dataobject)
Gets the value of this user defined property for the given role
 instance.

boolean
isSetRelationshipProperty(java.lang.String relationshipName,
                         java.lang.String propertyName,
                         int instanceid)
Determines if the user defined property for the given relationship
 instance is set.

boolean
isSetRoleProperty(java.lang.String relationshipName,
                 java.lang.String roleName,
                 java.lang.String propertyName,
                 int instanceid,
                 java.lang.Object dataobject)
Determines if this user defined property for the given role instance is
 set.

void
maintainIdentityRelationship(java.lang.String relationshipName,
                            java.lang.String appRoleName,
                            commonj.sdo.DataObject inputBO,
                            commonj.sdo.DataObject outputBO,
                            commonj.sdo.DataObject originalInputBO,
                            commonj.sdo.DataObject originalOutputBO,
                            java.lang.String callingContext)
Deprecated. 
since WPS6.1 use correlate to maintain relationships
 and correlateToList and correlateFromList to maintain containment relatoinships

int[]
retrieveInstanceIDs(java.lang.String relationshipName,
                   java.lang.String roleName,
                   commonj.sdo.DataObject bo)
Retrieves instance ids of relationship instances that match this
 relationship name, role name and BO.

int[]
retrieveInstanceIDsByBoolean(java.lang.String relationshipName,
                            java.lang.String roleName,
                            boolean dataSimpleType)
Retrieves ids of all the participants that match this relationship,
 role and data.

int[]
retrieveInstanceIDsByDouble(java.lang.String relationshipName,
                           java.lang.String roleName,
                           double dataSimpleType)
Retrieves ids of all the participants that match this relationship,
 role and data.

int[]
retrieveInstanceIDsByFloat(java.lang.String relationshipName,
                          java.lang.String roleName,
                          float dataSimpleType)
Retrieves ids of all the participants that match this relationship,
 role and data.

int[]
retrieveInstanceIDsByInt(java.lang.String relationshipName,
                        java.lang.String roleName,
                        int dataSimpleType)
Retrieves ids of all the participants that match this relationship,
 role and data.

int[]
retrieveInstanceIDsByLong(java.lang.String relationshipName,
                         java.lang.String roleName,
                         long dataSimpleType)
Retrieves ids of all the participants that match this relationship,
 role and data.

int[]
retrieveInstanceIDsByRelNameBoolean(java.lang.String relationshipName,
                                   boolean dataSimpleType)
Retrieves ids of the participants that match this relationship name and
 data.

int[]
retrieveInstanceIDsByRelNameDouble(java.lang.String relationshipName,
                                  double dataSimpleType)
Retrieves ids of the participants that match this relationship name and
 data.

int[]
retrieveInstanceIDsByRelNameFloat(java.lang.String relationshipName,
                                 float dataSimpleType)
Retrieves ids of the participants that match this relationship name and
 data.

int[]
retrieveInstanceIDsByRelNameInt(java.lang.String relationshipName,
                               int dataSimpleType)
Retrieves ids of the participants that match this relationship name and
 data.

int[]
retrieveInstanceIDsByRelNameLong(java.lang.String relationshipName,
                                long dataSimpleType)
Retrieves ids of the participants that match this relationship name and
 data.

int[]
retrieveInstanceIDsByRelNameString(java.lang.String relationshipName,
                                  java.lang.String dataString)
Retrieves ids of the participants that match this relationship name and
 data.

int[]
retrieveInstanceIDsByRoleNameBoolean(java.lang.String relationshipName,
                                    java.lang.String[] roleName,
                                    boolean dataSimpleType)
Retrieves ids of the participants that match the relationship name,
 the list of role names and the specified data.

int[]
retrieveInstanceIDsByRoleNameDouble(java.lang.String relationshipName,
                                   java.lang.String[] roleName,
                                   double dataSimpleType)
Retrieves ids of the participants that match the relationship name,
 the list of role names and the specified data.

int[]
retrieveInstanceIDsByRoleNameFloat(java.lang.String relationshipName,
                                  java.lang.String[] roleName,
                                  float dataSimpleType)
Retrieves ids of the participants that match the relationship name,
 the list of role names and the specified data.

int[]
retrieveInstanceIDsByRoleNameInt(java.lang.String relationshipName,
                                java.lang.String[] roleName,
                                int dataSimpleType)
Retrieves ids of the participants that match the relationship name,
 the list of role names and the specified data.

int[]
retrieveInstanceIDsByRoleNameLong(java.lang.String relationshipName,
                                 java.lang.String[] roleName,
                                 long dataSimpleType)
Retrieves ids of the participants that match the relationship name,
 the list of role names and the specified data.

int[]
retrieveInstanceIDsByRoleNameString(java.lang.String relationshipName,
                                   java.lang.String[] roleName,
                                   java.lang.String dataString)
Retrieves ids of the participants that match this relationship name,
 the list of role names and the specified data.

int[]
retrieveInstanceIDsByString(java.lang.String relationshipName,
                           java.lang.String roleName,
                           java.lang.String dataString)
Retrieves ids of all the participants that match this relationship,
 role and data.

int[]
retrieveInstanceIDsForParentObject(java.lang.String relationshipName,
                                  java.lang.String roleName,
                                  commonj.sdo.DataObject parent)
Retrieves InstanceIDs of the partcipants whose parent data match this
 parent ASBO.

int[]
retrieveInstanceIDsUseDeactivate(java.lang.String relationshipName,
                                java.lang.String roleName,
                                java.lang.String dataString)
Retrieves ids of relationship instances that match this relationship
 name, role name and data.

java.util.List
retrieveParticipants(java.lang.String relationshipName)
Retrieves all the participants of this relationship.

java.util.List
retrieveParticipants(java.lang.String relationshipName,
                    java.lang.String roleName)
Retrieves all the participants of this relationship that match this ASBO
 roleName.

java.util.List
retrieveParticipants(java.lang.String relationshipName,
                    java.lang.String[] roleNames)
Retrieves all the participants from this relationship and the list of
 ASBO roles.

java.util.List
retrieveParticipants(java.lang.String relationshipName,
                    java.lang.String roleName,
                    int instanceId)
Retrieves all the participants of this relationship that match this
  ASBO roleName and have this instance id.

java.util.List
retrieveParticipantsByRelationshipName(java.lang.String relationshipName,
                                      int instanceID)
Retrieves all the matched participants from all the ASBO roles of this
 relationship.

java.util.List
retrieveParticipantsByRoleName(java.lang.String relationshipName,
                              java.lang.String[] roleNames,
                              int instanceID)
Retrieves all the participants from this relationship and the list of ASBO
 roles.

void
setRelationshipProperties(java.lang.String relationshipName,
                         java.lang.String propertyName,
                         java.lang.Object propertyValue)
Sets a relationship property to a specified value for all the instances of a relationship.

void
setRelationshipProperty(java.lang.String relationshipName,
                       java.lang.String propertyName,
                       java.lang.Object value,
                       int instanceid)
Sets value for the user defined property into this relationship instance.

void
setRoleProperties(java.lang.String relationshipName,
                 java.lang.String roleName,
                 java.lang.String propertyName,
                 java.lang.Object propertyValue)
Sets a role property to a specified value for all instances.

void
setRoleProperties(java.lang.String relationshipName,
                 java.lang.String roleName,
                 java.lang.String propertyName,
                 java.lang.Object propertyValue,
                 int instanceid)
Sets a role property to a specified value for a relationship instance.

void
setRoleProperty(java.lang.String relationshipName,
               java.lang.String roleName,
               java.lang.String propertyName,
               java.lang.Object propertyValue,
               int instanceid,
               java.lang.Object object)
Sets the specified property with the specifed value for the given
 role instance.

void
setRolePropertyWithOldValue(java.lang.String relationshipName,
                           java.lang.String roleName,
                           java.lang.String propertyName,
                           java.lang.Object propertyValue,
                           java.lang.Object oldPropertyValue,
                           int instanceid)
Sets this propertyValue to the given role property in the role instance.

void
staticLookup(java.lang.String relName,
            java.lang.String inputRoleName,
            commonj.sdo.DataObject inputBO,
            java.lang.String[] inputAttrNames,
            java.lang.String outputRoleName,
            commonj.sdo.DataObject outputBO,
            java.lang.String[] outputAttrNames)
Performs a static relationship lookup using input Business Object and its property name.

java.lang.Object
staticLookup(java.lang.String relName,
            java.lang.String inputRoleName,
            java.lang.Object inputAttrValue,
            java.lang.String outputRoleName)
Performs a static lookup by taking relationship name, input and output role names
 and input key attribute value.

void
unsetRelationshipProperties(java.lang.String relationshipName,
                           java.lang.String propertyName)
Unsets a relationship property for all instances of a relationship.

void
unsetRelationshipProperty(java.lang.String relationshipName,
                         java.lang.String propertyName,
                         int instanceid)
Unsets this property for the given relationship instance.

void
unsetRoleProperties(java.lang.String relationshipName,
                   java.lang.String roleName,
                   java.lang.String propertyName)
Unsets a role property for all relationship instances.

void
unsetRoleProperties(java.lang.String relationshipName,
                   java.lang.String roleName,
                   java.lang.String propertyName,
                   int instanceid)
Unsets a role property for a relationship instance.

void
unsetRoleProperty(java.lang.String relationshipName,
                 java.lang.String roleName,
                 java.lang.String propertyName,
                 int instanceid,
                 java.lang.Object dataobject)
Removes property value for this this role instance.It can be used for
 static as well as dynamic relationship.

void
unsetRolePropertyWithOldValue(java.lang.String relationshipName,
                             java.lang.String roleName,
                             java.lang.String propertyName,
                             java.lang.Object oldPropertyValue,
                             int instanceid)
Unsets value of this role property in the give role instance.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - foreignKeyXref void foreignKeyXref(java.lang.String foreignRelationshipName, java.lang.String foreignInputRoleName, commonj.sdo.DataObject inputBO, java.util.List inputBOForeignKeys, java.lang.String foreignOutputRoleName, commonj.sdo.DataObject outputBO, java.util.List outputBOForeignKeys, commonj.sdo.DataObject originalInputBO, commonj.sdo.DataObject originalOutputBO, java.lang.String callingContext) throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException, com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException, com.ibm.wbiserver.relationshipservice.exceptions.MissingIdException Performs a lookup in this foreign relationship table based on the foreign key of this input business object in the calling context SERVICE\_CALL\_REQUEST, EVENT\_DELIVERY and SERVICE\_CALL\_RESPONSE. Currently it supports single foreign key attribute only. Parameters: foreignRelationshipName - name of the foreign identity relationship that manages the foreign business object foreignInputRoleName - role name of the foreign relationship for the foreign incoming object inputBO - input business object that contains the foreign attributes for this foreign input role. It could also be a BusinessGraph. inputBOForeignKeys - names of the attributes defined in this foreign input role foreignOutputRoleName - role name of the foreign relationship for the foregin outgoing object outputBO - output business object that contains the foreign attributes for this foreign output role. It could also be a BusinessGraph. outputBOForeignKeys - names of the attributes defined in this foregin output role originalInputBO - original input business object that contains the foreign key attributes. It could also be a BusinessGraph. originalOutputBO - original output business object that contains the foreign key attributes. It could also be a BusinessGraph. callingContext - calling context. It could be SERVICE\_CALL\_REQUEST, EVENT\_DELIVERY, SERVICE\_CALL\_RESPONSE and SERVICE\_CALL\_FAILURE. Throws: com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException com.ibm.wbiserver.relationshipservice.exceptions.MissingIdException

#### foreignKeyXref

```
void foreignKeyXref(java.lang.String foreignRelationshipName,
                  java.lang.String foreignInputRoleName,
                  commonj.sdo.DataObject inputBO,
                  java.util.List inputBOForeignKeys,
                  java.lang.String foreignOutputRoleName,
                  commonj.sdo.DataObject outputBO,
                  java.util.List outputBOForeignKeys,
                  commonj.sdo.DataObject originalInputBO,
                  commonj.sdo.DataObject originalOutputBO,
                  java.lang.String callingContext)
                    throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                           com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException,
                           com.ibm.wbiserver.relationshipservice.exceptions.MissingIdException
```

Currently it supports single foreign key attribute only.

 
 In the calling context SERVICE\_CALL\_REQUEST,
 the foreign input role is an ASBO role and the foreign output role is a GBO role.
 In this case, this inputBOForeignKeys refers to the key attribute in the
 foreign ASBO; the outputBOForeignKeys refers to the key attriubte in the
 foreign GBO.

 

Verb/ChangeSummary on the inputBO
Existing entry found in table
Entry not found in table

Create
Gets the value of the instance Id corresponding to the row with
 inputForeignAttr value and inserts this value in the outputBO for
 outputForeignAttr.
Generates a new instance Id in the foreign table. 

 This instance id should be put in the outputBO in the outputForeignAttr.
 Do not create a row in the foreign table. This will be created only on
 the response path.

Update
Gets the value of the instance Id corresponding to the row with
 inputForeignAttr value and inserts this value in the outputBO for
 outputForeignAttr. 
Throws MissingIdException

Delete,
 All other verbs
Gets the value of the instance Id corresponding to the row with
 inputForeignAttr value and inserts this value in the outputBO for
 outputForeignAttr.
Throws MissingIdException

UpdateWithDelete
This means that the object could be in the deleted list in the
 change summary. Hence first gets the verb, ensures whether it is an update,
 create or delete and then applies the appropriate behavior as defined above.
Processes differently according to different verb/ChangeSummary

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.foreignKeyXref("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", inputBG, foreignSAPBOAttrList,
                        "http://www.ibm.com/CustomGenRole", genBG, foreignGenBOAttrList, null, null, SERVICE\_CALL\_REQUEST);

 In the calling context EVENT\_DELIVERY,
 the foreign input role is an ASBO role and the foreing output role is a GBO role.
 Here this inputBOForeignKeys refers to the key attribute in the foreign ASBO;
 this outputBOForeignKeys refers to the key attriubte in the foreign GBO.

 

Verb/ChangeSummary on the inputBO
Existing entry found in table
Entry not found in table

Create
Gets the value of the instance Id corresponding to the row with
 inputForeignAttr value and inserts this value in the outputBO for
 outputForeignAttr. 
Creates a new row in the foreign table with the given
 inputForeignAttr as the role key and gets the generated instance id and
 inserts it in the outputForeignAttr of the outputBO.

Update
Gets the value of the instance Id corresponding to the row with
 inputForeignAttr value and inserts this value in the outputBO for
 outputForeignAttr. 
Creates a new row in the foreign table with the given
 inputForeignAttr as the role key and gets the generated instance id and
 inserts it in the outputForeignAttr of the outputBO.

Delete
Gets the value of the instance Id corresponding to the row with
 inputForeignAttr value and inserts this value in the outputBO for
 outputForeignAttr. 
Throws MissingIdException

UpdateWithDelete
This means that the object could be in the deleted list in the
 change summary. Hence first gets the verb, ensures whether it is an update,
 create or delete and then applies the appropriate behavior as defined above.
Processes differently according to different verb/ChangeSummary

All other verbs
Gets the value of the instance Id corresponding to the row with
 inputForeignAttr value and inserts this value in the outputBO for
 outputForeignAttr
Creates a new row in the foreign table with the given inputForeignAttr
 as the role key and gets the generated instance id and inserts it in the
 outputForeignAttr of the outputBO.

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.foreignKeyXref("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", inputBG, foreignSAPBOAttrList,
                        "http://www.ibm.com/CustomGenRole", genBG, foreignGenBOAttrList, null, null, EVENT\_DELIVERY);

 In the calling context SERVICE\_CALL\_REQUEST/EVENT\_DELIVERY,
 the foreign input role is a GBO role and the foreing output role is an ASBO role.
 In this case, this inputBOForeignKeys refers to the key attribute in the foreign GBO;
 the outputBOForeignKeys refers to the key attriubte in the foreign ASBO.

 

Verb/ChangeSummary on the inputBO
Existing entry found in table
Entry not found in table

Create,

                        Update,

                        UpdateWithDelete,

                        Delete,

                        All other verbs
                
Gets the value of the outputForeignAttr corresponding to the
 row with inputForeignAttr (InstanceId) value and inserts this value in
 the outputBO in outputForeignAttr.
Throws MissingIdException

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.foreignKeyXref("http://www.ibm.com/CustomerRel", "http://www.ibm.com/CustomGenRole", genBG, foreignGenBOAttrList,
                                "http://www.clarify.com/ClarifyRole", inputBG, foreignClarifyBOAttrList, null, null, EVENT\_DELIVERY);

 In the calling context SERVICE\_CALL\_RESPONSE,
 the foreign input role is an ASBO role and the foreing output role is a GBO role.
 Here this inputBOForeignKeys refers to the key attribute in the foreign ASBO,
 and the outputBOForeignKeys refers to the key attriubte in the foreign GBO.

 

Verb/ChangeSummary on the inputBO
Existing entry found in table
Entry not found in table

Create,

                        Update
                
Gets the value of the outputForeignAttr given the
 inputForeignAttr value which is now the instanceId and inserts this
 value in the outputBO for outputForeignAttr.
Creates a new row in the foreign table with the given
 inputForeignAttr as the instance Id and gets the foreign key value from
 the origOutputBO that is sent in. The foreign key value from the
 origOutputBO should be put in the outputBO in the outputForeignAttr.

Delete,

                        All other verbs
                
Gets the value of the outputForeignAttr given the
 inputForeignAttr value which is now the instanceId and inserts this value
 in the outputBO for outputForeignAttr. In the case of Delete, since there
 are no objects in the graph, we will use the origOutputBO which is the
 ASBO.
Throws MissingIdException

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.foreignKeyXref("http://www.ibm.com/CustomerRel", "http://www.clarify.com/ClarifyRole", inputBG, foreignClarifyBOAttrList,
                        "http://www.ibm.com/CustomGenRole", genBG, foreignGenBOAttrList, origInputBG, null, SERVICE\_CALL\_RESPONSE);

 In the calling context SERVICE\_CALL\_RESPONSE,
 foreign input role is a GBO role and foreing output role is an ASBO role.
 In this case, this inputBOForeignKeys refers to the key attribute in the foreign GBO;
 the outputBOForeignKeys refers to the key attriubte in the foreign ASBO.

 

Verb/ChangeSummary on the inputBO
Existing entry found in table
Entry not found in table

Create,
 Update
Gets the value of the outputForeignAttr given the
 inputForeignAttr value which is the instanceId and inserts this value
 in the outputBO for outputForeignAttr.
Create a new row in the foreign table with the given
 inputForeignAttr as the instance Id and gets the foreign key value
 from the origInputBO that is sent in. The foreign key value from the
 origInputBO should be put in the outputBO in the outputForeignAttr.

Delete,
 All other verbs
Gets the value of the outputForeignAttr given the
 inputForeignAttr value which is the instanceId and inserts
 this value in the outputBO for outputForeignAttr
Throws MissingIdException

UpdateWithDelete
This means that the object could be in the deleted list in the
 change summary. Hence first get the verb, ensure whether it is an
 update, create or delete and then apply the appropriate behavior as
 defined above.
Processes differently according to different verb/ChangeSummary.

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.foreignKeyXref("http://www.ibm.com/CustomerRel", "http://www.ibm.com/CustomGenRole", genBG, foreignGenBOAttrList,
                                 "http://www.sap.com/SAPRole", inputBG, foreignSAPBOAttrList, origInputBG, null, SERVICE\_CALL\_RESPONSE);

 In the calling context SERVICE\_CALL\_FAILURE, it simply returns
 the inputBOForeignKey of this originalInputBO.

- foreignKeyLookup void foreignKeyLookup(java.lang.String foreignRelationshipName, java.lang.String foreignInputRoleName, commonj.sdo.DataObject inputBO, java.util.List inputBOForeignKeys, java.lang.String foreignOutputRoleName, commonj.sdo.DataObject outputBO, java.util.List outputBOForeignKeys, commonj.sdo.DataObject originalInputBO, commonj.sdo.DataObject originalOutputBO, java.lang.String callingContext) throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException, com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException, com.ibm.wbiserver.relationshipservice.exceptions.MissingIdException Performs a lookup in the foreign relationship table based on the foreign key of the source business object in normal calling contexts (SERVICE\_CALL\_REQUEST, EVENT\_DELIVERY and SERVICE\_CALL\_RESPONSE). If the instance is not found, a MissingIdException is thrown . If the verb or change of inputBO is not set, a RelationshipServiceException is thrown. If the calling context is SERVICE\_CALL\_FAILURE, it simply returns outputBOForeignKeys of originalInputBO. Currently it supports single foreign key attribute only. Parameters: foreignRelationshipName - name of the foreign identity relationship that manages the foreign business object foreignInputRoleName - role name of the foreign relationship for the foreign incoming object inputBO - input business object that contains the foreign attributes for this foreign input role. It could also be a BusinessGraph. inputBOForeignKeys - names of the attributes defined in this foreign input role foreignOutputRoleName - role name of the foreign relationship for the foregin outgoing object outputBO - output business object that contains the foreign attributes for this foreign output role. It could also be a BusinessGraph. outputBOForeignKeys - names of the attributes defined in this foregin output role originalInputBO - original input business object that contains the foreign key attributes. It could also be a BusinessGraph. originalOutputBO - original output business object that contains the foreign key attributes. It could also be a BusinessGraph. callingContext - calling context. It could be SERVICE\_CALL\_REQUEST, EVENT\_DELIVERY, SERVICE\_CALL\_RESPONSE and SERVICE\_CALL\_FAILURE. Throws: com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException com.ibm.wbiserver.relationshipservice.exceptions.MissingIdException

#### foreignKeyLookup

```
void foreignKeyLookup(java.lang.String foreignRelationshipName,
                    java.lang.String foreignInputRoleName,
                    commonj.sdo.DataObject inputBO,
                    java.util.List inputBOForeignKeys,
                    java.lang.String foreignOutputRoleName,
                    commonj.sdo.DataObject outputBO,
                    java.util.List outputBOForeignKeys,
                    commonj.sdo.DataObject originalInputBO,
                    commonj.sdo.DataObject originalOutputBO,
                    java.lang.String callingContext)
                      throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                             com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException,
                             com.ibm.wbiserver.relationshipservice.exceptions.MissingIdException
```

Currently it supports single foreign key attribute only.

 

 The foreign input role is an ASBO role and the foreign output role is a GBO role:

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.foreignKeyLookup("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", srcBG, srcBOForeAttrList,
                                "http://www.ibm.com/CustomGenRole", genBG, genBOForeAttrList, null, null, SERVICE\_CALL\_REQUEST);

 The foreign input role is a GBO role and the foreign output role is an ASBO role:

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.foreignKeyLookup("http://www.ibm.com/CustomerRel", "http://www.ibm.com/CustomGenRole", genBG, genBOForeAttrList,
                                "http://www.clarify.com/ClarifyRole", destBG, destBOForeAttrList, null, null, SERVICE\_CALL\_REQUEST);

- addParticipant
int addParticipant(java.lang.String relationshipName,
                 java.lang.String roleName,
                 commonj.sdo.DataObject bo)
                   throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                          com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant to a new relationship instance. This BO contains value
 for the target participant that match the given relationship and ASBO
 role. This API can be used for static as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.addParticipant("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", sapCustomer);

Parameters:relationshipName - name of the relationship to add the participant to. If no Relationship
 found, RelationshipUserException is thrown.roleName - name of the ASBO role to add the participant to. If no role found,
 RelationshipUserException is thrown.bo - ASBO that contains value for the participant. It could also be a
 BusinessGraph. If there is a matched existing participant, the instance
 id of the existing one is returned.
Returns:relationship instance ID
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipantWithID
int addParticipantWithID(java.lang.String relationshipName,
                       java.lang.String roleName,
                       int instanceId,
                       commonj.sdo.DataObject bo)
                         throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant for an existing relationship instance that match this
 relationship, ASBO role and instance id. This API can be used for static
 as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.addParticipantWithID("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", 1, sapCustomer);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException is thrown.roleName - name of the ASBO role to add the participant to. If no role found,
 RelationshipUserException is thrown.instanceId - given relationship instanceIDbo - ASBO that contains value for the participant. It could also be a
 BusinessGraph. If there is a matched existing participant, the instance
 id of the existing one is returned.
Returns:relationship instance ID
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- existsParticipant
boolean existsParticipant(java.lang.String relationshipName,
                        java.lang.String roleName,
                        commonj.sdo.DataObject bo)
                          throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                 com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Determines the existence of a participant that matches this relationship,
 ASBO role and BO. This API can be used for static as well as dynamic
 relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 boolean result = relService.existsParticipant("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", sapCustomer);

Parameters:relationshipName - name of the relationship to check. If no relationship found,
 RelationshipUserException is thrown.roleName - name of the ASBO role to check. If no role found,
 RelationshipUserException is thrown.bo - ASBO contains the value for the target participant. It could also be
 a BusinessGraph.
Returns:true, if a matched participant exists
   false, if can't find a matched participant.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- existsParticipantByID
boolean existsParticipantByID(java.lang.String relationshipName,
                            java.lang.String roleName,
                            int instanceId)
                              throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                     com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Determines the existence of a participant that matches this relationship,
 ASBO role and owns the given relationship instanceID. This API can be
 used for static as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 boolean result = relService.existsParticipantByID("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", 1);

Parameters:relationshipName - name of the relationship to check. If no relationship found,
 RelationshipUserException is thrown.roleName - name of the ASBO role to check. If no role found,
 RelationshipUserException is thrown.instanceId - given relationship instanceID
Returns:true, if a matched participant exists
   false, if can't find a matched participant.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deactivateParticipant
void deactivateParticipant(java.lang.String relationshipName,
                         java.lang.String roleName,
                         commonj.sdo.DataObject bo)
                           throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                  com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deactivates all the participants of this relationship that match the
 specified BO. This BO contains value for the ASBO role. It could
 aslo be a BusinessGraph. This API can be used for static as well as
 dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deactivateParticipant("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", sapCustomer);

Parameters:relationshipName - name of the relationship to deactivate the participants from. If no
 relationship found, RelationshipUserException is thrown.roleName - name of the ASBO role to deactivate the partcipants from. If no role found,
 RelationshipUserException is thrown.bo - ASBO contains value for the partcipants to be deleted. It could aslo
 be a BusinessGraph.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deactivateParticipantByID
void deactivateParticipantByID(java.lang.String relationshipName,
                             java.lang.String roleName,
                             int instanceId)
                               throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                      com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deactivates all the participants of this relationship that matche the
 specified relationship instanceID. This API can be used for static as
 well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deactivateParticipantByID("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", 1);

Parameters:relationshipName - name of the relationship to deactivate the participants from. If no
 relationship found, RelationshipUserException is thrown.roleName - name of the ASBO role to deactivate the participants from. If no role found,
 RelationshipUserException is thrown.instanceId - specified relationship instanceID
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deactivateParticipantByIDAndDO
void deactivateParticipantByIDAndDO(java.lang.String relationshipName,
                                  java.lang.String roleName,
                                  int instanceId,
                                  commonj.sdo.DataObject bo)
                                    throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                           com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deactivates all the partcipants that match this relationship, role, BO and
 instanceId. The BO contains value for the ASBO role. This API can
 be used for static as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deactivateParticipantByIDAndDO("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", 1, sapCustomer);

Parameters:relationshipName - name of the relationship to deactivate the partcipant from. If no
 relationship found, RelationshipUserException is thrown.roleName - name of the ASBO role to deactivate the partcipant from. If no role found,
 RelationshipUserException is thrown.instanceId - specified relationship instanceIDbo - ASBO contains value for the partcipant to be deleted. It could also be
 a BusinessGraph.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipant
void deleteParticipant(java.lang.String relationshipName,
                     java.lang.String roleName,
                     commonj.sdo.DataObject bo)
                       throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                              com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants of this relationship that match the
 specified BO. This BO contains value for the ASBO role. It could
 aslo be a BusinessGraph. This API can be used for static as well as
 dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deleteParticipant("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", sapCustomer);

Parameters:relationshipName - name of the relationship to delete the participants from. If no
 relationship found, RelationshipUserException is thrown.roleName - name of the ASBO role to delete the partcipants from. If no role found,
 RelationshipUserException is thrown.bo - ASBO contains value for the partcipants to be deleted. It could aslo
 be a BusinessGraph.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipantByID
void deleteParticipantByID(java.lang.String relationshipName,
                         java.lang.String roleName,
                         int instanceId)
                           throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                  com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants of this relationship that matche the
 specified relationship instanceID. This API can be used for static as
 well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deleteParticipantByID("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", 1);

Parameters:relationshipName - name of the relationship to delete the participants from. If no
 relationship found, RelationshipUserException is thrown.roleName - name of the ASBO role to delete the participants from. If no role found,
 RelationshipUserException is thrown.instanceId - specified relationship instanceID
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipantByIDAndDO
void deleteParticipantByIDAndDO(java.lang.String relationshipName,
                              java.lang.String roleName,
                              int instanceId,
                              commonj.sdo.DataObject bo)
                                throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                       com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the partcipants that match this relationship, role, BO and
 instanceId. The BO contains value for the ASBO role. This API can
 be used for static as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deleteParticipantByIDAndDO("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", 1, sapCustomer);

Parameters:relationshipName - name of the relationship to delete the partcipant from. If no
 relationship found, RelationshipUserException is thrown.roleName - name of the ASBO role to delete the partcipant from. If no role found,
 RelationshipUserException is thrown.instanceId - specified relationship instanceIDbo - ASBO contains value for the partcipant to be deleted. It could also be
 a BusinessGraph.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteAllParticipants
void deleteAllParticipants(java.lang.String relationshipName,
                         java.lang.String roleName)
                           throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                  com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants for this relationship and the ASBO role.
 It can be used for static as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deleteAllParticipants("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole");

Parameters:relationshipName - name of the relationship to delete the participants from. If no
 relationship found, RelationshipUserException is thrown.roleName - name of the role to delete the partcipants from. If no role found,
 RelationshipUserException is thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDs
int[] retrieveInstanceIDs(java.lang.String relationshipName,
                        java.lang.String roleName,
                        commonj.sdo.DataObject bo)
                          throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                 com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves instance ids of relationship instances that match this
 relationship name, role name and BO.
 The BO contains the key values for the ASBO role. It could also be a
 BusinessGraph.
 This API can be used for static as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int[] ids = relService.retrieveInstanceIDs("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", sapCustomer);

Parameters:relationshipName - name of the relationship to retrieve the instanceIDs from. If no
 relationship found, RelationshipUserException
 will be thrown.roleName - name of the ASBO role for retrieve. If no role found,
 RelationshipUserException will be thrown.bo - ASBO that corresponds to this role. It could be a BusinessObject or a
 BusinessGraph. Either null value or a empty BusinessGraph
 instance that could not retrieve a BusinessObject from will cause
 RelationshipUserException
Returns:a int array of instance ids. If no target instance found, an empty
 int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsForParentObject
int[] retrieveInstanceIDsForParentObject(java.lang.String relationshipName,
                                       java.lang.String roleName,
                                       commonj.sdo.DataObject parent)
                                         throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                                com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves InstanceIDs of the partcipants whose parent data match this
 parent ASBO. It is used in the case of composite relationship where ASBO
 Roles contain both key attributes of parent ASBO and child ASBO.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int[] ids = relService.retrieveInstanceIDsForParentObject("http://www.ibm.com/CompositeRel", "http://www.ibm.com/Level1InRol", level1InBO);

Parameters:relationshipName - name of the composite relationship to retrieve instanceIDs fromroleName - name of the ASBO role to retrieve instanceIDs fromparent - parent ASBO contained in the target participant instances. It could
 also be a BusinessGraph.
Returns:int array of matched instance ids. If no target instance found, an
 empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveParticipants
java.util.List retrieveParticipants(java.lang.String relationshipName,
                                  java.lang.String roleName,
                                  int instanceId)
                                    throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                           com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves all the participants of this relationship that match this
  ASBO roleName and have this instance id.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 List partcipants = relService.retrieveParticipants("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", 1);
 
Parameters:relationshipName - name of the relationship to retrieve the participants from. If no
 relationship found, RelationshipUserException
 will be thrown.roleName - name of the role to retrieve the participants from. If no role found,
 RelationshipUserException will be thrown.instanceId - instanceID of the target participants. It should be greater than zero.
Returns:a list of the matched participants. If no matched participant found,
 an empty list will be returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveParticipants
java.util.List retrieveParticipants(java.lang.String relationshipName,
                                  java.lang.String roleName)
                                    throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                           com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves all the participants of this relationship that match this ASBO
 roleName.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 List partcipants = relService.retrieveParticipants("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole");
 

Parameters:relationshipName - name of the relationship to retrieve the participants from. If
            no relationship found, RelationshipUserException
            will be thrown.roleName - name of the role to retrieve the participants from. If no role
            found, RelationshipUserException will be
            thrown.
Returns:a list of the matched participants. If no matched participant
         found, an empty list will be returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveParticipants
java.util.List retrieveParticipants(java.lang.String relationshipName)
                                    throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                           com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves all the participants of this relationship.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 List partcipants = relService.retrieveParticipants("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole");
 

Parameters:relationshipName - name of the relationship to retrieve the participants from. If
            no relationship found, RelationshipUserException
            will be thrown.
Returns:a list of the matched participants. If no matched participant
         found, an empty list will be returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveParticipants
java.util.List retrieveParticipants(java.lang.String relationshipName,
                                  java.lang.String[] roleNames)
                                    throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                           com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves all the participants from this relationship and the list of
 ASBO roles.
Parameters:relationshipName - name of the relationship to retrieve the participants from. If
            no relationship found, RelationshipUserException
            will be thrown.roleNames - list of role names. If any role in the list could not be
            found, RelationshipUserException is thrown.
Returns:list of all the matced partcipants. If no matched participant
         found, an empty list is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- createParticipantString
int createParticipantString(java.lang.String relationshipName,
                          java.lang.String roleName,
                          java.lang.String dataString)
                            throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                   com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant to a new relationship instance. This role contains a
 roleObject of String type and a keyAttribute whose path is defined as
 "Data". Value for this role is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.createParticipantString("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "value\_String");

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.dataString - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- createParticipantLong
int createParticipantLong(java.lang.String relationshipName,
                        java.lang.String roleName,
                        long dataSimpleType)
                          throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                 com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant to a new relationship instance. This role contains a
 roleObject of long type and a keyAttribute whose path is defined as "Data".
 Value for this role is specified by the data. This API supports static
 relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.createParticipantLong("http://www.ibm.com/StaticRel", "http://www.ibm.com/longRole", -9223372036854775808);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- createParticipantInt
int createParticipantInt(java.lang.String relationshipName,
                       java.lang.String roleName,
                       int dataSimpleType)
                         throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant to a new relationship instance. This role contains a
 roleObject of int type and a keyAttribute whose path is defined as
 "Data". Value for this role is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.createParticipantInt("http://www.ibm.com/StaticRel", "http://www.ibm.com/intRole", -2147483648);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- createParticipantFloat
int createParticipantFloat(java.lang.String relationshipName,
                         java.lang.String roleName,
                         float dataSimpleType)
                           throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                  com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant to a new relationship instance. This role contains a
 roleObject of float type and a keyAttribute whose path is defined as
 "Data". Value for this role is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.createParticipantFloat("http://www.ibm.com/StaticRel", "http://www.ibm.com/floatRole", -3.40282346638528860e+38F);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- createParticipantDouble
int createParticipantDouble(java.lang.String relationshipName,
                          java.lang.String roleName,
                          double dataSimpleType)
                            throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                   com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant to a new relationship instance. This role contains a
 roleObject of double type and a keyAttribute whose path is defined as
 "Data". Value for this role is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.createParticipantDouble("http://www.ibm.com/StaticRel", "http://www.ibm.com/doubleRole", 4.94065645841246544e-324D);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- createParticipantBoolean
int createParticipantBoolean(java.lang.String relationshipName,
                           java.lang.String roleName,
                           boolean dataSimpleType)
                             throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                    com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant to a new relationship instance. This role contains a
 roleObject of boolean type and a keyAttribute whose path is defined as
 "Data". Value for this role is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.createParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- createParticipantStringWithID
int createParticipantStringWithID(java.lang.String relationshipName,
                                java.lang.String roleName,
                                int instanceID,
                                java.lang.String dataString)
                                  throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                         com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant for an existing relationship instance. This role
 contains a roleObject of String type and a keyAttribute whose path
 is defined as "Data". Value for this role is specified by the data.
 This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int origId = relService.createParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

 int id = relService.createParticipantStringWithID("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", origId, "value\_String");

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.instanceID - instanceID of the existing relationship instance. InstanceID equal
 with or less than zero is not valid.dataString - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- createParticipantLongWithID
int createParticipantLongWithID(java.lang.String relationshipName,
                              java.lang.String roleName,
                              int instanceID,
                              long dataSimpleType)
                                throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                       com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant for an existing relationship instance. This role
 contains a roleObject of long type and a keyAttribute whose path is
 defined as "Data". Value for this role is specified by the data.
 This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int origId = relService.createParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

 int id = relService.createParticipantLongWithID("http://www.ibm.com/StaticRel", "http://www.ibm.com/longRole", origId, -9223372036854775808);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.instanceID - instanceID of the existing relationship instance. InstanceID equal
 with or less than zero is not valid.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- createParticipantIntWithID
int createParticipantIntWithID(java.lang.String relationshipName,
                             java.lang.String roleName,
                             int instanceID,
                             int dataSimpleType)
                               throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                      com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant for an existing relationship instance. This role
 contains a roleObject of int type and a keyAttribute whose path is
 defined as "Data". Value for this role is specified by the data.
 This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int origId = relService.createParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

 int id = relService.createParticipantIntWithID("http://www.ibm.com/StaticRel", "http://www.ibm.com/intRole", origId, -2147483648);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.instanceID - instanceID of the existing relationship instance. InstanceID equal
 with or less than zero is not valid.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- createParticipantFloatWithID
int createParticipantFloatWithID(java.lang.String relationshipName,
                               java.lang.String roleName,
                               int instanceID,
                               float dataSimpleType)
                                 throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                        com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant for an existing relationship instance. This role
 contains a roleObject of float type and a keyAttribute whose path is
 defined as "Data". Value for this role is specified by the data.
 This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int origId = relService.createParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

 int id = relService.createParticipantFloatWithID("http://www.ibm.com/StaticRel", "http://www.ibm.com/floatRole", origId, -3.40282346638528860e+38F);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.instanceID - instanceID of the existing relationship instance. InstanceID equal
 with or less than zero is not valid.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- createParticipantDoubleWithID
int createParticipantDoubleWithID(java.lang.String relationshipName,
                                java.lang.String roleName,
                                int instanceID,
                                double dataSimpleType)
                                  throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                         com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant for an existing relationship instance. This role
 contains a roleObject of double type and a keyAttribute whose path is
 defined as "Data". Value for this role is specified by the data.
 This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int origId = relService.createParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

 int id = relService.createParticipantDoubleWithID("http://www.ibm.com/StaticRel", "http://www.ibm.com/doubleRole", origId, 4.94065645841246544e-324D);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.instanceID - instanceID of the existing relationship instance. InstanceID equal
 with or less than zero is not valid.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- createParticipantBooleanWithID
int createParticipantBooleanWithID(java.lang.String relationshipName,
                                 java.lang.String roleName,
                                 int instanceID,
                                 boolean dataSimpleType)
                                   throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                          com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant for an existing relationship instance. This role
 contains a roleObject of boolean type and a keyAttribute whose path is
 defined as "Data". Value for this role is specified by the data.
 This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int origId = relService.createParticipantString("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "value\_String");

 int id = relService.createParticipantBooleanWithID("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", origId, false);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.instanceID - instanceID of the existing relationship instance. InstanceID equal
 with or less than zero is not valid.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipantString
int addParticipantString(java.lang.String relationshipName,
                       java.lang.String roleName,
                       java.lang.String dataString)
                         throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant to a new relationship instance. This role contains a
 roleObject of String type and a keyAttribute whose path is defined as
 "Data". Value for this role is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.addParticipantString("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "value\_String");

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.dataString - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipantLong
int addParticipantLong(java.lang.String relationshipName,
                     java.lang.String roleName,
                     long dataSimpleType)
                       throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                              com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant to a new relationship instance. This role contains a
 roleObject of long type and a keyAttribute whose path is defined as
 "Data". Value for this role is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.addParticipantLong("http://www.ibm.com/StaticRel", "http://www.ibm.com/longRole", -9223372036854775808);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipantInt
int addParticipantInt(java.lang.String relationshipName,
                    java.lang.String roleName,
                    int dataSimpleType)
                      throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                             com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant to a new relationship instance. This role contains a
 roleObject of int type and a keyAttribute whose path is defined as
 "Data". Value for this role is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.addParticipantInt("http://www.ibm.com/StaticRel", "http://www.ibm.com/intRole", -2147483648);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipantFloat
int addParticipantFloat(java.lang.String relationshipName,
                      java.lang.String roleName,
                      float dataSimpleType)
                        throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                               com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant to a new relationship instance. This role contains a
 roleObject of float type and a keyAttribute whose path is defined as
 "Data". Value for this role is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.addParticipantFloat("http://www.ibm.com/StaticRel", "http://www.ibm.com/floatRole", -3.40282346638528860e+38F);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipantDouble
int addParticipantDouble(java.lang.String relationshipName,
                       java.lang.String roleName,
                       double dataSimpleType)
                         throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant to a new relationship instance. This role contains a
 roleObject of double type and a keyAttribute whose path is defined as
 "Data". Value for this role is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.addParticipantDouble("http://www.ibm.com/StaticRel", "http://www.ibm.com/doubleRole", 4.94065645841246544e-324D);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipantBoolean
int addParticipantBoolean(java.lang.String relationshipName,
                        java.lang.String roleName,
                        boolean dataSimpleType)
                          throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                 com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant to a new relationship instance. This role contains a
 roleObject of boolean type and a keyAttribute whose path is defined as
 "Data". Value for this role is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.addParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipantStringWithID
int addParticipantStringWithID(java.lang.String relationshipName,
                             java.lang.String roleName,
                             int instanceID,
                             java.lang.String dataString)
                               throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                      com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant for an existing relationship instance. This role
 contains a roleObject of String type and a keyAttribute whose path is
 defined as "Data". Value for this role is specified by the data. This
 API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int origId = relService.createParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

 int id = relService.addParticipantStringWithID("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", origId, "value\_String");

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.instanceID - instanceID of the existing relationship instance. InstanceID equal
 with or less than zero is not valid.dataString - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipantLongWithID
int addParticipantLongWithID(java.lang.String relationshipName,
                           java.lang.String roleName,
                           int instanceID,
                           long dataSimpleType)
                             throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                    com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant for an existing relationship instance. This role
 contains a roleObject of long type and a keyAttribute whose path is
 defined as "Data". Value for this role is specified by the data. This
 API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int origId = relService.createParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

 int id = relService.addParticipantLongWithID("http://www.ibm.com/StaticRel", "http://www.ibm.com/longRole", origId, -9223372036854775808);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.instanceID - instanceID of the existing relationship instance. InstanceID equal
 with or less than zero is not valid.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipantIntWithID
int addParticipantIntWithID(java.lang.String relationshipName,
                          java.lang.String roleName,
                          int instanceID,
                          int dataSimpleType)
                            throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                   com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant for an existing relationship instance. This role
 contains a roleObject of int type and a keyAttribute whose path is
 defined as "Data". Value for this role is specified by the data. This
 API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int origId = relService.createParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

 int id = relService.addParticipantIntWithID("http://www.ibm.com/StaticRel", "http://www.ibm.com/intRole", origId, -2147483648);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.instanceID - instanceID of the existing relationship instance. InstanceID equal
 with or less than zero is not valid.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipantFloatWithID
int addParticipantFloatWithID(java.lang.String relationshipName,
                            java.lang.String roleName,
                            int instanceID,
                            float dataSimpleType)
                              throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                     com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant for an existing relationship instance. This role
 contains a roleObject of float type and a keyAttribute whose path is
 defined as "Data". Value for this role is specified by the data. This
 API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int origId = relService.createParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

 int id = relService.addParticipantFloatWithID("http://www.ibm.com/StaticRel", "http://www.ibm.com/floatRole", origId, -3.40282346638528860e+38F);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.instanceID - instanceID of the existing relationship instance. InstanceID equal
 with or less than zero is not valid.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipantDoubleWithID
int addParticipantDoubleWithID(java.lang.String relationshipName,
                             java.lang.String roleName,
                             int instanceID,
                             double dataSimpleType)
                               throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                      com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant for an existing relationship instance. This role
 contains a roleObject of double type and a keyAttribute whose path is
 defined as "Data". Value for this role is specified by the data. This
 API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int origId = relService.createParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

 int id = relService.addParticipantDoubleWithID("http://www.ibm.com/StaticRel", "http://www.ibm.com/doubleRole", origId, 4.94065645841246544e-324D);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.instanceID - instanceID of the existing relationship instance. InstanceID equal
 with or less than zero is not valid.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipantBooleanWithID
int addParticipantBooleanWithID(java.lang.String relationshipName,
                              java.lang.String roleName,
                              int instanceID,
                              boolean dataSimpleType)
                                throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                       com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant for an existing relationship instance. This role
 contains a roleObject of boolean type and a keyAttribute whose path is
 defined as "Data". Value for this role is specified by the data. This
 API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int origId = relService.createParticipantString("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "value\_String");

 int id = relService.addParticipantBooleanWithID("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", origId, false);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to add the participant to. If no role found,
 RelationshipUserException will be thrown.instanceID - instanceID of the existing relationship instance. InstanceID equal
 with or less than zero is not valid.dataSimpleType - data of the participant to be added
Returns:relationship instanceID of the newly added participant
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deactivateParticipantString
void deactivateParticipantString(java.lang.String relationshipName,
                               java.lang.String roleName,
                               java.lang.String dataString)
                                 throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                        com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deactivates all the participants of this relationship that match this
 data for the participant. This role contains a roleObject of String type
 and a keyAttribute whose path is defined as "Data". Value for this role
 is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deactivateParticipantString("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "value\_String");

Parameters:relationshipName - name of the relationship to deactivate the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to deactivate the participants from. If no role found,
 RelationshipUserException will be thrown.dataString - data of the participants to be deactivated. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deactivateParticipantLong
void deactivateParticipantLong(java.lang.String relationshipName,
                             java.lang.String roleName,
                             long dataSimpleType)
                               throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                      com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deactivates all the participants of this relationship that match this
 data for the participant. This role contains a roleObject of long type
 and a keyAttribute whose path is defined as "Data". Value for this role
 is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deactivateParticipantLong("http://www.ibm.com/StaticRel", "http://www.ibm.com/longRole", -9223372036854775808);

Parameters:relationshipName - name of the relationship to deactivate the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to deactivate the participants from. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participants to be deactivated. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deactivateParticipantInt
void deactivateParticipantInt(java.lang.String relationshipName,
                            java.lang.String roleName,
                            int dataSimpleType)
                              throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                     com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deactivates all the participants of this relationship that match this
 data for the participant. This role contains a roleObject of int type
 and a keyAttribute whose path is defined as "Data". Value for this role
 is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deactivateParticipantInt("http://www.ibm.com/StaticRel", "http://www.ibm.com/intRole", -2147483648);

Parameters:relationshipName - name of the relationship to deactivate the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to deactivate the participants from. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participants to be deactivated. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deactivateParticipantFloat
void deactivateParticipantFloat(java.lang.String relationshipName,
                              java.lang.String roleName,
                              float dataSimpleType)
                                throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                       com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deactivates all the participants of this relationship that match this
 data for the participant. This role contains a roleObject of float type
 and a keyAttribute whose path is defined as "Data". Value for this role
 is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deactivateParticipantFloat("http://www.ibm.com/StaticRel", "http://www.ibm.com/floatRole", 1.40129846432481707e-45F);

Parameters:relationshipName - name of the relationship to deactivate the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to deactivate the participants from. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participants to be deactivated. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deactivateParticipantDouble
void deactivateParticipantDouble(java.lang.String relationshipName,
                               java.lang.String roleName,
                               double dataSimpleType)
                                 throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                        com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deactivates all the participants of this relationship that match this
 data for the participant. This role contains a roleObject of double type
 and a keyAttribute whose path is defined as "Data". Value for this role
 is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deactivateParticipantDouble("http://www.ibm.com/StaticRel", "http://www.ibm.com/doubleRole", 4.94065645841246544e-324D);

Parameters:relationshipName - name of the relationship to deactivate the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to deactivate the participants from. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participants to be deactivated. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deactivateParticipantBoolean
void deactivateParticipantBoolean(java.lang.String relationshipName,
                                java.lang.String roleName,
                                boolean dataSimpleType)
                                  throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                         com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deactivates all the participants of this relationship that match this
 data for the participant. This role contains a roleObject of boolean type
 and a keyAttribute whose path is defined as "Data". Value for this role
 is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deactivateParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

Parameters:relationshipName - name of the relationship to deactivate the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to deactivate the participants from. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participants to be deactivated. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deactivateParticipantStringByID
void deactivateParticipantStringByID(java.lang.String relationshipName,
                                   java.lang.String roleName,
                                   int instanceID,
                                   java.lang.String dataString)
                                     throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                            com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deactivates all the participant instances of the relationship that match
 this data for the participant and have the specified relationship
 instanceID. This role contains a roleObject of String type and a
 keyAttribute whose path is defined as "Data". Value for this role is
 specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.createParticipantString("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "value\_String");

 relService.deactivateParticipantStingByID("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", id, "value\_String");

Parameters:relationshipName - name of the relationship to deactivate the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to deactivate the participants from. If no role found,
 RelationshipUserException will be thrown.dataString - data of the participants to be deactivated. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deactivateParticipantLongByID
void deactivateParticipantLongByID(java.lang.String relationshipName,
                                 java.lang.String roleName,
                                 int instanceID,
                                 long dataSimpleType)
                                   throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                          com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deactivates all the participant instances of the relationship that match
 this data for the participant and have the specified relationship
 instanceID. This role contains a roleObject of long type and a
 keyAttribute whose path is defined as "Data". Value for this role is
 specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.createParticipantLong("http://www.ibm.com/StaticRel", "http://www.ibm.com/longRole", -9223372036854775808);

 relService.deactivateParticipantLongByID("http://www.ibm.com/StaticRel", "http://www.ibm.com/longRole", id, -9223372036854775808);

Parameters:relationshipName - name of the relationship to deactivate the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to deactivate the participants from. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participants to be deactivated. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deactivateParticipantIntByID
void deactivateParticipantIntByID(java.lang.String relationshipName,
                                java.lang.String roleName,
                                int instanceID,
                                int dataSimpleType)
                                  throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                         com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deactivates all the participant instances of the relationship that match
 this data for the participant and have the specified relationship
 instanceID. This role contains a roleObject of int type and a
 keyAttribute whose path is defined as "Data". Value for this role is
 specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.addParticipantInt("http://www.ibm.com/StaticRel", "http://www.ibm.com/intRole", -2147483648);

 relService.deactivateParticipantIntByID("http://www.ibm.com/StaticRel", "http://www.ibm.com/intRole", id, -2147483648);

Parameters:relationshipName - name of the relationship to deactivate the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to deactivate the participants from. If no role found,
 RelationshipUserException will be thrown.instanceID - specified relationship instanceIDdataSimpleType - data of the participants to be deactivated. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deactivateParticipantFloatByID
void deactivateParticipantFloatByID(java.lang.String relationshipName,
                                  java.lang.String roleName,
                                  int instanceID,
                                  float dataSimpleType)
                                    throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                           com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deactivates all the participant instances of the relationship that match
 this data for the participant and have the specified relationship
 instanceID. This role contains a roleObject of float type and a
 keyAttribute whose path is defined as "Data". Value for this role is
 specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.addParticipantFloat("http://www.ibm.com/StaticRel", "http://www.ibm.com/floatRole", -3.40282346638528860e+38F);

 relService.deactivateParticipantFloatByID("http://www.ibm.com/StaticRel", "http://www.ibm.com/floatRole", id, -3.40282346638528860e+38F);

Parameters:relationshipName - name of the relationship to deactivate the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to deactivate the participants from. If no role found,
 RelationshipUserException will be thrown.instanceID - specified relationship instanceIDdataSimpleType - data of the participants to be deactivated. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deactivateParticipantDoubleByID
void deactivateParticipantDoubleByID(java.lang.String relationshipName,
                                   java.lang.String roleName,
                                   int instanceID,
                                   double dataSimpleType)
                                     throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                            com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deactivates all the participant instances of the relationship that match
 this data for the participant and have the specified relationship
 instanceID. This role contains a roleObject of double type and a
 keyAttribute whose path is defined as "Data". Value for this role is
 specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.createParticipantDouble("http://www.ibm.com/StaticRel", "http://www.ibm.com/doubleRole", 4.94065645841246544e-324D);

 relService.deactivateParticipantDoubleByID("http://www.ibm.com/StaticRel", "http://www.ibm.com/doubleRole", id, 4.94065645841246544e-324D);

Parameters:relationshipName - name of the relationship to deactivate the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to deactivate the participants from. If no role found,
 RelationshipUserException will be thrown.instanceID - specified relationship instanceIDdataSimpleType - data of the participants to be deactivated. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deactivateParticipantBooleanByID
void deactivateParticipantBooleanByID(java.lang.String relationshipName,
                                    java.lang.String roleName,
                                    int instanceID,
                                    boolean dataSimpleType)
                                      throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                             com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deactivates all the participant instances of the relationship that match
 this data for the participant and have the specified relationship
 instanceID. This role contains a roleObject of boolean type and a
 keyAttribute whose path is defined as "Data". Value for this role is
 specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.createParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

 relService.deactivateParticipantBooleanByID("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", id, true);

Parameters:relationshipName - name of the relationship to deactivate the participants from. If no
 relationship found, RelationshipUserException will be thrown.roleName - name of the role to deactivate the participants from. If no role found,
 RelationshipUserException will be thrown.instanceID - specified relationship instanceID. InstanceID equal with or less than
 zero is not valid.dataSimpleType - data of the participants to be deactivated. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsUseDeactivate
int[] retrieveInstanceIDsUseDeactivate(java.lang.String relationshipName,
                                     java.lang.String roleName,
                                     java.lang.String dataString)
                                       throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                              com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of relationship instances that match this relationship
 name, role name and data. Deactivated instances are also considered.
 This role contains a roleObject of String type and a keyAttribute whose
 path is defined as "Data". This API supports static rleationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.createParticipantString("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "value\_String");

 relService.deactivateParticipantStringByID("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", id, "value\_String");

 int[] idArray = relService.retrieveInstanceIDsUseDeactivate("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "value\_String");

Parameters:relationshipName - name of the relationship to retrieve instanceIDs from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role for retrieve. If no role found,
 RelationshipUserException will be thrown.dataString - data of the participants to be retrieved
Returns:int array of ids of the matched instance ids. If no matched instance
 found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipantString
void deleteParticipantString(java.lang.String relationshipName,
                           java.lang.String roleName,
                           java.lang.String dataString)
                             throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                    com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants of this relationship that match this role
 and the specified data. This role contains a roleObject of String type
 and a keyAttribute whose path is defined as "Data". Value for this role
 is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deleteParticipantString("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "value\_String");

Parameters:relationshipName - name of the relationship to delete the participants from. If no
 relationship found, RelationshipUserException will be
 thrown.roleName - name of the role to delete the participants from. If no role found,
 RelationshipUserException will be thrown.dataString - data of the participants to be deleted. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipantLong
void deleteParticipantLong(java.lang.String relationshipName,
                         java.lang.String roleName,
                         long dataSimpleType)
                           throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                  com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants of this relationship that match this role
 and the specified data. This role contains a roleObject of long type
 and a keyAttribute whose path is defined as "Data". Value for this role
 is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deleteParticipantLong("http://www.ibm.com/StaticRel", "http://www.ibm.com/longRole",  -9223372036854775808);

Parameters:relationshipName - name of the relationship to delete the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to delete the participants from. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participants to be deleted. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipantInt
void deleteParticipantInt(java.lang.String relationshipName,
                        java.lang.String roleName,
                        int dataSimpleType)
                          throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                 com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants of this relationship that match this role
 and the specified data. This role contains a roleObject of int type
 and a keyAttribute whose path is defined as "Data". Value for this role
 is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deleteParticipantInt("http://www.ibm.com/StaticRel", "http://www.ibm.com/intRole", -2147483648);

Parameters:relationshipName - name of the relationship to delete the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to delete the participants from. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participants to be deleted. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipantFloat
void deleteParticipantFloat(java.lang.String relationshipName,
                          java.lang.String roleName,
                          float dataSimpleType)
                            throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                   com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants of this relationship that match this role
 and the specified data. This role contains a roleObject of float type
 and a keyAttribute whose path is defined as "Data". Value for this role
 is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deleteParticipantFloat("http://www.ibm.com/StaticRel", "http://www.ibm.com/floatRole", 1.40129846432481707e-45F);

Parameters:relationshipName - name of the relationship to delete the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to delete the participants from. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participants to be deleted. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipantDouble
void deleteParticipantDouble(java.lang.String relationshipName,
                           java.lang.String roleName,
                           double dataSimpleType)
                             throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                    com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants of this relationship that match this role
 and the specified data. This role contains a roleObject of double type
 and a keyAttribute whose path is defined as "Data". Value for this role
 is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deleteParticipantDouble("http://www.ibm.com/StaticRel", "http://www.ibm.com/doubleRole", 4.94065645841246544e-324D);

Parameters:relationshipName - name of the relationship to delete the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to delete the participants from. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participants to be deleted. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipantBoolean
void deleteParticipantBoolean(java.lang.String relationshipName,
                            java.lang.String roleName,
                            boolean dataSimpleType)
                              throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                     com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants of this relationship that match this role
 and the specified data. This role contains a roleObject of boolean type
 and a keyAttribute whose path is defined as "Data". Value for this role
 is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deleteParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

Parameters:relationshipName - name of the relationship to delete the participants from. If no relationship
 found, RelationshipUserException will be thrown.roleName - name of the role to delete the participants from. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the participants to be deleted. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipantStringByID
void deleteParticipantStringByID(java.lang.String relationshipName,
                               java.lang.String roleName,
                               int instanceID,
                               java.lang.String dataString)
                                 throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                        com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants that match this relationship name, role name,
 relationship instanceID and the data. This role contains a roleObject of
 String type and a keyAttribute whose path is defined as "Data". Value for
 this role is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.createParticipantString("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "value\_String");

 relService.deleteParticipantStringByID("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", id, "value\_String");

Parameters:relationshipName - name of the relationship to delete the participants from. If no
 relationship found, RelationshipUserException will be
 thrown.roleName - name of the role to delete the partcipants from. If no role found,
 RelationshipUserException will be thrown.instanceID - given relationship instanceIDdataString - data of the participants to be deleted. If no matched participant found,
 no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipantLongByID
void deleteParticipantLongByID(java.lang.String relationshipName,
                             java.lang.String roleName,
                             int instanceID,
                             long dataSimpleType)
                               throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                      com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants that match the relationship name, role name,
 relationship instanceID and the data. This role contains a roleObject of
 long type and a keyAttribute whose path is defined as "Data". Value for
 this role is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.createParticipantLong("http://www.ibm.com/StaticRel", "http://www.ibm.com/longRole", -9223372036854775808);

 relService.deleteParticipantLongByID("http://www.ibm.com/StaticRel", "http://www.ibm.com/longRole", id, -9223372036854775808);

Parameters:relationshipName - name of the relationship to delete the participants from. If no
 relationship found, RelationshipUserException will be
 thrown.roleName - name of the role to delete the partcipants from. If no role found,
 RelationshipUserException will be thrown.instanceID - given relationship instanceIDdataSimpleType - data of the participants to be deleted. If no matched participant
 found, no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipantIntByID
void deleteParticipantIntByID(java.lang.String relationshipName,
                            java.lang.String roleName,
                            int instanceID,
                            int dataSimpleType)
                              throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                     com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants that match the relationship name, role name,
 relationship instanceID and the data. This role contains a roleObject of
 int type and a keyAttribute whose path is defined as "Data". Value for
 this role is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.addParticipantInt("http://www.ibm.com/StaticRel", "http://www.ibm.com/intRole", -2147483648);

 relService.deleteParticipantIntByID("http://www.ibm.com/StaticRel", "http://www.ibm.com/intRole", id, -2147483648);

Parameters:relationshipName - name of the relationship to delete the participants from. If no
 relationship found, RelationshipUserException will be
 thrown.roleName - name of the role to delete the partcipants from. If no role found,
 RelationshipUserException will be thrown.instanceID - given relationship instanceIDdataSimpleType - data of the participants to be deleted. If no matched participant
 found, no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipantFloatByID
void deleteParticipantFloatByID(java.lang.String relationshipName,
                              java.lang.String roleName,
                              int instanceID,
                              float dataSimpleType)
                                throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                       com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants that match the relationship name, role name,
 relationship instanceID and the data. This role contains a roleObject of
 float type and a keyAttribute whose path is defined as "Data". Value for
 this role is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.addParticipantFloat("http://www.ibm.com/StaticRel", "http://www.ibm.com/floatRole", -3.40282346638528860e+38F);

 relService.deleteParticipantFloatByID("http://www.ibm.com/StaticRel", "http://www.ibm.com/floatRole", id, -3.40282346638528860e+38F);

Parameters:relationshipName - name of the relationship to delete the participants from. If no
 relationship found, RelationshipUserException will be
 thrown.roleName - name of the role to delete the partcipants from. If no role found,
 RelationshipUserException will be thrown.instanceID - given relationship instanceIDdataSimpleType - data of the participants to be deleted. If no matched participant
 found, no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipantDoubleByID
void deleteParticipantDoubleByID(java.lang.String relationshipName,
                               java.lang.String roleName,
                               int instanceID,
                               double dataSimpleType)
                                 throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                        com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants that match the relationship name, role name,
 relationship instanceID and the data. This role contains a roleObject of
 double type and a keyAttribute whose path is defined as "Data". Value for
 this role is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.createParticipantDouble("http://www.ibm.com/StaticRel", "http://www.ibm.com/doubleRole", 4.94065645841246544e-324D);

 relService.deleteParticipantDoubleByID("http://www.ibm.com/StaticRel", "http://www.ibm.com/doubleRole", id, 4.94065645841246544e-324D);

Parameters:relationshipName - name of the relationship to delete the participants from. If no
 relationship found, RelationshipUserException will be
 thrown.roleName - name of the role to delete the partcipants from. If no role found,
 RelationshipUserException will be thrown.instanceID - given relationship instanceIDdataSimpleType - data of the participants to be deleted. If no matched participant
 found, no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipantBooleanByID
void deleteParticipantBooleanByID(java.lang.String relationshipName,
                                java.lang.String roleName,
                                int instanceID,
                                boolean dataSimpleType)
                                  throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                         com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants that match this relationship name, role name,
 relationship instanceID and the data. This role contains a roleObject of
 boolean type and a keyAttribute whose path is defined as "Data". Value for
 this role is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.createParticipantBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

 relService.deleteParticipantBooleanByID("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", id, true);

Parameters:relationshipName - name of the relationship to delete the participants from. If no
 relationship found, RelationshipUserException will be
 thrown.roleName - name of the role to delete the partcipants from. If no role found,
 RelationshipUserException will be thrown.instanceID - given relationship instanceIDdataSimpleType - data of the participants to be deleted. If no matched participant
 found, no exception will be thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByString
int[] retrieveInstanceIDsByString(java.lang.String relationshipName,
                                java.lang.String roleName,
                                java.lang.String dataString)
                                  throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                         com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of all the participants that match this relationship,
 role and data. This role contains a roleObject of String type and a
 keyAttribute whose path is defined as "Data". Value for this role is
 specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int[] ids = relService.retrieveInstanceIDsByString("http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "value\_String");

Parameters:relationshipName - name of the specified relationship. If no relationship found,
 RelationshipUserException will be thrown.roleName - name of the specified role. If no role found,
  RelationshipUserException will be thrown.dataString - data of the target participants
Returns:int array of ids of all the matched participants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByLong
int[] retrieveInstanceIDsByLong(java.lang.String relationshipName,
                              java.lang.String roleName,
                              long dataSimpleType)
                                throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                       com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of all the participants that match this relationship,
 role and data. This role contains a roleObject of long type and a
 keyAttribute whose path is defined as "Data". Value for this role is
 specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int[] ids = relService.retrieveInstanceIDsByLong("http://www.ibm.com/StaticRel", "http://www.ibm.com/longRole", -9223372036854775808);

Parameters:relationshipName - name of the specified relationship. If no relationship found,
 RelationshipUserException will be thrown.roleName - name of the specified role. If no role found,
  RelationshipUserException will be thrown.dataSimpleType - data of the target participants
Returns:int array of ids of all the matched participants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByInt
int[] retrieveInstanceIDsByInt(java.lang.String relationshipName,
                             java.lang.String roleName,
                             int dataSimpleType)
                               throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                      com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of all the participants that match this relationship,
 role and data. This role contains a roleObject of int type and a
 keyAttribute whose path is defined as "Data". Value for this role is
 specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int[] ids = relService.retrieveInstanceIDsByInt("http://www.ibm.com/StaticRel", "http://www.ibm.com/intRole", -2147483648);

Parameters:relationshipName - name of the specified relationship. If no relationship found,
 RelationshipUserException will be thrown.roleName - name of the specified role. If no role found,
  RelationshipUserException will be thrown.dataSimpleType - data of the target participants
Returns:int array of ids of all the matched participants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByFloat
int[] retrieveInstanceIDsByFloat(java.lang.String relationshipName,
                               java.lang.String roleName,
                               float dataSimpleType)
                                 throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                        com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of all the participants that match this relationship,
 role and data. This role contains a roleObject of float type and a
 keyAttribute whose path is defined as "Data". Value for this role is
 specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int[] ids = relService.retrieveInstanceIDsByFloat("http://www.ibm.com/StaticRel", "http://www.ibm.com/floatRole", 1.40129846432481707e-45F);

Parameters:relationshipName - name of the specified relationship. If no relationship found,
 RelationshipUserException will be thrown.roleName - name of the specified role. If no role found,
  RelationshipUserException will be thrown.dataSimpleType - data of the target participants
Returns:int array of ids of all the matched participants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByDouble
int[] retrieveInstanceIDsByDouble(java.lang.String relationshipName,
                                java.lang.String roleName,
                                double dataSimpleType)
                                  throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                         com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of all the participants that match this relationship,
 role and data. This role contains a roleObject of double type and a
 keyAttribute whose path is defined as "Data". Value for this role is
 specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int[] ids = relService.retrieveInstanceIDsByDouble("http://www.ibm.com/StaticRel", "http://www.ibm.com/doubleRole", 4.94065645841246544e-324D);

Parameters:relationshipName - name of the specified relationship. If no relationship found,
 RelationshipUserException will be thrown.roleName - name of the specified role. If no role found,
  RelationshipUserException will be thrown.dataSimpleType - data of the target participants
Returns:int array of ids of all the matched participants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByBoolean
int[] retrieveInstanceIDsByBoolean(java.lang.String relationshipName,
                                 java.lang.String roleName,
                                 boolean dataSimpleType)
                                   throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                          com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of all the participants that match this relationship,
 role and data. This role contains a roleObject of boolean type and a
 keyAttribute whose path is defined as "Data". Value for this role is
 specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int[] ids = relService.retrieveInstanceIDsByBoolean("http://www.ibm.com/StaticRel", "http://www.ibm.com/booleanRole", true);

Parameters:relationshipName - name of the specified relationship. If no relationship found,
 RelationshipUserException will be thrown.roleName - name of the specified role. If no role found,
  RelationshipUserException will be thrown.dataSimpleType - data of the target participants
Returns:int array of ids of all the matched participants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByRoleNameString
int[] retrieveInstanceIDsByRoleNameString(java.lang.String relationshipName,
                                        java.lang.String[] roleName,
                                        java.lang.String dataString)
                                          throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                                 com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of the participants that match this relationship name,
 the list of role names and the specified data. Each role contains a
 roleObject of String type and a keyAttribute whose path is defined as
 "Data". Value for these roles is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 String[] roleNames = {"http://www.ibm.com/StringRole\_First", "http://www.ibm.com/StringRole\_Second"};

 int[] ids = relService.retrieveInstanceIDsByRoleNameString("http://www.ibm.com/StaticRel", roleNames, "value\_String");

Parameters:relationshipName - name of the specified relationship. If no relationship found,
 RelationshipUserException will be thrown.roleName - list of the specified role names. If no role found,
 RelationshipUserException will be thrown.dataString - data of the target participants
Returns:int array of ids of all the matched participants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByRoleNameLong
int[] retrieveInstanceIDsByRoleNameLong(java.lang.String relationshipName,
                                      java.lang.String[] roleName,
                                      long dataSimpleType)
                                        throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                               com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of the participants that match the relationship name,
 the list of role names and the specified data. Each role contains a
 roleObject of long type and a keyAttribute whose path is defined as
 "Data". Value for these roles is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 String[] roleNames = {"http://www.ibm.com/longRole\_First", "http://www.ibm.com/longRole\_Second"};

 int[] ids = relService.retrieveInstanceIDsByRoleNameLong("http://www.ibm.com/StaticRel", roleNames, -9223372036854775808);

Parameters:relationshipName - name of the specified relationship. If no relationship found,
 RelationshipUserException will be thrown.roleName - list of the specified role names. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the target participants
Returns:list of ids of all the matched participants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByRoleNameInt
int[] retrieveInstanceIDsByRoleNameInt(java.lang.String relationshipName,
                                     java.lang.String[] roleName,
                                     int dataSimpleType)
                                       throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                              com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of the participants that match the relationship name,
 the list of role names and the specified data. Each role contains a
 roleObject of int type and a keyAttribute whose path is defined as
 "Data". Value for these roles is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 String[] roleNames = {"http://www.ibm.com/intRole\_First", "http://www.ibm.com/intRole\_Second"};

 int[] ids = relService.retrieveInstanceIDsByRoleNameInt("http://www.ibm.com/StaticRel", roleNames, -2147483648);

Parameters:relationshipName - name of the specified relationship. If no relationship found,
 RelationshipUserException will be thrown.roleName - list of the specified role names. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the target participants
Returns:list of ids of all the matched participants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByRoleNameFloat
int[] retrieveInstanceIDsByRoleNameFloat(java.lang.String relationshipName,
                                       java.lang.String[] roleName,
                                       float dataSimpleType)
                                         throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                                com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of the participants that match the relationship name,
 the list of role names and the specified data. Each role contains a
 roleObject of float type and a keyAttribute whose path is defined as
 "Data". Value for these roles is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 String[] roleNames = {"http://www.ibm.com/floatRole\_First", "http://www.ibm.com/floatRole\_Second"};

 int[] ids = relService.retrieveInstanceIDsByRoleNameFloat("http://www.ibm.com/StaticRel", roleNames, 1.40129846432481707e-45F);

Parameters:relationshipName - name of the specified relationship. If no relationship found,
 RelationshipUserException will be thrown.roleName - list of the specified role names. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the target participants
Returns:list of ids of all the matched participants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByRoleNameDouble
int[] retrieveInstanceIDsByRoleNameDouble(java.lang.String relationshipName,
                                        java.lang.String[] roleName,
                                        double dataSimpleType)
                                          throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                                 com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of the participants that match the relationship name,
 the list of role names and the specified data. Each role contains a
 roleObject of double type and a keyAttribute whose path is defined as
 "Data". Value for these roles is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 String[] roleNames = {"http://www.ibm.com/doubleRole\_First", "http://www.ibm.com/doubleRole\_Second"};

 int[] ids = relService.retrieveInstanceIDsByRoleNameDouble("http://www.ibm.com/StaticRel", roleNames, 4.94065645841246544e-324D);

Parameters:relationshipName - name of the specified relationship. If no relationship found,
 RelationshipUserException will be thrown.roleName - list of the specified role names. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the target participants
Returns:list of ids of all the matched participants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByRoleNameBoolean
int[] retrieveInstanceIDsByRoleNameBoolean(java.lang.String relationshipName,
                                         java.lang.String[] roleName,
                                         boolean dataSimpleType)
                                           throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                                  com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of the participants that match the relationship name,
 the list of role names and the specified data. Each role contains a
 roleObject of boolean type and a keyAttribute whose path is defined as
 "Data". Value for these roles is specified by the data. This API supports
 static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 String[] roleNames = {"http://www.ibm.com/booleanRole\_First", "http://www.ibm.com/booleanRole\_Second"};

 int[] ids = relService.retrieveInstanceIDsByRoleNameBoolean("http://www.ibm.com/StaticRel", roleNames, true);

Parameters:relationshipName - name of the specified relationship. If no relationship found,
 RelationshipUserException will be thrown.roleName - list of the specified role names. If no role found,
 RelationshipUserException will be thrown.dataSimpleType - data of the target participants
Returns:list of ids of all the matched participants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByRelNameString
int[] retrieveInstanceIDsByRelNameString(java.lang.String relationshipName,
                                       java.lang.String dataString)
                                         throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                                com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of the participants that match this relationship name and
 data. It looks up all the roles that contains a  roleObject of
 String type and a keyAttribute whose path is defined as "Data". Value
 for these roles is specified by the data. This API supports static relationship
 only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int[] ids = relService.retrieveInstanceIDsByRelNameString("http://www.ibm.com/StaticRel", "value\_String");

Parameters:relationshipName - name of the spcified relationship. If no relationship found,
 RelationshipUserException will be thrown.dataString - data of the target partcipants
Returns:list of ids of all the matched partcipants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByRelNameLong
int[] retrieveInstanceIDsByRelNameLong(java.lang.String relationshipName,
                                     long dataSimpleType)
                                       throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                              com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of the participants that match this relationship name and
 data. It looks up all the roles that contains a roleObject of long type
 and a keyAttribute whose path is defined as "Data". Value for these
 roles is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int[] ids = relService.retrieveInstanceIDsByRelNameLong("http://www.ibm.com/StaticRel", -9223372036854775808);

Parameters:relationshipName - name of the spcified relationship. If no relationship found,
 RelationshipUserException will be thrown.dataSimpleType - data of the target partcipants
Returns:list of ids of all the matched partcipants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByRelNameInt
int[] retrieveInstanceIDsByRelNameInt(java.lang.String relationshipName,
                                    int dataSimpleType)
                                      throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                             com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of the participants that match this relationship name and
 data. It looks up all the roles that contains a roleObject of int type
 and a keyAttribute whose path is defined as "Data". Value for these
 roles is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int[] ids = relService.retrieveInstanceIDsByRelNameInt("http://www.ibm.com/StaticRel", -2147483648);

Parameters:relationshipName - name of the spcified relationship. If no relationship found,
 RelationshipUserException will be thrown.dataSimpleType - data of the target partcipants
Returns:list of ids of all the matched partcipants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByRelNameFloat
int[] retrieveInstanceIDsByRelNameFloat(java.lang.String relationshipName,
                                      float dataSimpleType)
                                        throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                               com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of the participants that match this relationship name and
 data. It looks up all the roles that contains a roleObject of float type
 and a keyAttribute whose path is defined as "Data". Value for these
 roles is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int[] ids = relService.retrieveInstanceIDsByRelNameFloat("http://www.ibm.com/StaticRel", -3.40282346638528860e+38F);

Parameters:relationshipName - name of the spcified relationship. If no relationship found,
 RelationshipUserException will be thrown.dataSimpleType - data of the target partcipants
Returns:list of ids of all the matched partcipants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByRelNameDouble
int[] retrieveInstanceIDsByRelNameDouble(java.lang.String relationshipName,
                                       double dataSimpleType)
                                         throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                                com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of the participants that match this relationship name and
 data. It looks up all the roles that contains a roleObject of double type
 and a keyAttribute whose path is defined as "Data". Value for these
 roles is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int[] ids = relService.retrieveInstanceIDsByRelNameDouble("http://www.ibm.com/StaticRel", 4.94065645841246544e-324D);

Parameters:relationshipName - name of the spcified relationship. If no relationship found,
 RelationshipUserException will be thrown.dataSimpleType - data of the target partcipants
Returns:list of ids of all the matched partcipants. If no matched
 participant found, an empty int array is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveInstanceIDsByRelNameBoolean
int[] retrieveInstanceIDsByRelNameBoolean(java.lang.String relationshipName,
                                        boolean dataSimpleType)
                                          throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                                 com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves ids of the participants that match this relationship name and
 data. It looks up all the roles that contains a roleObject of boolean type
 and a keyAttribute whose path is defined as "Data". Value for these
 roles is specified by the data. This API supports static relationship only.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int[] ids = relService.retrieveInstanceIDsByRelNameBoolean("http://www.ibm.com/StaticRel", true);

Parameters:relationshipName - name of the spcified relationship. If no relationship found,
 RelationshipUserException will be thrown.dataSimpleType - data of the target partcipants
Returns:list of ids of all the matched partcipants. If no matched
 participant found, an empty list is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveParticipantsByRoleName
java.util.List retrieveParticipantsByRoleName(java.lang.String relationshipName,
                                            java.lang.String[] roleNames,
                                            int instanceID)
                                              throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                                     com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves all the participants from this relationship and the list of ASBO
 roles. The matched participants own the specified instanceID. It
 can be used for static as well as dynamic relationship.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 String roleNames = {"http://www.ibm.com/StringRole", "http://www.ibm.com/longRole"};

 List participants = relService.retrieveParticipantsByRoleName("http://www.ibm.com/StaticRel", roleNames, 1);

Parameters:relationshipName - name of the relationship to retrieve the participants from. If no
 relationship found, RelationshipUserException is
 thrown.roleNames - list of role names. If any role in the list could not be found,
 RelationshipUserException is thrown.instanceID - specified relationship instanceID
Returns:list of all the matced partcipants. If no matched participant found,
 an empty list is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- retrieveParticipantsByRelationshipName
java.util.List retrieveParticipantsByRelationshipName(java.lang.String relationshipName,
                                                    int instanceID)
                                                      throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                                             com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Retrieves all the matched participants from all the ASBO roles of this
 relationship. The matched participants own the given relationship
 instanceID. It can be used for static as well as dynamic relationship.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 List participants = relService.retrieveParticipantsByRelationshipName("http://www.ibm.com/StaticRel", 1);

Parameters:relationshipName - name of the relationship to retrieve participants from. If no
 relationship found, RelationshipUserException is
 thrown.instanceID - given relationship instanceID
Returns:list of all the matched participants. If no matched participant found,
 an empty list is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- maintainIdentityRelationship void maintainIdentityRelationship(java.lang.String relationshipName, java.lang.String appRoleName, commonj.sdo.DataObject inputBO, commonj.sdo.DataObject outputBO, commonj.sdo.DataObject originalInputBO, commonj.sdo.DataObject originalOutputBO, java.lang.String callingContext) throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException, com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException, com.ibm.wbiserver.relationshipservice.exceptions.MissingIdException Deprecated. since WPS6.1 use correlate to maintain relationships and correlateToList and correlateFromList to maintain containment relatoinships Maintains an identity relationship, this could be used for both simple and composite relationship. Before using this API, please ensure follwoing items are true: Five usage scenarioes are listed below. Parameters: relationshipName - name of the identity relationship to maintain appRoleName - name of the ASBO role inputBO - input BO, it could also be a BG. outputBO - output BO, it could also be a BG. originalInputBO - original input BO, it could also be a BG. originalOutputBO - original output BO, it could also be a BG. callingContext - calling context including SERVICE\_CALL\_REQUEST, SERVICE\_CALL\_RESPONSE, EVENT\_DELIVERY and SERVICE\_CALL\_FAILURE Throws: com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException com.ibm.wbiserver.relationshipservice.exceptions.MissingIdException Since: WPS6.0 In WPS6.0, the need for parent-children relationships in composite relationship maintenance, will be done away with with the new maintainIdentityRelationship API. That is:

#### maintainIdentityRelationship

```
void maintainIdentityRelationship(java.lang.String relationshipName,
                                java.lang.String appRoleName,
                                commonj.sdo.DataObject inputBO,
                                commonj.sdo.DataObject outputBO,
                                commonj.sdo.DataObject originalInputBO,
                                commonj.sdo.DataObject originalOutputBO,
                                java.lang.String callingContext)
                                  throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                         com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException,
                                         com.ibm.wbiserver.relationshipservice.exceptions.MissingIdException
```

    - An 'identity' relationship is involved (e.g. the 'isIdentity'
 attribute on the relationship descriptor is set to TRUE).
    The identity relationship has at least 1 role marked as 'managed'
 (role descriptor 'managed' attribute is set to TRUE).
    Each maintainIdentityRelationship invocation involves one
 business object participating in a 'managed' role and the other business
 object participating in an unmanaged role.
    - In the calling context SERVICE\_CALL\_REQUEST,
 the inputBO is an ASBO and the outputBO is a GBO. The inputBO is an
 instance of the ASBO role specified by the param appRoleName.

 

Verb/ChangeSummary on the inputBO
Existing entry found in table
Entry not found in table
Exceptions

Create,
 Update
Gets the instance id and inserts into the GBO id. If a row with
 given role key id exists, but is deactivated, then creates a new row with
 the given role key id and a new instanceId.
A new row will be created in the role table with a unique
 instanceId and the value of role key Id obtained from the ASBO DataObject.
 This InstanceId is then inserted into the GBO id.
If the key in the ASBO is null, RelationshipUserException
 will be thrown.

Delete
Gets the instance Id and inserts in the GBO.
Throws MissingIdException
If the key in the ASBO is null, RelationshipUserException
 will be thrown.

UpdateWithDelete
Figures out if the verb is create, update or deleted and applies
 the above behavior

If the key in the ASBO is null, RelationshipUserException
 will be thrown.

All other verbs
Gets the instance Id and inserts in the GBO.
Throws MissingIdException
If the key in the ASBO is null, RelationshipUserException
 will be thrown.

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relSerive.maintainIdentityRelationship("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", sapCustomer, genBO,
                        null, null, SERVICE\_CALL\_REQUEST);

 In the calling context EVENT\_DELIVERY,
 the inputBO is an ASBO and the outputBO is a GBO. The inputBO is an
 instance of the ASBO role specified by the param appRoleName.

 

Verb/ChangeSummary on the inputBO
Existing entry found in table
Entry not found in table
Exceptions

Create
Gets the instance id and inserts into the GBO id. If a row with
 given role key id exists, but is deactivated, then creates a new row with
 the given role key id and a new instanceId.
A new row will be created in the role table with a unique
 instanceId and the value of role key Id obtained from the ASBO DataObject.
 This InstanceId is then inserted into the GBO id.
If the key in the ASBO is null, RelationshipUserException
 will be thrown.

Delete
Gets the instance id and inserts into the GBO id.
Message is logged indicating that the participant has
 already been deleted.
If the key in the ASBO is null, RelationshipUserException
 will be thrown.

Update
Uses that Id for the GBO. If a row with given role key id
 exists, but is deactivated, then creates a new row with the given
 role key id and a new instanceId.
A new row will be created in the table with a unique
 instanceId and the value of role key id obtained from the ASBO
 DataObject. This InstanceId is then inserted into the GBO id.
If the key in the ASBO is null, RelationshipUserException
 will be thrown.

UpdateWithDelete
Depending on whether it is Create, Update or Delete,
 it will behave like one.
Depending on whether it is Create, Update or Delete,
 it will behave like one.

All other verbs
The instance id corresponding to that row is inserted into
 the GBO id.
Creates a new row in the table and inserts the instance id into
 the GBO id.
If the key in the ASBO is null, RelationshipUserException
 will be thrown.

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relSerive.maintainIdentityRelationship("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", sapCustomer, genBO,
                        null, null, EVENT\_DELIVERY);

 In the calling context SERVICE\_CALL\_REQUEST/EVENT\_DELIVERY,
 the inputBO is a GBO and the outputBO is an ASBO. The outputBO is an
 instance of the ASBO role specified by the param appRoleName.

 

Verb/ChangeSummary on the inputBO
Existing entry found in table
Entry not found in table

Create
No action is taken. The table remains as is.
No action is taken. The table remains as is.

Update
The ASBO key corresponding to that row is inserted into the ASBO id.
MissingIdException is thrown

Delete
The row is deactivated and the role key id is inserted into the ASBO id.
MissingIdException is thrown

UpdateWithDelete
Depending on whether it is Create, Update or Delete,
 it will behave like one.
Depending on whether it is Create, Update or Delete,
 it will behave like one.

All other verbs
The ASBO key corresponding to that row is inserted into the ASBO id.
MissingIdException is thrown

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relSerive.maintainIdentityRelationship("http://www.ibm.com/CustomerRel", "http://www.clarify.com/ClarifyRole", genBO, clarifyCustomer,
                        null, null, EVENT\_DELIVERY);

 In the calling context SERVICE\_CALL\_RESPONSE,
 the inputBO is an ASBO and the outputBO is a GBO. The inputBO is an
 instance of the ASBO role specified by the param appRoleName.

 

Verb/ChangeSummary on the inputBO
Existing entry found in table
Entry not found in table
Exceptions

Create
The instance id corresponding to that row will be inserted in
 the GBO id.
A new row will be created in the role table with the given
 role key id with the InstanceId set to the same value as in the origGBO
 id. This InstanceId is then inserted into the new GBO id. If the origGBO
 does not exist, then a new entry will be created and an instance id will
 be generated as oppose to the one that is obtained from the origGbo.
 Also, an error will be logged that the origGBO is null.

Update
The instance id corresponding to that row is inserted into
 the GBO id.
A new row will be created in the role table with the given role
 key id and with the InstanceId set to the same value as in the origGBO id.
 This InstanceId is then inserted into the new GBO id. If the origGBO does
 not exist, then a new entry will be created and an instance id will be
 generated as oppose to the one that is obtained from the origGbo. Also,
 an error will be logged that the origGBO is null.

Delete 
In the case of delete, the incoming object is really no good
 because all the contained objects from there have been deleted. We need
 to look at the origASBO. The row is deactivated and the instance id is
 inserted into the GBO id.
Gets the gbo id from the origgbo id and adds it to the output gbo.
If the gboid is null, then throw a RelationshipUserException.

UpdateWithDelete
First figure out what the verb is whether it is a delete,
 create or update and apply the above behavior
First figure out what the verb is whether it is a delete,
 create or update and apply the above behavior

All other verbs
The instance id corresponding to that row is inserted into the GBO id.
Gets the gbo id from the origgbo id and adds it to the output gbo.

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relSerive.maintainIdentityRelationship("http://www.ibm.com/CustomerRel", "http://www.clarify.com/ClarifyRole", clarifyCustomer, genBO,
                        originalGenBO, null, SERVICE\_CALL\_RESPONSE);

 In the calling context SERVICE\_CALL\_RESPONSE,
 the inputBO is a GBO and the outputBO is an ASBO. The outputBO is an
 instance of the ASBO role specified by the param appRoleName.

 

Verb/ChangeSummary on the inputBO
Existing entry found in table
Entry not found in table
Exceptions

Create,
 Update
Gets the corresponding ASBO key from the table and inserts into
 the ASBO id. If the ASBO id obtained from the table does not match the
 one in the origASBO, then it should log an error.
Checks the origASBO object and gets the key from that object and
 sets it in the output ASBO object. Also, adds a row to the table with this
 ASBO id and the GBO id.
If we need the origASBO to create the entry and the origASBO is
 null or does not have a key, then we won��t be able to create an entry hence
 we throw a RelationshipUserException

UpdateWithDelete
Same as above. Depending on whether it is Create, Update or
 Delete, it will behave like one.
Depending on whether it is Create, Update or Delete, it will
 behave like one.
Same as above

Delete
Same as above. Also the entry has be marked as deactivated.

Same as above

All other verbs
Same as above
Same as above
Same as above

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relSerive.maintainIdentityRelationship("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", genBO, sapCustomer,
                        originalSAPCustomer, null, SERVICE\_CALL\_RESPONSE);

 In the calling context SERVICE\_CALL\_FAILURE, simply puts the key attribute in
 this original input BO into the output BO.

In WPS6.0, the need for parent-children relationships in composite
 relationship maintenance, will be done away with with the new
 maintainIdentityRelationship API.
 That is:
 
   In WPS6.0, users will no longer be required to create
 parent-children relationships in order to help maintain composite
 relationships if they choose to adopt the new maintainIdentity api.
  maintainIdentityRelationship now replaces both
 maintainSimpleIdentityRelationship and
 maintainCompositeIdentityRelationship.
  maintainSimpleIdentityRelationship and
 maintainCompositeIdentityRelationship will still be
 supported but will be marked as deprecated.
    Likewise, the WBI ICS *child* relationship api
 (updateMyChildren, etc.) will still be supported but will be marked
 as deprecated.
    The map 'relationshipCall' transform type will only invoke
 maintainIdentity (vs. maintainSimple or maintainComposite) for direct
 relationship maintenance purposes
 (i.e., for non foreign-key application - for these applications, the
 foreignKey* methods will be used in place of maintain*).
    [MIGRATION] The coexistence scenario for composite relationship
 support requires that the old (deprecated) maintainComposite*,
 *children* api be used, instead of the new maintainIdentity api, when
 composite relationships are shared by both a WBI ICS instance and a
 Diamond Server instance.

- correlate void correlate(java.lang.String relationshipName, java.lang.String inputRoleName, java.lang.String outputRoleName, commonj.sdo.DataObject inputBO, commonj.sdo.DataObject outputBO, commonj.sdo.DataObject originalInputBO, commonj.sdo.DataObject originalOutputBO, java.lang.String callingContext) throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException, com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException, com.ibm.wbiserver.relationshipservice.exceptions.DataNotFoundException, com.ibm.wbiserver.relationshipservice.exceptions.DuplicateDataException Correlates an inputBO of the given inputRoleName with the outputBO of the given outputRoleName and maintains the relationship between them according to the meta data contained in the inputBO (currently either verb or change summary information or both). In order to make use of this API, the following criteria must be met: The following tables document the usage scenarios categorized by the calling context, the direction of the correlation, and the command derived from the meta data contained in the inputBO. The direction of the correlation can be either generic business object (GBO) to application specific business object (ASBO) or ASBO to GBO. The managed role in the relationship is considered the generic role, while all other roles are considered application specific roles. (Note: In the following the header 'existing participant found for input' indicates that a corresponding entry in the role table exists that has not been deactivated, whereas 'no participant found for input' indicates that either no corresponding entry in the role table was found or that the corresponding entry is deactivated) Example for service call request ASBO to GBO invocation: RelationshipService relationshipService = (RelationshipService)ServiceManager.INSTANCE.locateService("com/ibm/wbiserver/rel/RelationshipService"; relationshipService.correlate("http://www.ibm.com/CustomerRel", "http://www.clarify.com/ClarifyRole", "http://www.ibm.com/GenericRole", clarifyCustomerBO, genericBO, null, null, SERVICE\_CALL\_REQUEST); Example for service call response GBO to ASBO invocation: RelationshipService relationshipService = (RelationshipService)ServiceManager.INSTANCE.locateService("com/ibm/wbiserver/rel/RelationshipService"; relationshipService.correlate("http://www.ibm.com/CustomerRel", "http://www.ibm.com/GenericRole", "http://www.clarify.com/ClarifyRole", genericBO, clarifyCustomerBO, origClarifyCustomerBO, origGenericBO, SERVICE\_CALL\_REQUEST); Parameters: relationshipName - The fully qualified name of the relationship inputRoleName - The fully qualified name of the input role outputRoleName - The fully qualified name of the output role inputBO - The input business object of the input role type outputBO - The output business object of the output role type originalInputBO - The original input business object. For calling context SERVICE\_CALL\_RESPONSE or SERVICE\_CALL\_FAILURE this BO may not be null and must be of the output role type. originalOutputBO - The original output business object. For calling context SERVICE\_CALL\_RESPONSE or SERVICE\_CALL\_FAILURE this BO may not be null and must be of the input role type. callingContext - The calling context for the invocation. One of SERVICE\_CALL\_REQUEST, EVENT\_DELIVERY, SERVICE\_CALL\_RESPONSE, and SERVICE\_CALL\_FAILURE. Throws: com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException - Indicates an exception internal to the Relationship Service, such as a missing database connection or other runtime failures. com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException - Indicates an error in the usage of this API. Examples of incorrect use are invalid relationship/role names, business objects that are null or of invalid type, or lack of change summary/verb information in the inputBO. com.ibm.wbiserver.relationshipservice.exceptions.DataNotFoundException - Indicates that a participant was not found when attempting to retrieve it. com.ibm.wbiserver.relationshipservice.exceptions.DuplicateDataException - Indicates a duplicate. Since: WPS6.1 This API replaces maintainIdentityRelationship for maintaining relationships between simple roles (i.e. not parent/child roles). For parent/child roles use correlateToList and correlateFromList.

#### correlate

```
void correlate(java.lang.String relationshipName,
             java.lang.String inputRoleName,
             java.lang.String outputRoleName,
             commonj.sdo.DataObject inputBO,
             commonj.sdo.DataObject outputBO,
             commonj.sdo.DataObject originalInputBO,
             commonj.sdo.DataObject originalOutputBO,
             java.lang.String callingContext)
               throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                      com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException,
                      com.ibm.wbiserver.relationshipservice.exceptions.DataNotFoundException,
                      com.ibm.wbiserver.relationshipservice.exceptions.DuplicateDataException
```

    - The relationship that the relationshipName refers to
      is an 'identity' relationship (i.e. the isIdentity
      attribute on the relationship definition is set to true
    - The relationship has at least one role marked as 'managed' (i.e. the
      managed attribute in the role definition is set to
      true).
    - Either the inputRoleName or the
      outputRoleName refer to the managed role
    - The inputBO matches the role object type of the role
      for the inputRoleName and the outputBO
      matches the role object type of the role for the
      outputRoleName
    - If the calling context is a response or a failure (see usage
      scenarios below), the originalInputBO matches the role
      object type of the role for the outputRoleName and the
      originalOutputBO matches the role object type of the role for
      the inputRoleName
    - Both input and output role are simple roles, i.e. not a parent/child role.
      A parent/child role refers to a role that contains one or more key attributes
      from the parent BO and one or more key attributes from a child BO with the
      intention to maintain the child in the context of its parent.
    - The calling context is SERVICE\_CALL\_REQUEST, the inputBO is an ASBO and
  the outputBO is a GBO.
  

Command derived from verb/change summary
Existing participant found for input
No participant found for input

              Create
          

              The retrieved instance id is set in the key attribute property of the
              generic output BO.
          

              A new participant is created and the generated instance id is set in the
              key attribute property of the generic output BO.
          

              Update
          

              The instance id is retrieved and set in the key attribute property of the
              generic output BO.
          

              A DataNotFoundException is thrown to indicate that an expected
              participant could not be found.
          

              Delete
          

              The participant is deactivated and the instance id is retrieved and set
              in the key attribute property of the generic output BO.
          

              A DataNotFoundException is thrown to indicate that an expected
              participant could not be found.
          

              All other commands
          

              The instance id is retrieved and set in the key attribute property of the
              generic output BO.
          

              A DataNotFoundException is thrown to indicate that an expected
              participant could not be found.
    - The calling context is SERVICE\_CALL\_REQUEST, the inputBO is a GBO and
  the outputBO is an ASBO.
  

Command derived from verb/change summary
Existing participant found for input
No participant exists for input

              Create
          

              No action is taken
          

              No action is taken.
          

              Update
          

              All key attributes are retrieved and set in the key attribute property of the
              application specific output BO.
          

              A DataNotFoundException is thrown to indicate that an expected
              participant could not be found.
          

              Delete
          

              All key attributes are retrieved and set in the key attribute property of the
              application specific output BO.
          

              A DataNotFoundException is thrown to indicate that an expected
              participant could not be found.
          

              All other commands
          

              All key attributes are retrieved and set in the key attribute property of the
              application specific output BO.
          

              A DataNotFoundException is thrown to indicate that an expected
              participant could not be found.
    - The calling context is SERVICE\_CALL\_RESPONSE, the inputBO is an ASBO and
  the outputBO is a GBO.
  

Command derived from verb/change summary
Existing participant found for input
No participant exists for input

              Create
          

              The retrieved instance id is set in the key attribute property of the
              generic output BO.
          

              A new participant is created and the generated instance id is set in the
              key attribute property of the generic output BO.
          

              Update
          

              The instance id is retrieved and set in the key attribute property of the
              generic output BO.
          

              A DataNotFoundException is thrown to indicate that an expected
              participant could not be found.
          

              Delete
          

              The participant is deactivated and the instance id is retrieved and set
              in the key attribute property of the generic output BO.
          

              A DataNotFoundException is thrown to indicate that an expected
              participant could not be found.
          

              All other commands
          

              The instance id is retrieved and set in the key attribute property of the
              generic output BO.
          

              A DataNotFoundException is thrown to indicate that an expected
              participant could not be found.
    - The calling context is SERVICE\_CALL\_RESPONSE, the inputBO is a GBO and
  the outputBO is an ASBO.
  

Command derived from verb/change summary
Existing participant found for input
No participant exists for input

              Create
          

              All key attribute values are extracted from the originalInputBO
              and set to the key attribute properties in the outputBO

              Update
          

              All key attribute values are extracted from the originalInputBO
              and set to the key attribute properties in the outputBO

              All key attribute values are extracted from the originalInputBO
              and set to the key attribute properties in the outputBO

              All other commands
          

              All key attribute values are extracted from the originalInputBO
              and set to the key attribute properties in the outputBO
    - The calling context is EVENT\_DELIVERY, the inputBO is an ASBO and
  the outputBO is a GBO.
  

Command derived from verb/change summary
Existing participant found for input
No participant found for input

              Create
          

              The retrieved instance id is set in the key attribute property of the
              generic output BO.
          

              A new participant is created and the generated instance id is set in the
              key attribute property of the generic output BO.
          

              Update
          

              The instance id is retrieved and set in the key attribute property of the
              generic output BO.
          

              A DataNotFoundException is thrown to indicate that an expected
              participant could not be found.
          

              Delete
          

              The participant is deactivated and the instance id is retrieved and set
              in the key attribute property of the generic output BO.
          

              A DataNotFoundException is thrown to indicate that an expected
              participant could not be found.
          

              All other commands
          

              The instance id is retrieved and set in the key attribute property of the
              generic output BO.
          

              A DataNotFoundException is thrown to indicate that an expected
              participant could not be found.
    - The calling context is EVENT\_DELIVERY, the inputBO is a GBO and
  the outputBO is an ASBO.
  

Command derived from verb/change summary
Existing participant found for input
No participant exists for input

              Create
          

              A RelationshipUserException is thrown to indicate that the pattern
              has been violated by attempting to create a participant.
          

              Update
          

              All key attributes are retrieved and set in the key attribute property of the
              application specific output BO.
          

              A DataNotFoundException is thrown to indicate that an expected
              participant could not be found.
          

              Delete
          

              The participant is deactivated and all key attributes are retrieved and set
              in the key attribute property of the application specific output BO.
          

              A DataNotFoundException is thrown to indicate that an expected
              participant could not be found.
          

              All other commands
          

              All key attributes are retrieved and set in the key attribute property of the
              application specific output BO.
          

              A DataNotFoundException is thrown to indicate that an expected
              participant could not be found.
    - If the calling context is SERVICE\_CALL\_FAILURE, the originalInputBO is used to populate
  the outputBO. No retrieval or modification of participants is done

- correlateToList void correlateToList(java.lang.String relationshipName, java.lang.String inputRoleName, java.lang.String outputRoleName, commonj.sdo.DataObject inputBO, java.util.List outputBOs, java.util.List originalInputBOs, commonj.sdo.DataObject originalOutputBO, java.lang.String callingContext) throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException, com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException, com.ibm.wbiserver.relationshipservice.exceptions.DataNotFoundException, com.ibm.wbiserver.relationshipservice.exceptions.DuplicateDataException Used to correlate the children of a parent/child input role with a list of business objects of a simple output role. The children of the input role are extracted from the inputBO according to the key attribute path defined in the according role definition. The relationship is maintained based on the meta data conatined in the inputBO and the children (currently either verb or change summary information or both). In order to make use of this API, the following criteria must be met: This API supports the same usage scenarios described for correlate(String, String, String, DataObject, DataObject, DataObject, DataObject, String) and applies these rules to all children. In addition, the containment relationship between the inputBO and its children is maintained with repect to the type of business graph and derived command: For after image updates: - all children that have matching participants in the database, but are not contained in the graph are deleted. - all children that exist in the graph, but are not contained in the database are created. For after image deletes: - all children under the parent are deleted In order to facilitate using this API, a helper is provided with getListOfChildren(DataObject, String) to retrieve the list for the outputBOs and originalInputBOs . Example for service call request invocation: RelationshipService relationshipService = (RelationshipService)ServiceManager.INSTANCE.locateService("com/ibm/wbiserver/rel/RelationshipService"; List genricLineItems = relationshipService.getListOfChildren(genericOrder, "lineItems"); relationshipService.correlateToList("http://www.ibm.com/OrderRel", "http://www.sap.com/SAPOrder", "http://www.ibm.com/GenericOrder", sapOrder, genricLineItems, null, null, SERVICE\_CALL\_REQUEST); Parameters: relationshipName - The fully qualified name of the relationship inputRoleName - The fully qualified name of the input role outputRoleName - The fully qualified name of the output role inputBO - The input business object of the input role type outputBOs - A list of output business objects that match the role object child type. originalInputBOs - A list of original input business objects. For calling context SERVICE\_CALL\_RESPONSE or SERVICE\_CALL\_FAILURE this list may not be null or empty and the contained business objects must be of the input role type. originalOutputBO - The original output business object. For calling context SERVICE\_CALL\_RESPONSE or SERVICE\_CALL\_FAILURE this BO may not be null and must be of the input role type. callingContext - The calling context for the invocation. One of SERVICE\_CALL\_REQUEST, EVENT\_DELIVERY, SERVICE\_CALL\_RESPONSE, and SERVICE\_CALL\_FAILURE. Throws: com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException - Indicates an exception internal to the Relationship Service, such as a missing database connection or other runtime failures. com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException - Indicates an error in the usage of this API. Examples of incorrect use are invalid relationship/role names, business objects that are null or of invalid type, or lack of change summary/verb information in the inputBO. com.ibm.wbiserver.relationshipservice.exceptions.DataNotFoundException - Indicates that a participant was not found when attempting to retrieve it. com.ibm.wbiserver.relationshipservice.exceptions.DuplicateDataException - Indicates a duplicate. Since: WPS6.1 This API replaces maintainIdentityRelationship for maintaining relationships between parent/child roles.

#### correlateToList

```
void correlateToList(java.lang.String relationshipName,
                   java.lang.String inputRoleName,
                   java.lang.String outputRoleName,
                   commonj.sdo.DataObject inputBO,
                   java.util.List outputBOs,
                   java.util.List originalInputBOs,
                   commonj.sdo.DataObject originalOutputBO,
                   java.lang.String callingContext)
                     throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                            com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException,
                            com.ibm.wbiserver.relationshipservice.exceptions.DataNotFoundException,
                            com.ibm.wbiserver.relationshipservice.exceptions.DuplicateDataException
```

    - The relationship that the relationshipName refers to
      is an 'identity' relationship (i.e. the isIdentity
      attribute on the relationship definition is set to true
    - The relationship has at least one role marked as 'managed' (i.e. the
      managed attribute in the role definition is set to
      true).
    - The outputRoleName refers to the managed role.
    - The inputBO matches the role object type of the role
      for the inputRoleName and the outputBO
      matches the role object type of the role for the
      outputRoleName
    - If the calling context is a response or a failure (see usage
      scenarios below), the type of the originalInputBOs matches
      the role object type of the role for the outputRoleName and the
      originalOutputBO matches the role object type of the role for
      the inputRoleName
    - The input role is a parent/child role, i.e. the role is defined on the
      parent and contains at least one key attribute path to the child.

- correlateFromList void correlateFromList(java.lang.String relationshipName, java.lang.String inputRoleName, java.lang.String outputRoleName, java.util.List inputBOs, commonj.sdo.DataObject outputBO, commonj.sdo.DataObject originalInputBO, java.util.List originalOutputBOs, java.lang.String callingContext) throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException, com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException, com.ibm.wbiserver.relationshipservice.exceptions.DataNotFoundException, com.ibm.wbiserver.relationshipservice.exceptions.DuplicateDataException Used to correlate a list of business objects of a simple input role with the children of parent/child output role. The children of the output role are extracted from the outputBO according to the key attribute path defined in the according role definition. The relationship is maintained based on the meta data contained in the list of inputBOs (currently either verb or change summary information or both). In order to make use of this API, the following criteria must be met: This API supports the same usage scenarios described for correlate(String, String, String, DataObject, DataObject, DataObject, DataObject, String) and applies these rules to all children. In addition, the containment relationship between the inputBO and its children is maintained with repect to the type of business graph and derived command: For after image updates: - all children that have matching participants in the database, but are not contained in the graph are deleted. - all children that exist in the graph, but are not contained in the database are created. For after image deletes: - all children under the parent are deleted In order to facilitate using this API, a helper is provided with getListOfChildren(DataObject, String) to retrieve the list for the inputBOs and originalOutputBOs . Example for service call request invocation: RelationshipService relationshipService = (RelationshipService)ServiceManager.INSTANCE.locateService("com/ibm/wbiserver/rel/RelationshipService"; List genricLineItems = relationshipService.getListOfChildren(genericOrder, "lineItems"); relationshipService.correlateToList("http://www.ibm.com/OrderRel", "http://www.ibm.com/GenericOrder", "http://www.sap.com/SAPOrder", genricLineItems, sapOrder, null, null, SERVICE\_CALL\_REQUEST); Parameters: relationshipName - The fully qualified name of the relationship inputRoleName - The fully qualified name of the input role outputRoleName - The fully qualified name of the output role inputBOs - A list of input business objects that match the role object child type. outputBO - The output business object of the output role type originalInputBO - The original input business object. For calling context SERVICE\_CALL\_RESPONSE or SERVICE\_CALL\_FAILURE this BO may not be null and must be of the input role type. originalOutputBO - A list of original output business objects. For calling context SERVICE\_CALL\_RESPONSE or SERVICE\_CALL\_FAILURE this list may not be null or empty and the contained business objects must be of the output role type. callingContext - The calling context for the invocation. One of SERVICE\_CALL\_REQUEST, EVENT\_DELIVERY, SERVICE\_CALL\_RESPONSE, and SERVICE\_CALL\_FAILURE. Throws: com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException - Indicates an exception internal to the Relationship Service, such as a missing database connection or other runtime failures. com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException - Indicates an error in the usage of this API. Examples of incorrect use are invalid relationship/role names, business objects that are null or of invalid type, or lack of change summary/verb information in the inputBO. com.ibm.wbiserver.relationshipservice.exceptions.DataNotFoundException - Indicates that a participant was not found when attempting to retrieve it. com.ibm.wbiserver.relationshipservice.exceptions.DuplicateDataException - Indicates that an existing participant was found when attempting to create it. Since: WPS6.1 This API replaces maintainIdentityRelationship for maintaining relationships between parent/child roles.

#### correlateFromList

```
void correlateFromList(java.lang.String relationshipName,
                     java.lang.String inputRoleName,
                     java.lang.String outputRoleName,
                     java.util.List inputBOs,
                     commonj.sdo.DataObject outputBO,
                     commonj.sdo.DataObject originalInputBO,
                     java.util.List originalOutputBOs,
                     java.lang.String callingContext)
                       throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                              com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException,
                              com.ibm.wbiserver.relationshipservice.exceptions.DataNotFoundException,
                              com.ibm.wbiserver.relationshipservice.exceptions.DuplicateDataException
```

    - The relationship that the relationshipName refers to
      is an 'identity' relationship (i.e. the isIdentity
      attribute on the relationship definition is set to true
    - The relationship has at least one role marked as 'managed' (i.e. the
      managed attribute in the role definition is set to
      true).
    - The inputRoleName refers to the managed role.
    - The inputBO matches the role object type of the role
      for the inputRoleName and the outputBO
      matches the role object type of the role for the
      outputRoleName
    - If the calling context is a response or a failure (see usage
      scenarios below), the type of the originalInputBO matches
      the role object type of the role for the outputRoleName and the
      type of the originalOutputBOs matches the role object type of
      the role for the inputRoleName
    - The output role is a parent/child role, i.e. the role is defined on the
      parent and contains at least one key attribute path to the child.

- getListOfChildren
java.util.List getListOfChildren(commonj.sdo.DataObject parent,
                               java.lang.String pathToChildren)
                                 throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- isSetRelationshipProperty
boolean isSetRelationshipProperty(java.lang.String relationshipName,
                                java.lang.String propertyName,
                                int instanceid)
                                  throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                         com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Determines if the user defined property for the given relationship
 instance is set. This property name is one of properties defined in the
 relationship. In a relationship instance, it is optional to set value
 for relationship properties. It can be used for static as well as dynamic
 relationship.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 boolean isSet = relService.isSetRelationshipProperty("http://www.ibm.com/CustomerRel", "DatetimeProperty", 1); 

Parameters:relationshipName - name of the relationship to check. If no relationship found,
 RelationshipUserException is thrown.propertyName - property name to be set. If no property name found in this
 relationship, RelationshipServiceException is thrown.instanceid - ID of the target relationship instance. instanceid equal with or less
 than zero is not valid.
Returns:true, if the target property is set;
   false, if the target property is not set
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- setRelationshipProperty
void setRelationshipProperty(java.lang.String relationshipName,
                           java.lang.String propertyName,
                           java.lang.Object value,
                           int instanceid)
                             throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                    com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Sets value for the user defined property into this relationship instance.
 It can be used for static as well as dynamic relationship.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.setRelationshipProperty("http://www.ibm.com/CustomerRel", "StringProperty", "value\_String", 1); 

Parameters:relationshipName - name of the relationship to set relationship instance property. If no
 relationship found, RelationshipUserException is
 thrown.propertyName - property name to be set. If no property name found in this
 relationship, RelationshipServiceException is thrown.value - value to set for the propertyinstanceid - ID of the relationship instance
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- getRelationshipProperty
java.lang.Object getRelationshipProperty(java.lang.String relationshipName,
                                       java.lang.String propertyName,
                                       int instanceid)
                                         throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                                com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Gets the value of the user defined property in this relationship instance.
 In case of no property value set in this relationship instance, if
 there is a default value defined in the relationship definition, the
 default value is returned; otherwise, null is returned.
 It can be used for static as well as dynamic relationship.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 String value = (String) relService.getRelationshipProperty("http://www.ibm.com/CustomerRel", "StringProperty", 1); 

Parameters:relationshipName - name of the relationship to get property from. If no
 relationship found, RelationshipUserException is
 thrown.propertyName - name of the target property. If no property name found in this
 relationship, RelationshipServiceException is thrown.instanceid - given relationship instanceID
Returns:relationship property value
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- unsetRelationshipProperty
void unsetRelationshipProperty(java.lang.String relationshipName,
                             java.lang.String propertyName,
                             int instanceid)
                               throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                      com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Unsets this property for the given relationship instance. It can be used
 for static as well as dynamic relationship.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.unsetRelationshipProperty("http://www.ibm.com/CustomerRel", "DatetimeProperty", 1); 

Parameters:relationshipName - name of the relationship to unset property value. If no
 relationship found, RelationshipUserException is
 thrown.propertyName - name of the target property. If no property name found in this
 relationship, RelationshipServiceException is thrown.instanceid - given relationship instanceID
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- isSetRoleProperty
boolean isSetRoleProperty(java.lang.String relationshipName,
                        java.lang.String roleName,
                        java.lang.String propertyName,
                        int instanceid,
                        java.lang.Object dataobject)
                          throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                 com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Determines if this user defined property for the given role instance is
 set. This property name is one of properties defined in the role. In a
 role instance, it is optional to set value for role properties. This API
 can be used for static as well as dynamic relationship.

 

 For dynamic relationship or static relationship with BO roleObject,
 param dataobject is an String:

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 boolean result = relService.isSetRoleProperty( "http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", "IntProperty", 1, bo);

 For static relationship with simple type roleObject, param dataobject could
 be String, long, int, float, double or boolean:

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 boolean result = relService.isSetRoleProperty( "http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "IntProperty", 1, "value\_String");

Parameters:relationshipName - name of the relationship to check. If no relationship found,
 RelationshipUserException is thrown.roleName - name of the ASBO role to check. If no role found,
 RelationshipUserException is thrown.propertyName - name of the target property. If no property name found in this
 role, RelationshipServiceException is thrown.instanceid - given relationship instanceIDdataobject - data of the target role instance. For dynamic relationship and static
 relationship with BO roleObject, dataobject is a ASBO. For static
 relationship with simple type roleObject, data could be String, long,
 int, float, double or boolean.
Returns:true, if the target role property is set
   false, if the target role property is not set
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- getRoleProperty
java.lang.Object getRoleProperty(java.lang.String relationshipName,
                               java.lang.String roleName,
                               java.lang.String propertyName,
                               int instanceid,
                               java.lang.Object dataobject)
                                 throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                        com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Gets the value of this user defined property for the given role
 instance. In case of no role property set in this role instance,
 if there is a default value defined in the role definition, the
 default one is returned; otherwise, null is returned.
 This API can be used for static as well as dynamic relationship.

 

 For dynamic relationship or static relationship with BO roleObject:

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 Integer value = (Integer) relService.getRoleProperty( "http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", "IntProperty", 1, bo);

 For static relationship with simple type roleObject:

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 Integer value = (Integer) relService.getRoleProperty( "http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "IntProperty", 1, "value\_String");

Parameters:relationshipName - name of the target relationship. If no relationship found,
 RelationshipUserException is thrown.roleName - name of the ASBO role to get property from. If no role found,
 RelationshipUserException is thrown.propertyName - name of the target property. If no property name found in this
 role, RelationshipServiceException is thrown.instanceid - given relationship instanceIDdataobject - data of the target role instance. For dynamic relationship and static
 relationship with BO roleObject, dataobject is a ASBO. For static
 relationship with simple type roleObject, data could be String, long,
 int, float, double or boolean.
Returns:property value or the default value if the property is not set
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- setRoleProperty
void setRoleProperty(java.lang.String relationshipName,
                   java.lang.String roleName,
                   java.lang.String propertyName,
                   java.lang.Object propertyValue,
                   int instanceid,
                   java.lang.Object object)
                     throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                            com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Sets the specified property with the specifed value for the given
 role instance. It can be used for static as well as dynamic relationship.

 

 For dynamic relationship or static relationship with BO roleObject,
 param object is an String:

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.setRoleProperty( "http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", "IntProperty", new Integer(123456), 1, bo);

 For static relationship with simple type roleObject, param object could
 be String, long, int, float, double or boolean:

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.setRoleProperty( "http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "IntProperty", new Integer(123456), 1, "value\_String");

Parameters:relationshipName - name of the target relationship. If no relationship found,
 RelationshipUserException is thrown.roleName - name of the ASBO role that defines this property name. If no role found,
 RelationshipUserException is thrown.propertyName - name of the property that is defined in the ASBO role. If no property
 name found in this role, RelationshipServiceException is
 thrown.propertyValue - specified property valueinstanceid - given relationship instanceIDobject - data of the target role instance. For dynamic relationship and static
 relationship with BO roleObject, dataobject is a ASBO. For static
 relationship with simple type roleObject, data could be String, long,
 int, float, double or boolean.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- unsetRoleProperty
void unsetRoleProperty(java.lang.String relationshipName,
                     java.lang.String roleName,
                     java.lang.String propertyName,
                     int instanceid,
                     java.lang.Object dataobject)
                       throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                              com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Removes property value for this this role instance.It can be used for
 static as well as dynamic relationship.

 

 For dynamic relationship or static relationship with BO roleObject,
 param object is an String:

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.unsetRoleProperty( "http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", "IntProperty", 1, bo);

 For static relationship with simple type roleObject, param object could
 be String, long, int, float, double or boolean:

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.unsetRoleProperty( "http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "IntProperty", 1, "value\_String");

Parameters:relationshipName - name of the target relationship. If no relationship found,
 RelationshipUserException is thrown.roleName - name of the ASBO role that defines this property name. If no role found,
 RelationshipUserException is thrown.propertyName - name of the property that is defined in the ASBO role. If no property
 name found in this role, RelationshipServiceException is
 thrown.instanceid - given relationship instanceIDdataobject - data of the target role instance. For dynamic relationship and static
 relationship with BO roleObject, dataobject is a ASBO. For static
 relationship with simple type roleObject, data could be String, long,
 int, float, double or boolean.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- createParticipant
int createParticipant(java.lang.String relationshipName,
                    java.lang.String roleName,
                    commonj.sdo.DataObject bo)
                      throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                             com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant to a new relationship instance. The BO contains
 value for the ASBO role. It could also be a BusinessGraph. This
 API can be used for static as well as dynamic relationship.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int instanceID = relService.createParticipant("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", bg);
 
Parameters:relationshipName - name of the relationship to add the relationship instance to. If no
 relationship found, RelationshipUserException is thrown.roleName - name of the ASBO role to add the participant to. If no role found,
 RelationshipUserException is thrown.bo - data to be set for the role attribute. It could also be an BusinessGraph.
Returns:relationship instance ID. If there is an existing participant with the
 same bo, the instanceID of the existing one is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- createParticipantWithID
int createParticipantWithID(java.lang.String relationshipName,
                          java.lang.String roleName,
                          int instanceId,
                          commonj.sdo.DataObject bo)
                            throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                   com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds a participant for an existing relationship instance that has this
 instanceId. BO contains value for this ASBO role. It could also be an
 BusinessGraph. This API can be used for static as well as dynamic
 relationship.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int instanceID = relService.createParticipantWithID("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", targetID, bg);
 
Parameters:relationshipName - name of the relationship to add the participant to. If no
 relationship found, RelationshipUserException is thrown.roleName - name of the ASBO role to add the participant to. If no role found,
 RelationshipUserException is thrown.instanceId - given relationship instanceIDbo - data to be set for the role attribute. It could also be an
 BusinessGraph.
Returns:relationship instance ID. If there is an existing participant with the
 same bo, the instanceID of the existing one is returned.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- setRolePropertyWithOldValue
void setRolePropertyWithOldValue(java.lang.String relationshipName,
                               java.lang.String roleName,
                               java.lang.String propertyName,
                               java.lang.Object propertyValue,
                               java.lang.Object oldPropertyValue,
                               int instanceid)
                                 throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                        com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Sets this propertyValue to the given role property in the role instance.
 This role instance has the specified instanceID and this oldPropertyValue
 in the specified role property name. This API can be used for static as
 well as dynamic relationship.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.setRolePropertyWithOldValue("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", "IntProperty", new Integer(123456), new Integer(11111), 1);
 
Parameters:relationshipName - name of the target relationship. If no relationship found,
 RelationshipUserException is thrown.roleName - name of the ASBO role that defines this property name. If no role found,
 RelationshipUserException is thrown.propertyName - name of the property that is defined in the ASBO role. If no property
 name found in this role, RelationshipServiceException is
 thrown.propertyValue - new property valueoldPropertyValue - old property valueinstanceid - given relationship instanceID
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- unsetRolePropertyWithOldValue
void unsetRolePropertyWithOldValue(java.lang.String relationshipName,
                                 java.lang.String roleName,
                                 java.lang.String propertyName,
                                 java.lang.Object oldPropertyValue,
                                 int instanceid)
                                   throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                          com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Unsets value of this role property in the give role instance.
 This role instance has the specified instanceID and this oldPropertyValue
 in the specified role property name.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.unsetRolePropertyWithOldValue("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", "IntProperty", new Integer(11111), 1);
 
Parameters:relationshipName - name of the target relationship. If no relationship found,
 RelationshipUserException is thrown.roleName - name of the ASBO role that defines this property name. If no role found,
 RelationshipUserException is thrown.propertyName - name of the property that is defined in the ASBO role. If no property
 name found in this role, RelationshipServiceException is
 thrown.oldPropertyValue - specified old property valueinstanceid - given relationship instanceID
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- staticLookup
void staticLookup(java.lang.String relName,
                java.lang.String inputRoleName,
                commonj.sdo.DataObject inputBO,
                java.lang.String[] inputAttrNames,
                java.lang.String outputRoleName,
                commonj.sdo.DataObject outputBO,
                java.lang.String[] outputAttrNames)
                  throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                         com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Performs a static relationship lookup using input Business Object and its property name. Sets the output Business Object property

 to the retrieved value.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.staticLookup("http://www.ibm.com/StateRel", "http://www.sap.com/SAPRole", inputBO, inputAttrNames, "http://www.clarify.com/ClarifyRole", outputBO, outputAttrNames);
 
Parameters:relationshipName - name of the static relationship. If no relationship found or relationship is not static,
 RelationshipUserException is thrown.inputRoleName - name of the input role. If no role found,
 RelationshipUserException is thrown.inputBO. - If input role is based on a BO, then inputBO type has to match the role BO type.
   input BusinessObjectinputAttrNames - list of input Business Object property names. If input role is based on a BO, then input property names have to match the key attributes of

 the input role.outputRoleName - name of the output role. If no role found,
 RelationshipUserException is thrown.outputBO. - If output role is based on a BO, then outputBO type has to match the role BO type.
   input BusinessObjectoutputAttrNames - list of output Business Object property names. If output role is based on a BO, then output property names have to match the key attributes of

 the output role.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- staticLookup
java.lang.Object staticLookup(java.lang.String relName,
                            java.lang.String inputRoleName,
                            java.lang.Object inputAttrValue,
                            java.lang.String outputRoleName)
                              throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                     com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Performs a static lookup by taking relationship name, input and output role names
 and input key attribute value. Returns the retrieved value of the output key attribute.
 This API is added initialy for the static relationship lookup call from XSLT map.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 String stateFullName = (String)relService.staticLookup("http://www.ibm.com/StateRel", "http://www.sap.com/SAPRole", "CA", "http://www.clarify.com/ClarifyRole");
 
Parameters:relName - name of a static relationship. If no relationship found or relationship is not static,
 RelationshipUserException is thrown.inputRoleName - name of the input role. If no role found, RelationshipUserException is thrown.inputAttrValue - input key attribute value. It could be a primitive type that matches the key attribute type of input roleoutputRoleName - name of the output role. If no role found, RelationshipUserException is thrown.
Returns:Object
  output key attribute value. Its type is a primitive type that matches the key attribute type of output role
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- setRelationshipProperties
void setRelationshipProperties(java.lang.String relationshipName,
                             java.lang.String propertyName,
                             java.lang.Object propertyValue)
                               throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                      com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Sets a relationship property to a specified value for all the instances of a relationship.
 It can be used for static as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.setRelationshipProperties("http://www.ibm.com/CustomerRel", "StringProperty", "value\_String"); 

Parameters:relationshipName - name of the relationship whose property needs to be set. If no relationship found, RelationshipUserException is thrown.propertyName - name of the target property. If no property name found in the specified
 relationship, RelationshipServiceException is thrown.propertyValue - property value
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- setRoleProperties
void setRoleProperties(java.lang.String relationshipName,
                     java.lang.String roleName,
                     java.lang.String propertyName,
                     java.lang.Object propertyValue,
                     int instanceid)
                       throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                              com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Sets a role property to a specified value for a relationship instance.
 It can be used for static as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.setRoleProperties( "http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "IntProperty", new Integer(123456), 1);

Parameters:relationshipName - name of the relationship whose role property needs to be set. If no relationship found,
 RelationshipUserException is thrown.roleName - name of the ASBO role that contains the specified property. If no role found,
 RelationshipUserException is thrown.propertyName - name of the target property. If no property
 name found in the specified role, RelationshipServiceException is
 thrown.propertyValue - property valueinstanceid - id of the relationship instance whose role property needs to be set.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- setRoleProperties
void setRoleProperties(java.lang.String relationshipName,
                     java.lang.String roleName,
                     java.lang.String propertyName,
                     java.lang.Object propertyValue)
                       throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                              com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Sets a role property to a specified value for all instances.
 It can be used for static as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.setRoleProperties( "http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "IntProperty", new Integer(123456));

Parameters:relationshipName - name of the relationship whose role property needs to be set. If no relationship found,
 RelationshipUserException is thrown.roleName - name of the ASBO role that contains the specified property. If no role found,
 RelationshipUserException is thrown.propertyName - name of the target property. If no property
 name found in this role, RelationshipServiceException is
 thrown.propertyValue - property value
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- unsetRelationshipProperties
void unsetRelationshipProperties(java.lang.String relationshipName,
                               java.lang.String propertyName)
                                 throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                        com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Unsets a relationship property for all instances of a relationship. It can be used
 for static as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.unsetRelationshipProperties("http://www.ibm.com/CustomerRel", "DatetimeProperty"); 

Parameters:relationshipName - name of the relationship whose property needs to be unset. If no
 relationship found, RelationshipUserException is
 thrown.propertyName - name of the target property. If no property name found in the
 relationship, RelationshipServiceException is thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- unsetRoleProperties
void unsetRoleProperties(java.lang.String relationshipName,
                       java.lang.String roleName,
                       java.lang.String propertyName)
                         throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Unsets a role property for all relationship instances. It can be used for
 static as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.unsetRoleProperties( "http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "IntProperty");

Parameters:relationshipName - name of the relationship that contains the specified role. If no relationship found,
 RelationshipUserException is thrown.roleName - name of the ASBO role that contains the specified property. If no role found,
 RelationshipUserException is thrown.propertyName - name of the target property. If no property name found in this role, RelationshipServiceException is thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- unsetRoleProperties
void unsetRoleProperties(java.lang.String relationshipName,
                       java.lang.String roleName,
                       java.lang.String propertyName,
                       int instanceid)
                         throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Unsets a role property for a relationship instance. It can be used for
 static as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.unsetRoleProperties( "http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "IntProperty",1);

Parameters:relationshipName - name of the relationship that contains the specified role. If no relationship found,
 RelationshipUserException is thrown.roleName - name of the ASBO role that contains the specified property. If no role found,
 RelationshipUserException is thrown.propertyName - name of the target property. If no property
 name found in this role, RelationshipServiceException is
 thrown.instanceid - id of the relationship instance whose role proprety needs to be unset. If the id is invalid,
 RelationshipUserException is thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- getRelationshipProperties
java.util.List getRelationshipProperties(java.lang.String relationshipName,
                                       java.lang.String propertyName)
                                         throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                                com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Gets the values of a user defined relationship property for all instances
  of a relationship. In case of no property value set in an instance, the
 default value is returned if there is a default value defined in
 the relationship definition; otherwise, an empty string is returned for
 that instance. It can be used for static as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 String value = (String) relService.getRelationshipProperties("http://www.ibm.com/CustomerRel", "StringProperty"); 

Parameters:relationshipName - name of the relationship to get property from. If no
 relationship found, RelationshipUserException is
 thrown.propertyName - name of the target property. If no property name found in this
 relationship, RelationshipServiceException is thrown.
Returns:a list of instance id and property value pairs. An empty list if there is no relationship instance exists.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- getRoleProperties
java.util.List getRoleProperties(java.lang.String relationshipName,
                               java.lang.String roleName,
                               java.lang.String propertyName)
                                 throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                        com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Gets the values of a user defined role property for all instances
  of the specified relatinoship, role.
 In case of no role property value set in an instance, the default
 value is returned if there is a default value defined in the role
 definition; otherwise, an empty string is returned for the instance.
 This API can be used for static as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 Integer value = (Integer) relService.getRoleProperties( "http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "IntProperty");

Parameters:relationshipName - name of the target relationship. If no relationship found,
 RelationshipUserException is thrown.roleName - name of the ASBO role to get property from. If no role found,
 RelationshipUserException is thrown.propertyName - name of the target property. If no property name found in this
 role, RelationshipServiceException is thrown.
Returns:a list that each element in the list is also a list that contains instance id, role id and property value.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- getRoleProperties
java.util.List getRoleProperties(java.lang.String relationshipName,
                               java.lang.String roleName,
                               java.lang.String propertyName,
                               int instanceid)
                                 throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                        com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Gets the values of a user defined role property for a instance based on the given relationship
 name, role name, property name and instance id. In case of no role property
 value set in an instance, default value is returned if there is a default value
  defined in the role definition; otherwise, an empty string is returned for the instance.
 This API can be used for static as well as dynamic relationships.
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 Integer value = (Integer) relService.getRoleProperties( "http://www.ibm.com/StaticRel", "http://www.ibm.com/StringRole", "IntProperty", 1);

Parameters:relationshipName - name of the relationship to get property from. If no relationship found,
 RelationshipUserException is thrown.roleName - name of the ASBO role to get property from. If no role found,
 RelationshipUserException is thrown.propertyName - name of the target property. If no property name found in the
 role, RelationshipServiceException is thrown.instanceid - id of the relationship instance to get property for. If the id
 is invalid, RelationshipUserException is thrown.
Returns:a list of role id and property value pairs.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipantsWithID
void addParticipantsWithID(java.lang.String relationshipName,
                         int instanceid,
                         java.util.HashMap roleName\_value)
                           throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                  com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds multiple participants to a relationship instance for multiple roles.
 This API can be used for static as well as dynamic relationships.
 

 Map roleName\_value = new HashMap();

 roleName\_value.put("http://www.sap.com/SAPRole", sapCustomer);

 roleName\_value.put("http://www.clarify.com/ClarifyRole", clarifyCustomer);

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.addParticipantsWithID("http://www.ibm.com/CustomerRel", 1, rolaName\_value);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException is thrown.instanceid - id of the relatinoship instance to add participant to. If id is invalid,
 RelationshipUserException is thrown.roleName\_value - a HashMap that contains role name and participant data pairs.
   role name is the name of the ASBO role to add the participant to. If no role found,
 RelationshipUserException is thrown.
   participant data could be BusinessObject, BusinessGraph, or the supported primitive types.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipants
void addParticipants(java.lang.String relationshipName,
                   java.lang.String roleName,
                   java.util.HashMap iid\_value)
                     throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                            com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds multiple participants to multiple relationship instances for a role.
 This API can be used for static as well as dynamic relationships.
 

 Map iid\_value = new HashMap();

 iid\_value.put(1,sapCustomer1);

 iid\_value.put(2,sapCustomer2);

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.addParticipants("http://www.ibm.com/CustomerRel", "http://www.sap.com/SAPRole", iid\_value);

Parameters:relationshipName - name of the relationship to add the participant to. If no relationship
 found, RelationshipUserException is thrown.roleName - name of the ASBO role to add the participant to. If no role found,
 RelationshipUserException is thrown.iid\_value - a HashMap that contains instance id and participant data pairs.
   iid is the id of the relationship instance to add the participant to. If no role found,
 RelationshipUserException is thrown.
   participant data could be BusinessObject, BusinessGraph, or the supported primitive types.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipants
void addParticipants(java.lang.String relationshipName,
                   java.util.HashMap iid\_subMap)
                     throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                            com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds mulitple participants to multiple relationship instances for multiple roles.
 This API can be used for static as well as dynamic relationships.
 

 Map roleName\_value1 = new HashMap();

 roleName\_value.put("http://www.sap.com/SAPRole", sapCustomer1);

 roleName\_value.put("http://www.clarify.com/ClarifyRole", clarifyCustomer1);

 Map roleName\_value2 = new HashMap();

 roleName\_value2.put("http://www.sap.com/SAPRole", sapCustomer2);

 roleName\_value2.put("http://www.clarify.com/ClarifyRole", clarifyCustomer2);

 Map iid\_subMap = new HashMap>();

 iid\_subMap.put(1,roleName\_Value1);

 iid\_subMap.put(2,roleName\_value2);

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.addParticipants("http://www.ibm.com/CustomerRel", iid\_subMap);

Parameters:relationshipName - name of the relationship to add the participants to. If no relationship
 found, RelationshipUserException is thrown.iid\_subMap - a HashMap that contains instance id and subMap pairs.
  instance id determines the instance to add participants to.
  subMap contains participtns of the instance. It is a HashMap that
  contains role name and participant data pairs.
  role name is the name of the ASBO role to add the participant to. If no role found,
 RelationshipUserException is thrown.
   participant data could be BusinessObject, BusinessGraph, or the supported primitive types.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- addParticipantsWithoutID
int addParticipantsWithoutID(java.lang.String relationshipName,
                           java.util.HashMap roleName\_value)
                             throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                                    com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Adds multiple participants to a new relationship instance for multiple roles.
 This API can be used for static as well as dynamic relationships.
 

 Map roleName\_value = new HashMap();

 roleName\_value.put("http://www.sap.com/SAPRole", sapCustomer);

 roleName\_value.put("http://www.clarify.com/ClarifyRole", clarifyCustomer);

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int id = relService.addParticipantsWithoutID("http://www.ibm.com/CustomerRel", roleName\_value);

Parameters:relationshipName - name of the relationship to add the participant to. If no Relationship
 found, RelationshipUserException is thrown.roleName\_value - a HashMap that contains role name and participant data pairs.
   role name is name of the ASBO role to add the participant to. If no role found,
 RelationshipUserException is thrown.
   participant data could be BusinessObject,
 BusinessGraph, or supported primitive types.
Returns:relationship instance ID
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- deleteParticipants
void deleteParticipants(java.lang.String relationshipName,
                      java.util.List roleNames)
                        throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                               com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Deletes all the participants for the sepecified roles of a relationship.
 It can be used for static as well as dynamic relationships.
 

 List roleNameList = new ArrayList();

 roleNameList.add("http://www.sap.com/SAPRole");

 roleNameList.add("http://www.clarify.com/ClarifyRole");

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 relService.deleteParticipants("http://www.ibm.com/CustomerRel", roleNameList);

Parameters:relationshipName - name of the relationship to delete the participants from. If no
 relationship found, RelationshipUserException is thrown.roleNames - a list of role names to delete the partcipants from. If no role found,
 RelationshipUserException is thrown.
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException

- getNewInstanceId
int getNewInstanceId(java.lang.String relationshipName)
                     throws com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException,
                            com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException
Gets a new instance id for a new relationship instance
 

 RelationshipService relService = (RelationshipService) new ServiceManager().locateService("com/ibm/wbiserver/rel/RelationshipService");

 int instanceId = relService.getNewInstanceId("http://www.ibm.com/CustomerRel");

Parameters:relationshipName - name of the relationship to get the new instance id for. If no
 relationship found, RelationshipUserException is thrown.
Returns:a new instance id that is generated by RelationshipService
Throws:
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipServiceException
com.ibm.wbiserver.relationshipservice.exceptions.RelationshipUserException