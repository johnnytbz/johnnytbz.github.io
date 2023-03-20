---
layout: post
title: OWASP API Security top 10 Introduction
subtitle: The Open Web Application Security Project (OWASP) 
tags: [technology]
comments: true
---
# Introduction

- The Open Web Application Security Project (OWASP) is a non-profit, collaborative online community behind the OWASP Top 10. They produce articles, methodologies, documentation, tools, and technologies to improve application security.

- Since 2003, OWASP Top 10 project has been the authoritative list of information prevalent to web application vulnerabilities and the ways to mitigate them. in 2019, OWASP started an effort to create a version of their Top 10 dedicated specifically to API security. The first OWASP API Security Top 10 list was released on 31 December 2019.

# API Security Risk Rating

&emsp;&emsp;The OWASP Risk Rating Methodology was used to do the risk analysis.
The table below summarizes the terminology associated with the risk score.

![Crepe](/img/owasp/p001.png)

# API1: Broken object level authorization

&emsp;&emsp;Attackers substitute the ID of their own resource in the API call with an ID of a resource belonging to another user. The lack of proper authorization checks allows attackers to access the specified resource.

![Crepe](/img/owasp/p002.png)

### Example Attack Scenarios

**Scenario #1**


&emsp;An e-commerce platform for online stores (shops) provides a listing page with the revenue charts for their hosted shops. Inspecting the browser requests, an attacker can identify the API endpoints used as a data source for those charts and their pattern /shops/{shopName}/revenue_data.json. Using another API endpoint, the attacker can get the list of all hosted shop names. With a simple script to manipulate the names in the list, replacing {shopName} in the URL, the attacker gains access to the sales data of thousands of ecommerce stores.

**Scenario #2**


&emsp;While monitoring the network traffic of a wearable device, the following HTTP PATCH request gets the
attention of an attacker due to the presence of a custom HTTP request header X-User-Id: 54796.
Replacing the X-User-Id value with 54795, the attacker receives a successful HTTP response, and is able to modify other users' account data.

### How To Prevent

- Implement authorization checks with user policies and hierarchy.（Session,JWT）
- Do not rely on IDs that the client sends. Use IDs stored in the session object instead.
- Check authorization for each client request to access database.
- Use random IDs that cannot be guessed (UUIDs).

# API2: Broken User Authentication

- Poorly implemented API authentication allows attackers to assume other users’ identities.
- Type of Auth:

  - Basic
  - Session
  - JWT
  - Auth2.0

![Crepe](/img/owasp/p003.png)

### Example Attack Scenarios

**Scenario #1**


&emsp;An attacker starts the password recovery workflow by issuing a POST request to /api/system/verification-codes and by providing the username in the request body. Next an SMS
token with 6 digits is sent to the victim’s phone. Because the API does not implement a rate limiting policy, the attacker can test all possible combinations using a multi-threaded script, against the
/api/system/verification-codes/{smsToken} endpoint to discover the right token within a few minutes.

**Scenario #2**


- Unprotected APIs that are considered “internal”
- Weak authentication
- Credentials and keys included in URLs

### How To Prevent

- Check all possible ways to authenticate to all APIs.
- APIs for password reset and one-time links also allow users to authenticate, and should be protected just as rigorously.
- Use standard authentication, token generation, password storage, and multi-factor authentication (MFA).
- Use short-lived access tokens.
- Authenticate your apps (so you know who is talking to you).
- Use stricter rate-limiting for authentication, and implement lockout policies and weak password checks.

# API3: Excessive Data Exposure

&emsp;&emsp;The API may expose a lot more data than what the client legitimately needs, relying on the client to do the filtering. If attackers go directly to the API, they have it all.

![Crepe](/img/owasp/p004.png)

### Example Attack Scenarios

**Scenario #1**


&emsp;The client-side code running in the user’s web browser is submitting a POST request to a backend API to retrieve stored payment information. /payments/storedcard/json
the API is retrieving stored credit card information, specifically primary account number (PAN) and card verification value (CVV) code.[{"PAN":"41111111123454321","status":"ok","CVV":"1234"}]

**Scenario #2**


&emsp;An surveillance system allows administrators to create users with different permissions. An admin
created a user account for a new security guard that should only have access to specific buildings on the site.
Once the security guard uses his mobile app, an API call is triggered to: /api/sites/111/cameras in
order to receive data about the available cameras and show them on the dashboard. The response contains a list
with details about cameras in the following format: {"id":"xxx","live_access_token":"xxxxbbbbb","building_id":"yyy"}. While the client GUI shows only cameras which the security guard should have access to, the actual API response contains a full list of all the cameras in the site.

### How To Prevent

- Never rely on the client to filter data!
- Review all API responses and adapt them to match what the API consumers really need.
- Carefully define schemas for all the API responses.
- Do not forget about error responses, define proper schemas as well.
- Identify all the sensitive data or Personally Identifiable Information (PII) and justify its use.
- Enforce response checks to prevent accidental leaks of data or exceptions.

# API4: Lack of Resources & Rate Limiting

&emsp;&emsp;The API is not protected against an excessive amount of calls or payload sizes. Attackers can use this for Denial of Service (DoS) and authentication flaws like brute force attacks.

![Crepe](/img/owasp/p005.png)

### Example Attack Scenarios

**Scenario #1**

&emsp;An attacker uploads a large image by issuing a POST request to /api/v1/images. When the upload is
complete, the API creates multiple thumbnails with different sizes. Due to the size of the uploaded image, available memory is exhausted during the creation of thumbnails and the API becomes unresponsive.

**Scenario #2**

&emsp;We have an application that contains the users' list on a UI with a limit of 200 users per page. The users' list is retrieved from the server using the following query: /api/users?page=1&size=100. An attacker changes the size parameter to 200 000, causing performance issues on the database. Meanwhile, the API becomes unresponsive and is unable to handle further requests from this or any other clients (aka DoS).

### How To Prevent

- Define proper rate limiting.
- Limit payload sizes.
- Tailor the rate limiting to be match what API methods, clients, or addresses need or should be allowed to get.
- Add checks on compression ratios.
- Define limits for container resources.

# API5: Broken Function Level Authorization

&emsp;&emsp;The API relies on the client to use user level or admin level APIs as appropriate. Attackers figure out the “hidden” admin API methods and invoke them directly.

![Crepe](/img/owasp/p006.png)

### Example Attack Scenarios

**Scenario #1**


&emsp;The attacker has changed the method from POST. to DELETE allowing them to delete the account associated with user_id=exampleId_100. Access to the DELETE method should have been restricted to users with administrative access but was allowed due to an inadequate authorization policy.

![Crepe](/img/owasp/p007.png)

### How To Prevent

- Do not rely on the client to enforce admin access.
- Deny all access by default.
- Only allow operations to users belonging to the appropriate group or role.
- Properly design and test authorization.

# API6: Mass Assignment

- Modern application frameworks encourage developers to use functions that automatically bind input from the client into code variables and internal objects in order to help simplify and speed up development within the framework.
- Attackers can use this side effect of frameworks to their advantage by updating or overwriting properties of sensitive objects that developers never intended to expose.
- Mass assignment vulnerabilities are also sometimes referred to as auto binding or object injection vulnerabilities.

![Crepe](/img/owasp/p008.png)

### Example Attack Scenarios

**Scenario #1**


&emsp;A ride sharing application provides a user the option to edit basic information for their profile. During this process, an API call is sent to PUT /api/v1/users/me with the following legitimate JSON object:
{"user_name":"inons","age":24} The request GET /api/v1/users/me includes an additional credit_balance property: {"user_name":"inons","age":24,"credit_balance":10}.
The attacker replays the first request with the following payload: {"user_name":"attacker","age":60,"credit_balance":99999}

**Scenario #2**


&emsp;A video sharing portal allows users to upload content and download content in different formats. An attacker who explores the API found that the endpoint GET /api/v1/videos/{video_id}/meta_data returns
a JSON object with the video’s properties. One of the properties is "mp4_conversion_params":"-v
codec h264", which indicates that the application uses a shell command to convert the video.
The attacker also found the endpoint POST /api/v1/videos/new is vulnerable to mass assignment and
allows the client to set any property of the video object. The attacker sets a malicious value as follows:
"mp4_conversion_params":"-v codec h264 && format C:/". This value will cause a shell command injection once the attacker downloads the video as MP4.

### How To Prevent

- If possible, avoid using functions that automatically bind a client’s input into code variables or internal
  objects.
- Whitelist only the properties that should be updated by the client.
- Use built-in features to blacklist properties that should not be accessed by clients.
- If applicable, explicitly define and enforce schemas for the input data payloads.

# API7: Security Misconfiguration

&emsp;&emsp;Poor configuration of the API servers allows attackers to exploit them.

![Crepe](/img/owasp/p009.png)

### Example Attack Scenarios

**Scenario #1**


&emsp;An attacker finds the .bash_history file under the root directory of the server, which contains commands
used by the DevOps team to access the API:

```
$ curl -X GET 'https://api.server/endpoint/' -H 'authorization: Basic Zm9vOmJhcg=='
```

An attacker could also find new endpoints on the API that are used only by the DevOps team and are not
documented.

**Scenario #2**


&emsp;To target a specific service, an attacker uses a popular search engine to search for computers directly accessible from the Internet. The attacker found a host running a popular database management system, listening on the default port. The host was using the default configuration, which has authentication disabled by default, and the attacker gained access to millions of records with PII, personal preferences, and authentication data.

### How To Prevent

- Establish repeatable hardening and patching processes.
- Automate locating configuration flaws.
- Disable unnecessary features.
- Restrict administrative access.
- Define and enforce all outputs, including errors.

# API8: Injection

&emsp;&emsp;Attackers construct API calls that include SQL, NoSQL, LDAP, OS, or other commands that the API or the backend behind it blindly executes.

![Crepe](/img/owasp/p010.png)

### Example Attack Scenarios

**Scenario #1**


&emsp;We have an application with basic CRUD functionality for operations with bookings. An attacker managed to
identify that NoSQL injection might be possible through bookingId query string parameter in the delete
booking request. This is how the request looks like: DELETE /api/bookings?bookingId=678.
The API server uses the following function to handle delete requests:

```
router.delete('/bookings', async function (req, res, next) {
  try {
	const deletedBooking = await Bookings.findOneAndRemove({_id' : req.query.bookingId});
	res.status(200);
     } catch (err) {
	res.status(400).json({
	error: 'Unexpected error occured while processing a request'});}
});
```

The attacker intercepted the request and changed bookingId query string parameter as shown below. In this case, the attacker managed to delete another user's booking:

```
DELETE /api/bookings?bookingId[$ne]=678
```

### How To Prevent

- Never trust your API consumers, even if they are internal.
- Strictly define all input data, such as schemas, types, and string patterns, and enforce them at runtime.
- Validate, filter, and sanitize all incoming data.
- Define, limit, and enforce API outputs to prevent data leaks.

# API9: Improper Assets Management

&emsp;&emsp;Attackers find non-production versions of the API (for example, staging, testing, beta, or earlier versions) that are not as well protected as the production API, and use those to launch their attacks.

![Crepe](/img/owasp/p011.png)

### Example Attack Scenarios

**Scenario #1**


&emsp;After redesigning their applications, a local search service left an old API version(api.someservice.com/v1) running, unprotected, and with access to the user database. While targeting one of the latest released applications, an attacker found the API address (api.someservice.com/v2).Replacing v2 with v1 in the URL gave the attacker access to the old, unprotected API, exposing the personal identifiable information (PII) of over 100 Million users.

**Scenario #2**


&emsp;A social network implemented a rate-limiting mechanism that blocks attackers from using brute-force to guess reset password tokens. This mechanism wasn’t implemented as part of the API code itself, but in a separate component between the client and the official API (www.socialnetwork.com). A researcher found a beta API host (www.mbasic.beta.socialnetwork.com) that runs the same API, including the reset
password mechanism, but the rate limiting mechanism was not in place. The researcher was able to reset the password of any user by using a simple brute-force to guess the 6 digits token.

### How To Prevent

- Keep an up-to-date inventory all API hosts.
- Limit access to anything that should not be public.
- Limit access to production data, and segregate access to production and non-production data.
- Implement additional external controls, such as API firewalls.
- Properly retire old versions of APIs or backport security fixes to them.
- Implement strict authentication, redirects, CORS, and so forth.

# API10: Insufficient Logging & Monitoring

&emsp;&emsp;Lack of proper logging, monitoring, and alerting allows attacks and attackers go unnoticed.

![Crepe](/img/owasp/p012.png)

### Example Attack Scenarios

**Scenario #1**


&emsp;Access keys of an administrative API were leaked on a public repository. The repository owner was notified by email about the potential leak, but took more than 48 hours to act upon the incident, and access keys exposure may have allowed access to sensitive data. Due to insufficient logging, the company is not able to assess what data was accessed by malicious actors.

**Scenario #2**


&emsp;A video-sharing platform was hit by a “large-scale” credential stuffing attack. Despite failed logins being
logged, no alerts were triggered during the timespan of the attack. As a reaction to user complaints, API logs were analyzed and the attack was detected. The company had to make a public announcement asking users to reset their passwords, and report the incident to regulatory authorities.

### How To Prevent

- Log failed attempts, denied access, input validation failures, or any failures in security policy checks.
- Ensure that logs are formatted so that other tools can consume them as well.
- Protect logs like highly sensitive information.
- Include enough detail to identify attackers.
- Avoid having sensitive data in logs — if you need the information for debugging purposes, redact it partially.
- Other dashboards, monitoring, and alerting tools.

# Summary

&emsp;&emsp;As security is a crucial aspect of modern development. Every day we come across data breaches and cyber-attacks, which can run a company into losses. Above, we have listed OWASP API Security Top 10  are worthy of attention. API testing also plays a very important role in security, as it helps you identify loopholes and repair them.

# References

**OWASP**

- [OWASP API Security Project](https://owasp.org/www-project-api-security/)
- [API Security Top 10 2019 (PDF)](https://github.com/OWASP/API-Security/raw/master/2019/en/dist/owasp-api-security-top-10.pdf)
- [Top 10 Web Application Security Risks](https://owasp.org/www-project-top-ten/)
- [OWASP API Check](https://owasp.org/www-project-apicheck/)

**External**

- [Top 10 API Security Vulnerabilities According to OWASP](https://curity.io/resources/learn/owasp-to-ten/)
- [API Security Best Practices](https://curity.io/resources/learn/api-security-best-practices/)
- [The API Security Maturity Model](https://curity.io/resources/learn/the-api-security-maturity-model/)
- [Testing OWASP’s Top 10 API Security Vulnerabilities](https://nordicapis.com/testing-owasps-top-10-api-security-vulnerabilities/)
- [7 Open-Source API Security Tools](https://nordicapis.com/7-open-source-api-security-tools/)
- [Update your code, use Transport Layer Security (TLS)](https://hpbn.co/transport-layer-security-tls/)
