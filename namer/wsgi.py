#!/usr/bin/python
from search import Search
from server import app as application

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    print("Loading server...")
    Search()  # Loads data into search engine cache

    httpd = make_server('0.0.0.0', 5000, application)
    print("Serving corporate names on http://0.0.0.0:5000/\n")
    httpd.serve_forever()
    print("Terminated!!")
