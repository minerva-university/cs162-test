## Making HTTP requests

This pre-class work can be quite long if you have had no previous exposure to
HTML and web programming. In this case you are encouraged to find someone with
some prior experience and work together. (Conversely, if you do have any prior
experience, then you are encouraged to find someone with no web experience to
help them!)

### HTML Forms

The first time that you usually encounter an HTML request (other than a GET
request) is in an HTML form. The following (freely-available) short course uses
active learning to help you understand HTML forms:
https://developer.mozilla.org/en-US/docs/Learn/HTML/Forms

For this session you will need to work through the following guides:

1. Your first form
2. How to structure a web form
3. The native form controls
4. Sending form data

After which you should feel comfortable tackling questions 1 and 2.

### Python HTTP requests

However, we can also query the web through a python program. There are many
ways of making http requests programmatically. A nice library is the `requests`
library. You can install it using:

```bash
pip3 install requests
```

Now work through [the guide to HTTP requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview).

And then read through the [quickstart for python requests](http://docs.python-requests.org/en/master/user/quickstart/).

### JSON

The web services listed below all return information in a format known as JSON.
Fortunately for us it is straightforward to turn the JSON back into standard
python objects that you are already familiar with.

As an example (borrowed from the requests tutorial), here is a call to github,
which is then read into a python list of python dictionaries:

```python3
>>> import requests
>>> r = requests.get('https://api.github.com/events')
>>> r.json()
[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...
```

## Questions

### 1. httpbin Form

Using Chrome dev tools, inspect the following form:
https://httpbin.org/forms/post

1. See how the form is structured and how the data is sent to the server.
2. Fill in the form and submit it.
3. Make sure to capture the POST request (in the network tab).

### 2. Kanban form

Build on your work from the previous session in which you designed a basic
Kanban website. For today's class you need to build a small HTML form which
will allow you to write a short description of the task which you want to add
to the board. Use inspiration from the httpbin form, and from the HTML form
documentation that you read as part of the pre-class work.

Make sure you have the HTML form ready to paste into a document when you
come to class.

### 3. httpbin Python

Visit [httpbin](https://httpbin.org/) and look at the schema for several of the endpoints and methods.
Using AI tools write working Python code to achieve the following:

1. Successfully log in using basic auth
2. Download an image
3. Generate a UUID4
4. Return a simple JSON response

For learning purposes, please print all the requests and responses so the all
the data can be seen.

You can write a single program which does all of these things, or you can write
several programs, one for each task. Use the requests library, so that it is easier
for everyone to read each other's code.

### 4. (Optional) Public APIs

Browse the following repo:
https://github.com/public-apis/public-apis

1. Find an interesting or whimsical API
2. Write some simple Python code to query the API
3. Bring the code to class!

**Please commit your work to your PCW repo and push it to github before class!**
