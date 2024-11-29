# Configuring single sign-on for federated environments by using a custom trust association
interceptor (TAI)

## Procedure

1. Develop and implement a custom trust association interceptor.
Use the com.ibm.wsspi.security.tai.TrustAssociationInterceptor interface
that is provided by Process Federation Server to
implement your custom TAI.
2. Put the custom TAI class in a JAR file, for example, simpleTAI.jar,
and then make the JAR file available as a shared library.
3. Update the Process Federation Server server.xml file
with the custom TAI configuration information: <trustAssociation id="myTrustAssociation" invokeForUnprotectedURI="false" failOverToAppAuthType="false">
   <interceptors>
      className="com.ibm.websphere.security.sample.SimpleTAI"
      libraryRef="simpleTAI" invokeBeforeSSO="true" enabled="true">
      <properties defaultUser="u1"/>
   </interceptors>
</trustAssociation>

<library id="simpleTAI" name="simpleTAI">
   <fileset dir="pfs\_install\_root/usr/servers/server\_name/resources" includes="SimpleTAI.jar"/>
</library>
4 Configure the federated servers to use the custom TAI:
    1. Put the JAR file for the custom TAI in the
BPM\_HOME/lib/ext directory.
    2. Log in to the administrative console.
    3. Open the Global security page by selecting
Security > Global security.
Expand Web and SIP security and click Trust
association.
    4. In the Trust association window, under Additional
properties, click Interceptors.
    5. In the Interceptors window, click New,
enter the class name for the custom TAI and any additional properties.
    6. Save the settings and restart the environment.
5. Optional: Configure a list of cookie names and header names. If
the custom TAI on the federated servers requires cookies or headers from the user's request,
configure the propagateCookieNames property, the
propagateHeaderNames property, or both in the Process Federation Server
server.xml file. For more information, see Configuration properties for the Process Federation Server index.