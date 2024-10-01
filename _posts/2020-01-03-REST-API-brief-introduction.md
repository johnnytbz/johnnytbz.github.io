---
layout: post
title: REST API brief introduction
subtitle: How to understand REST API
tags: [technology]
comments: true
---


# What is REST API?

## REST definition

  REST is the abbreviation of Representational State Transfer. The direct translation means "representational state transfer".

  It is an API design concept for Internet applications: URL locates resources and HTTP verbs (GET, POST, DELETE, DETC) are used to describe operations.

  If an architecture conforms to the REST principle, it is called a RESTful architecture.

  What is representational?
  ~~~	
    XML, JSON, TEXT to present the data representing the response
  ~~~	
  What is state transfer?
  ~~~	
    response data from the server, sent the state / data to the client
  ~~~	
  Resource identifier
  ~~~	
    URL / endpoint
  ~~~	
  Representation Metadata
    header / content-type

## HTTP Verbs

~~~	
GET (SELECT): retrieves a resource (one or more) from the server.
POST (CREATE): creates a new resource on the server.
PUT (UPDATE): updates a resource on the server (the client provides the complete resource after the change).
PATCH (UPDATE): updates a resource on the server (the client provides the changed properties).
DELETE (DELETE): deletes a resource from the server.
~~~	  

### examples

~~~	
GET /zoos: List all zoos
POST /zoos: Create a new zoo
GET /zoos/ID: Get information about a specific zoo
PUT /zoos/ID: Update information about a specific zoo (provide all information about the zoo)
PATCH /zoos/ID: Update information about a specific zoo (provide partial information about the zoo)
DELETE /zoos/ID: Delete a specific zoo
GET /zoos/ID/animals: List all animals in a specific zoo
DELETE /zoos/ID/animals/ID: Delete a specific animal in a specific zoo
~~~	  

### Filtering

  If there are a lot of records, the server cannot return all of them to the user. 
  The API should provide parameters to filter the returned results.
  Below are some common parameters.
~~~	
?limit=10: specifies the number of records to be returned
?offset=10: specifies the starting position of the returned records.
?page=2&per_page=100: specifies the page number and the number of records per page.
?sortby=name&order=asc: specifies the attribute by which the returned results are sorted and the sorting order.
?animal_type_id=1: specifies the filter condition
~~~	  

## Status Codes

  The status codes and prompt information returned by the server to the user are commonly seen as follows (the HTTP verbs corresponding to the status codes are in square brackets).

~~~	
200 OK - [GET]: The server successfully returns the data requested by the user. This operation is idempotent.
201 CREATED - [POST/PUT/PATCH]: The user successfully creates or modifies data.
202 Accepted - [*]: Indicates that a request has entered the background queue (asynchronous task)
204 NO CONTENT - [DELETE]: The user successfully deletes data.
400 INVALID REQUEST - [POST/PUT/PATCH]: The request sent by the user is wrong. The server does not create or modify data. This operation is idempotent.
401 Unauthorized - [*]: Indicates that the user does not have permission (token, username, password error).
403 Forbidden - [*] Indicates that the user is authorized (as opposed to 401 error), but access is prohibited.
404 NOT FOUND - [*]: The request sent by the user is for a non-existent record. The server did not perform the operation. This operation is idempotent.
406 Not Acceptable - [GET]: The format requested by the user is not available (for example, the user requested JSON format, but only XML format is available).
410 Gone - [GET]: The resource requested by the user is permanently deleted and will not be obtained again.
422 Unprocesable entity - [POST/PUT/PATCH] A validation error occurred when creating an object.
500 INTERNAL SERVER ERROR - [*]: An error occurred on the server and the user will not be able to determine whether the request was successful.
~~~	

## demo

  swagger yaml file using

    https://editor.swagger.io/?_ga=2.3628400.1714038499.1638196716-1457558838.1638196716
    
  postman using 
