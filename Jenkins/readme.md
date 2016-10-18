# Test + Analysis

## Set Up

* Using the tools we got from last milestone, we can easily provision a build server with Jenkins and DigitalOcean
* run ```node provision_jenkins.js``` to create a droplet
* run ```ansible-playbook -i inventory jenkins.yml``` to install ```jenkins``` and all the dependencies
* The open source project that we selected to test is [httpbin](https://github.com/DevOps2016Fall/httpbin), which is a python package.

## Test Suites
We use the following packages and plugins to implement unit tests and display results

* nose: unitest for python code.
* coverage: compute coverage for python code.
* pylint: statical code analysis for python code.
* Junit Plugin: display the unit test results generated from nose.
* Cobertura Plugin: display the coverage analysis from coverage.
* Violations Plugin: display the statical analysis results from pylint.

![unit](img/unittest.png) 

## Advanced Testing:test case generation
Based on the project [httpbin](https://github.com/DevOps2016Fall/httpbin) test cases, we implement a test case generator using ast module in python, which will read the source code ```core.py``` and generate a test case based on default parameters of each function. We can see that our converage is improved from 70% to 77%.
![unit](img/unnitest2.png) 

## Basic Analysis 
We used ```pylint``` which is a statical analysis tool for python language. we get the following results.
![](img/pylint.png)

## Custom Metrics: 
![](img/metric.png)

## Gates:
* [Demo: accept and reject a commit]()








  
  
  

