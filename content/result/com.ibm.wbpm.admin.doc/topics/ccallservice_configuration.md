# callService configuration for running different service types

Administrators can change the callService configuration
to specify types, the combination of services to run, or both. To
change the configuration for callService, add the callservice-valid-services property
in 100Custom.xml. The property contains one or
more valid-service-entry elements that specify the
type of service that you want to run.

```
<properties>
     <server>
         <portal>
             <callservice-valid-services merge="replace">
                      <valid-service-entry>ajax service</valid-service-entry>
             </callservice-valid-services>
         </portal>    
      </server>
</properties>
```

```
<properties>
     <server>
         <portal>
             <callservice-valid-services merge="replace">
                      <valid-service-entry>integration service</valid-service-entry>
             </callservice-valid-services>
         </portal>
     </server>
</properties>
```

- all
- none
- Ajax Service
- Case Manager Integration Service
- Deployment Service Flow
- General System Service
- Human Service
- Installation Service
- Integration Service
- Regular Service
- Rule Service
- SCA Service
- Service Flow
- Undercover Agent Passthrough Service

You can use any combination of the service identifiers to allow callService to
run specific types of services. If the special keywords "all" or "none"
are encountered in the list, all other entries are ignored.

The following example illustrates the configuration
to block everything except for Regular services, Ajax services, and
SCA services.

```
<properties>
     <server>        
        <portal>
             <callservice-valid-services merge="replace">
                      <valid-service-entry>regular service</valid-service-entry>
                      <valid-service-entry>Ajax service</valid-service-entry>
                      <valid-service-entry>SCA service</valid-service-entry>
             </callservice-valid-services>
        </portal>    
      </server>
</properties>
```