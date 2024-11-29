<!-- image -->

# User-specific time zone information

The BPCListHandler class uses the com.ibm.bpc.clientcore.util.User interface
to get information about the time zone and locale of each user. The List component
expects the implementation of the interface to be configured with user as
the managed-bean name in your JavaServer Faces (JSF) configuration
file. If this entry is missing from the configuration file, the time
zone in which the process server is running is returned.

```
public interface User {

    /**
     * The locale used by the client of the user.
     * @return Locale.
     */
    public Locale getLocale();
   /**
    * The time zone used by the client of the user.    
    * @return TimeZone.
    */
    public TimeZone getTimeZone();

   /**
    * The name of the user.
    * @return name of the user.
    */
    public String getName();
}
```