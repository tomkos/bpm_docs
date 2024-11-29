# Understanding User Management Service login and logout
behavior

The OIDC specification is evolving and adding support for single sign-out. These aspects of the
protocol are not yet widely supported by the server side technologies used in the DBA platform.

## OpenID Connect (OIDC) login

When an unauthenticated user requests a protected URL from a DBA component, for example IBM® Business Automation Workflow (BAW system 1), the browser is redirected to
UMS for authentication. Upon authentication in UMS, a session with UMS is established using cookies,
and the user is redirected back to the DBA component to complete the login sequence. The DBA
component also establishes a session with the browser using cookies. At this point, we have two
independent sessions with two servers from the same browser.

## Single Sign-On

When the same user from the same browser attempts to access another DBA component (for example
BAW system 2), there is no session between the browser and this DBA component, so the user is again
redirected to UMS for authentication. But because the user's browser already has an established
cookie-based session with UMS, the user is not prompted for credentials. The user is redirected back
to the DBA component (BAW system 2) which completes the login sequence and another cookie-based
session is established between the browser and BAW system 2.

## Logout

It is important to
understand that other DBA components (BAW system 1 in the current example) are not notified about
the logout and session termination in UMS or other DBA components. The user's session with other DBA
components remains active. To terminate all active sessions, users can close their browsers or use
the logout button for each system that they logged into.