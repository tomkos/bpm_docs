# User Management Service single sign-on

You can use UMS SSO to provide a common login page for Business Automation Workflow apps that are enabled to delegate
authentication to the service. If you have multiple deployments, users can have a single sign-on
experience when they interact with more than one of them.

Because Business Automation Workflow combines
several technologies and runtime servers in your virtual cloud-based environments, UMS helps you
manage this complexity by consolidating aspects of user management in a single place.

UMS SSO brings the following advantages:

- Reuses existing customizations of Trust Association Interceptors for single sign-on.
- Provides an authentication scheme that is based on the open standards OpenID Connect and OAuth 2.0.
- Familiarity for many administrators from a configuration and operations perspective.

If an unauthenticated user requests access to a protected resource that is owned by Business Automation Workflow, then the user is redirected to
UMS to sign on. After the authentication completes successfully, the user is redirected back to the
web application, which then checks the user’s authorization and, if successful, returns the
protected resource. The OpenID Connect protocol requires that the Offering Party and Relying Party
are made known to each other as part of the configuration. This happens as part of the automated
setup process when Business Automation Workflow is
installed using the operator.

The following sections describe what happens between login and logout for containers that
delegate authentication to UMS.

## OpenID Connect (OIDC) login

When an unauthenticated user requests a protected URL from an application, for example IBM Business Automation Studio, the browser is redirected to UMS for
authentication. Upon authentication in UMS, a session with UMS is established that uses cookies, and
the user is redirected back to Business Automation Studio to
complete the login sequence. Business Automation Studio also
establishes a session with the browser by using cookies. Two independent sessions with two servers
are open from the same browser.

## Single Sign-On

When the same user from the same browser attempts to access a different application or another
instance of the same application, the user is redirected to UMS for authentication. Because the
browser already has an established cookie-based session with UMS, the user is not prompted for
credentials. The user is redirected to the second application, which completes the login sequence
and another cookie-based session is established.

## Identity propagation

## Logout

Users often interact with one or more applications from their browser. When a user clicks
Logout in an application, a request is sent from the browser to the server
and the server-side session is invalidated and cookies are removed.

Each application is configured to redirect a browser to the UMS logout endpoint
/oidc/endpoint/ums/logout. UMS invalidates the session and clears the related
cookies.

- Invoking OAuth 2.0 protected APIs

 Containers: 
For your client application to invoke a REST API that is provided by a component that has been configured to delegate authentication to User Management Service (UMS) single sign-on (SSO), the client app must present an access token.