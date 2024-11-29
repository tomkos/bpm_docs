<!-- image -->

# Change the quality of service at run time

## About this task

## Procedure

1. Right-click StockQuote\_MediationFlow and select Test
Component.
2 In the Events page, enter these initial request parameters,and click Continue .
    - For symbol, enter AAA.
    - For customerID, enter CustomerB.

<!-- image -->

3. Select the server for the unit test environment. Click Finish and
enter the username and password to login to the server. The default
is admin\admin. The results in the emulator show
that the service invoked is RealtimeService. You can also see the
value of the qualityOfService string which tells you that this customer's
service level is premium.
4. Switch to the Servers view. Right-click the server, and
select Administration > Run administrative console.
 In the log in window, enter your userid and password (the default
is admin/admin). Click Log in.
5. In the administrative console, expand Applications and
click SCA modules.
6. In the list of applications, click StockQuote.
7. Click Module Properties.
8. 'The property that you promoted earlier is displayed, showing
the alias PREMIUM\_SERVICE. Click the value field of PREMIUM\_SERVICE,
and change "premium" to "nomatch". Click Apply.
 This means that when the lookup returns with the subscriptionLevel
set to premium, it won't match to the realtime terminal, and therefore
will take the default path.
9. In the messages window, click Save.
10. In the SCA Modules window, click the Save button.
11. Switch to the Events page of the test client. Click Invoke  on the
upper left side of the page.
12. Keep AAA as the symbol value, and
enter CustomerB, the premium service customer,
as the customerID value. Click Continue
The results in the Events area show DelayedService as
the invoked service.