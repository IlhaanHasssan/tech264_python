# Overview of APIs and HTTP
<!-- TOC -->
* [Overview of APIs and HTTP](#overview-of-apis-and-http)
    * [What are APIs?](#what-are-apis)
    * [How are APIs Used and Why are They So Popular?](#how-are-apis-used-and-why-are-they-so-popular)
    * [Data Transfer Process in API Communication](#data-transfer-process-in-api-communication)
    * [What is a REST API?](#what-is-a-rest-api)
    * [What Makes an API RESTful?](#what-makes-an-api-restful)
    * [What are the REST Guidelines?](#what-are-the-rest-guidelines)
    * [What is HTTP?](#what-is-http)
    * [HTTP Request Structure](#http-request-structure)
    * [HTTP Response Structure](#http-response-structure)
    * [What are the 5 HTTP Verbs and What Do They Do?](#what-are-the-5-http-verbs-and-what-do-they-do)
    * [What is Statelessness?](#what-is-statelessness)
      * [Examples of Stateless and Stateful HTTP Requests:](#examples-of-stateless-and-stateful-http-requests)
    * [What is Caching?](#what-is-caching)
<!-- TOC -->
### What are APIs?
APIs (Application Programming Interfaces) are sets of rules and protocols that allow different software applications to communicate with each other. They enable developers to access specific features or data from an application or service without needing to understand its internal workings. 

### How are APIs Used and Why are They So Popular?
APIs are used for various purposes, including:
- **Integration**: Connecting different systems or services (e.g., linking a web app to a payment processor).
- **Data Retrieval**: Accessing information from databases or services (e.g., fetching weather data).
- **Automation**: Streamlining workflows and processes (e.g., automating data entry).

APIs are popular due to their ability to simplify development, promote interoperability, and facilitate the creation of rich, scalable applications.

### Data Transfer Process in API Communication
![API Data Transfer Process](https://hygraph.com/blog/how-do-apis-work)

### What is a REST API?
A REST API (Representational State Transfer API) is a type of web API that adheres to the principles of REST architecture. It allows clients to access and manipulate resources using standard HTTP methods.

### What Makes an API RESTful?
An API is considered RESTful if it:
- Uses standard HTTP methods (GET, POST, PUT, DELETE).
- Is stateless, meaning each request from a client contains all the information needed for the server to fulfill it.
- Uses URIs (Uniform Resource Identifiers) to identify resources.

### What are the REST Guidelines?
The REST guidelines include:
- Resource representation (JSON or XML).
- Use of standard HTTP status codes.
- Layered system architecture.
- Stateless communication.

### What is HTTP?
**HTTP** stands for **Hypertext Transfer Protocol**. It is a protocol used for transmitting data over the web. HTTP facilitates communication between clients (like web browsers) and servers, allowing users to request and receive web content.

**What is HTTPS?**
**HTTPS** stands for **Hypertext Transfer Protocol Secure**. It is the secure version of HTTP, using encryption (SSL/TLS) to protect data exchanged between clients and servers.

### HTTP Request Structure
An HTTP request consists of:
1. **Request Line**: Contains the HTTP method, URL, and HTTP version.
2. **Headers**: Key-value pairs providing additional context (e.g., `Content-Type`).
3. **Body** (optional): Contains data sent with the request (e.g., form data).

![HTTP Request Structure](https://www.tutorialspoint.com/http/images/http_request_structure.jpg)

### HTTP Response Structure
An HTTP response consists of:
1. **Status Line**: Contains the HTTP version, status code, and status message.
2. **Headers**: Key-value pairs providing additional context (e.g., `Content-Length`).
3. **Body**: Contains the requested resource or information.

![HTTP Response Structure](https://www.tutorialspoint.com/http/images/http_response_structure.jpg)

### What are the 5 HTTP Verbs and What Do They Do?
- **GET**: Retrieves data from a server.
- **POST**: Sends data to a server to create a resource.
- **PUT**: Updates an existing resource or creates one if it doesn't exist.
- **PATCH**: Partially updates an existing resource.
- **DELETE**: Removes a resource from the server.

### What is Statelessness?
Statelessness means that each request from a client to a server is treated as an independent transaction. The server does not retain any client context between requests.

#### Examples of Stateless and Stateful HTTP Requests:
- **Stateless**: A user requests a webpage, and the server does not remember the user’s previous requests.
- **Stateful**: A user logs into a website, and the server maintains their session information until they log out.

### What is Caching?
Caching is the process of storing copies of files or data in temporary storage (cache) so that future requests for that data can be served faster. It reduces latency and improves application performance by minimizing the need to fetch data from the original source repeatedly.

