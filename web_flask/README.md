Concepts
For this project, we expect you to look at this concept:

- [AirBnB clone](https://intranet.alxswe.com/concepts/74)
**Resources**
Read or watch:

- [What is a Web Framework?](https://intranet.alxswe.com/rltoken/64SQpOGx46Ljp0zFJchESg)
- [A Minimal Application](https://intranet.alxswe.com/rltoken/NopQlHIr9J_9OPX9XRgfvw)
- [Routing (except “HTTP Methods”)](https://intranet.alxswe.com/rltoken/cQiIhbSdIcg1Ao1MICseBg)
- [Rendering Templates](https://intranet.alxswe.com/rltoken/DBM65T59nySd0ZRlZZ0CXw)
- [Synopsis](https://intranet.alxswe.com/rltoken/5Y_A7XB9Qo1JeZgiSUq0yQ)
- [Variables](https://intranet.alxswe.com/rltoken/ITzobwYP1Lc4KqEUUcYCGw)
- [Comments](https://intranet.alxswe.com/rltoken/ykUFuQSE9KD1M7WGY-4v4w)
- [Whitespace Control](https://intranet.alxswe.com/rltoken/NMLZom50ZVOxQlgYW3rnuQ)
- [List of Control Structures (read up to “Call”)](https://intranet.alxswe.com/rltoken/5AGhzIt0zSpPJh9SFysdMQ)
- [Flask](https://intranet.alxswe.com/rltoken/VJs151_hsE9g7Cw-Pz5bVg)
- [Jinja](https://intranet.alxswe.com/rltoken/2y_hunzGCCvSot06EW67UQ)
**Learning Objectives**
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
- What is a Web Framework
- How to build a web framework with Flask
- How to define routes in Flask
- What is a route
- How to handle variables in a route
- What is a template
- How to create a HTML response in Flask by using a template
- How to create a dynamic template (loops, conditions…)
- How to display in HTML data from a MySQL database
**More Info**
Install Flask
`$ pip3 install Flask`
![web model](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step3.png)
**Tasks**
0. Hello Flask!
mandatory
Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
	- /: display “Hello HBNB!”
- You must use the option strict_slashes=False in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$
```
File: `0-hello_route.py`, `__init__.py`

1. HBNB
mandatory
Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
	- /: display “Hello HBNB!”
	- /hbnb: display “HBNB”
- You must use the option strict_slashes=False in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$
file: `1-hbnb_route.py`

```
2. C is fun!
mandatory
Write a script that starts a Flask web application:

- Your web application must be listening on 0.0.0.0, port 5000
- Routes:
	- /: display “Hello HBNB!”
	- /hbnb: display “HBNB”
	- /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
- You must use the option strict_slashes=False in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$
```
File: `2-c_route.py`

3. Python is cool!
mandatory
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
	- /: display “Hello HBNB!”
	- /hbnb: display “HBNB”
	- /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
	- /python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
		- The default value of text is “is cool”
- You must use the option strict_slashes=False in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$
```
File: `3-python_route.py`

4. Is it a number?
mandatory
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
- Routes:
	- /: display “Hello HBNB!”
	- /hbnb: display “HBNB”
	- /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
	- /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
	- The default value of text is “is cool”
	- /number/<n>: display “n is a number” only if n is an integer
- You must use the option strict_slashes=False in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$
```
File: `4-number_route.py`

5. Number template
mandatory
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
- Routes:
	- /: display “Hello HBNB!”
	- /hbnb: display “HBNB”
	- /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
	- /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
		- The default value of text is “is cool”
	- /number/<n>: display “n is a number” only if n is an integer
	- /number_template/<n>: display a HTML page only if n is an integer:
		- H1 tag: “Number: n” inside the tag BODY
- You must use the option strict_slashes=False in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$
```
File: `5-number_template.py`, `templates/5-number.html`

6. Odd or even?
mandatory
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
- Routes:
	- /: display “Hello HBNB!”
	- /hbnb: display “HBNB”
	- /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
	- /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
		- The default value of text is “is cool”
	- /number/<n>: display “n is a number” only if n is an integer
	- /number_template/<n>: display a HTML page only if n is an integer:
		- H1 tag: “Number: n” inside the tag BODY
	- /number_odd_or_even/<n>: display a HTML page only if n is an integer:
		- H1 tag: “Number: n is even|odd” inside the tag BODY
- You must use the option strict_slashes=False in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.6-number_odd_or_even
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 89 is odd</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>Number: 32 is even</H1>
    </BODY>
</HTML>
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
guillaume@ubuntu:~$
```
File: `6-number_odd_or_even.py`, `templates/6-number_odd_or_even.html`
