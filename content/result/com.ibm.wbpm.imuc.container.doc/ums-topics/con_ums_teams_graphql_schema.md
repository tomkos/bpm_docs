# User Management Service Teams GraphQL schema

```
schema {
    query: Query
    mutation: Mutation
}

# Root type for all queries
type Query {

    # Retrieve a team definition
    team(

        # The unique identifier of the team definition.
        uuid: String!,

        # If "shallow", the team definition contains only the directly
        # contained users, groups and teams. If "deep", the team definition
        # contains the recursively contained users, groups and teams
        # (but LDAP groups are not expanded).
        membership: MembershipEnum = shallow

    ): Team

    # Retrieve a teams collection
    teams(
        # When true, only those team are returned that contain the current user.
        myteams: Boolean = false,

        # When specified, only those team definitions matching the filter
        # expression are returned. A filter is a logical expression consisting
        # of an attribute test (e.g., displayName EQ "ABC") or logical
        # combinations (AND, OR, NOT) of attribute tests. Operator precedence
        # can be overridden by braces ```()```.
        filter: String = null,

        # Specifies the attributes whose value is used to order the returned
        # items.
        sortBy: TeamSortByEnum = displayName,

        # Specifies whether the sort order is ascending or descending.
        sortOrder: SortOrderEnum = ascending,

        # Specifies the index of the first retrieved result within the list
        # of all elements that match the search filter. The index starts at 1.
        startIndex: Int = 1,

        # Non-negative integer that specified the desired maximum number of
        # retrieved elements per page. If this parameter is missing, all
        # elements are retrieved.
        maxCount: Int = -1,

        # If "shallow", the team definition contains only the directly
        # contained users, groups and teams. If "deep", the team definition
        # contains the recursively contained users, groups and teams (but LDAP
        # groups are not expanded).
        membership: MembershipEnum = shallow

    ): TeamCollection!
    
    # Check if the current user is a member of any of the provided teams
    userMemberOfAnyTeam(

        # A list of unique identifiers of team definitions.
        teamIds: [String!]

    ): UserMemberOfAnyTeam!

    # Retrieve the info of the current user
    userInfo: UserInfo!

    # Retrieve the permissions of the current user
    userPermission: UserPermission! 
}

# Root type for all mutations
type Mutation {
    # Create a team definition
    createTeam(
        # The team definition when creating a new team
        team: TeamInput!
    ): Team

    # Replace a team definition
    replaceTeam(
        # The unique identifier of the team definition.
        uuid: String!

        # The new team definition for the team with the uuid 
        team: TeamInput!
    ): Team

    # Delete a team definition
    deleteTeam(
        # The unique identifier of the team definition.
        uuid: String!
    ): String
}

# The new team definition
input TeamInput {
    # The team definition's distinguished name
    # Distinguished names are used to identify a teams in a readable and unique way.
    # The distinguished name must be unique among all teams.
    distinguishedName: String!

    # The team definition's display name
    displayName: String

    # The team definition's description
    description: String

    # The distinguished names of users that belong to the team
    users: [String!]

    # The distinguished names of groups that belong to the team
    groups: [String!]

    # The UUIDs of subteams that belong to the team
    teams: [String!]
}

# The team definition
type Team {
    # The team definition's unique identifier
    uuid: String!

    # The team definition's distinguished name.
    # Distinguished names are used to identify a teams in a readable and unique way.
    # The distinguished name must be unique among all teams.
    # While the uuid is immutable, the distinguished name can be modified by the user.
    distinguishedName: String!

    # The team definition's display name
    displayName: String

    # The team definition's description
    description: String

    # The distinguished names of users that belong to the team
    users: [String!] 

    # The distinguished names of groups that belong to the team
    groups: [String!] 

    # The subteams that belong to the team
    teams: [Team!]

    # Meta data about the creation and update timestamps
    metadata: MetaData
}

# Result of userMemberOfAnyTeam query
type UserMemberOfAnyTeam {
    # True, if the current user is a member of any of the provided teams
    memberOfAnyTeam: Boolean!
}

# The information for a user.
type UserInfo {
    # This is a short name uniquely identifying a user. This is expected to be stable
    # and typically matches what the user specified during login.
    userName: String

    # The user's distinguished name.
    distinguishedName: String
 
    # The distinguished names of groups the user belongs to.
    groups: [String!]
}

# The permissions of a user indicate what operations the user is allowed to perform.
type UserPermission {
    # True if the user is permitted to retrieve the list of his own teams.
    canListMyTeams: Boolean!
    
    # True if the user is permitted to retrieve the list of all teams.
    canListAllTeams: Boolean!
          
    # True if the user is permitted to view the details of each team.
    canViewTeamDetails: Boolean!
          
    # True if the user is permitted to create a new team.
    canCreateTeam: Boolean!
          
    # True if the user is permitted to modify each existing team.
    canModifyTeam: Boolean!
          
    # True if the user is permitted to replace each existing team.
    canReplaceTeam: Boolean!
          
    # True if the user is permitted to delete each existing team.
    canDeleteTeam: Boolean!
}

# Meta data about the creation and update timestamps
type MetaData {
    # The time stamp when the object was created
    created: String!

    # The time stamp when the object was modified
    lastModified: String!
}

# Collection of team definitions.
type TeamCollection {
    # An array of team definitions.
    items: [Team!] 

    # Meta data about a paginated collection.
    metadata: PagedCollectionMetaData
}

# Meta data about a paginated collection.
type PagedCollectionMetaData {
    # The total number of elements that match the search filter.
    # A negative number is interpreted as unlimited total number.
    totalSize: Int!

    # The start index in the total list of elements if only a page of elements
    # is returned. The first element has index 1.
    startIndex: Int!

    # The total number of available pages if only a page of elements is returned.
    pageSize: Int

    # The page index if only a page of elements is returned. The first page has
    # page index 1.
    pageIndex: Int
}

# Enumeration for team membership deepness
enum MembershipEnum {
    # Team definitions contains only the directly contained users, groups and teams.
    shallow

    # Team definition contains the recursively contained users, groups and teams.
    deep
}

# Enumeration for team sorting
enum TeamSortByEnum {
    # Sort by distinguishedName
    distinguishedName
    # Sort by displayName
    displayName
    # Sort by description
    description
    # Sort by unique identifier
    uuid
    # Sort by creation timestamp
    created
    # Sort by modification timestamp
    lastModified
}

# Enumeration for sort order
enum SortOrderEnum {
    # Ascending order
    ascending
    # Descending order
    descending
}
```