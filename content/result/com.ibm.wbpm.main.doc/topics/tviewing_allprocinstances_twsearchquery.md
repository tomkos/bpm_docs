# Viewing all process instances by using a TWSearch API query

## Procedure

To switch off the authorization, complete the following steps:

1. In the appropriate 100Custom.xml file (see the topic Location of 100Custom configuration files for its location), add the following elements in the
properties element:

<common merge="mergeChildren">
     <search-execution merge="mergeChildren">
          <javascript-administrative-search-processes-with-user-authorization merge="replace">false</javascript-administrative-search-processes-with-user-authorization>
     </search-execution>
</common>
2. Restart the server.