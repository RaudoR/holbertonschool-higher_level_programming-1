# 0x10. Python - Network #0

**What you should learn from this project**

    At the end of this project you are expected to be able to explain to anyone, without the help of Google:

* What a URL is
* What HTTP is
* How to read a URL
* The scheme for a HTTP URL
* What a domain name is
* What a sub-domain is
* How to define a port number in a URL
* What a query string is
* What an HTTP request is
* What an HTTP response is
* What HTTP headers are
* What the HTTP message body is
* What an HTTP request method is
* What an HTTP response status code is
* What an HTTP Cookie is
* How to make a request with cURL
* What happens when you type google.com in your browser (Application level)

## Exercises

[0-body_size.sh](./0-body_size.sh)
```
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
```
* The size must be displayed in bytes
* You have to use curl

[1-body.sh](./1-body.sh)
```
Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
```
* Display only body of a 200 status code response
* You have to use curl

[2-delete.sh](./2-delete.sh)
```
Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
```
* You have to use curl

[3-methods.sh](./3-methods.sh)
```
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
```
* You have to use curl

[4-header.sh](./4-header.sh)
```
Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
```
* A header variable X-HolbertonSchool-User-Id must be sent with the value 98
* You have to use curl

[5-post_params.sh](./5-post_params.sh)
```
Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
```
* A variable email must be sent with the value hr@holbertonschool.com
* A variable subject must be sent with the value I will always be here for PLD
* You have to use curl

[6-peak.py](./6-peak.py)
```
Technical interview preparation: 
Write a function that finds a peak in a list of unsorted integers.
```
* You are not allowed to google anything
* Whiteboard first
* Prototype: def find_peak(list_of_integers):
* You are not allowed to import any module
* Your algorithm must have the lowest complexity 
* 6-peak.py must contain the function
* 6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)

## Author
### Kevin Yook 
Email: <yook00627@gmail.com> Twitter: [@yook00627](https://twitter.com/yook00627)
