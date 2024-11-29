# Defining usage settings for root client-side human services

## About this task

## Procedure

To define the usage settings of a root client-side human service, complete the
following steps:

1. Open the root client-side human service that you want to work with, and switch to
Overview.
2. In the Usage section, ensure that Nested service
is clear.
3 In the Use as list, specify the usage type by selecting one of thefollowing options. The Use as option is disabled for nested client-side humanservices. Table 1. Usage options for root client-side human services Option Description Task (Service contained in a process) This is the default option for client-side human services that implementactivities within a process. When this option is selected, Expose to start isdisabled. StartableService Use this option to enable members of the selected team to start the rootclient-side human service in Workplace or Process Portal . Dashboard Use this option to make the root client-side human service available inProcess Portal tomembers of the selected team. If you do not specify a localization resource for the dashboardname, the dashboard page has the same name as the exposed service. If you defined a localizationresource for your dashboard name, click Select next toLabel and select the key in the resource. See Globalizing dashboard names . If the root client-side human service isin a toolkit, you must complete the following steps: URL Use this option to make the service available from a URL address.For fastaccess, the URL is displayed as a link that you can either click or copy and paste into your webbrowser. To copy the URL, right-click the link and select the option provided by your browser tocopy the URL (for example, Copy Link Location in Mozilla Firefox orCopy link address in Google Chrome). The URL selects a default versionof the client-side human service to run, depending on the environment. Retrievethe full list of client-side human service URL addresses that are available in the environment byusing the RESTInterface for BPD-related Resources - Exposed Items Resource REST API. See alsoTable 2 and Calling a dynamically selected service version . Process Instance details UI Use this option to indicate that the client-side human service cannot beexposed because it implements an instance details user interface that is used for a processinstance.When you create the process and create the details user interface under Views > Details UI , you also create the client-side human service that implements the user interface forthe specified process instance. When this option is displayed for a client-side human service,the Use as and Expose to start settings underOverview are disabled. The usage of this client-side human service isdetermined only by the settings in the Views folder of the correspondingprocess. For root client-side human services, the URL can include the following additionalparameters:Remember: Any browser-specific URL limitations, such as the URL length andcharacter restrictions, apply when a client-side human service is called as a URL. Input variables In the URL, input variables that are defined for the service have the followingformat:&tw.local.variableName =value Date/Time syntax The date and time format differs between client-side human services andheritage human services. The syntax for the other simple types (String ,Integer , Decimal , Selection ) is thesame for client-side human services and heritage human services. Note: For information about the date and time syntax in exposed heritage human services, see Exposing heritage human services . For client-side human services, the date and time format is specified by a profile of theISO-8601 standard, as defined by RFC3339 .

| Option                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task (Service contained in a process) | This is the default option for client-side human services that implement activities within a process. When this option is selected, Expose to start is disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Startable Service                     | Use this option to enable members of the selected team to start the root client-side human service in Workplace or Process Portal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Dashboard                             | Use this option to make the root client-side human service available in Process Portal to members of the selected team. If you do not specify a localization resource for the dashboard name, the dashboard page has the same name as the exposed service. If you defined a localization resource for your dashboard name, click Select next to Label and select the key in the resource. See Globalizing dashboard names. If the root client-side human service is in a toolkit, you must complete the following steps:  Create a snapshot of the toolkit.  Activate the toolkit snapshot. See Activating snapshots for use with IBM Process Portal  Add the toolkit snapshot as a dependency to a process application. See Managing toolkit dependencies.           |
| URL                                   | Use this option to make the service available from a URL address.For fast access, the URL is displayed as a link that you can either click or copy and paste into your web browser. To copy the URL, right-click the link and select the option provided by your browser to copy the URL (for example, Copy Link Location in Mozilla Firefox or Copy link address in Google Chrome). The URL selects a default version of the client-side human service to run, depending on the environment. Retrieve the full list of client-side human service URL addresses that are available in the environment by using the REST Interface for BPD-related Resources - Exposed Items Resource REST API.  See also Table 2  and Calling a dynamically selected service version. |
| Process Instance details UI           | Use this option to indicate that the client-side human service cannot be exposed because it implements an instance details user interface that is used for a process instance.When you create the process and create the details user interface under Views > Details UI, you also create the client-side human service that implements the user interface for the specified process instance. When this option is displayed for a client-side human service, the Use as and Expose to start settings under Overview are disabled. The usage of this client-side human service is determined only by the settings in the Views folder of the corresponding process.                                                                                                   |

```
&tw.local.variableName=value
```

    - The Date format is YYYY-MM-DD.
    - The Time format is [hh]:[mm]:[ss] , where For example, the time might be displayed as 13:47:30 .
        - [hh] specifies a zero-padded hour between 00 and 24 (where 24 indicates
midnight at the end of a calendar day).
        - [mm] specifies a zero-padded minute between 00 and 59.
        - [ss] specifies a zero-padded second between 00 and 60 (where 60 indicates
an added leap second).
- Note the following time zone designators for Time :
    - If no UTC relation information is given with a time representation,
<time> is assumed to be the local time. The
<time>Z parameter refers to UTC time. For example, 14:45:15
UTC can be 14:45:15Z.
    - The following parameters are time zone offsets from UTC time:<time>±hh:mm
<time>±hhmm
<time>±hhFor example, the following times refer to the same moment:
18:30Z, 22:30+04, 1130-0700,
and 15:00-03:30.
- The combined Date and Time format is
<date>T<time>, for example
2007-04-05T14:30Z or 2007-04-05T12:30-02:00.
4. Click Select next to Expose to start to choose
the team whose members can view and use the exposed service.
Note:  The Expose to start option is not available for embedded
client-side human services.
To create a team, click New. To remove an
assigned team, click the X icon next to New.
5. Click Save or Finish Editing.

## Results

| Environment            | Default version of the client-side human service                                                                                                                                                                                                                                                                                 |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Workflow Center server | The version of the exposed running service is the same as the one that is in the current working version of the default track. For testing purposes, any author in this environment can run the client-side human service as a URL regardless of the service's Usage and Expose to start settings.                               |
| Workflow Server        | The version of the exposed running service is the same as the one that is in the default snapshot.                                                                                                                                                                                                                               |
| Workplace l            | When you start a client-side human service as a dashboard or a startable service, Process Portal uses the REST Interface for BPD-related Resources - Exposed Items Resource REST API to make all the active snapshots available. You can then select which snapshot version to run by clicking the icon to the left of its name. |

- Calling a dynamically selected client-side human service version (snapshot)

When you use ID-based parameters to call a client-side human service as a URL, you start the service version that is exposed in a specific snapshot or tip. To call a dynamically selected version, you can use name-based parameters in the URL.