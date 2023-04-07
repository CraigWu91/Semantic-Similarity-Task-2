# Overview
The dockerfile will install all the pre-requisites to get the python app working. Mainly en-core-web-md and it will also copy the movies text file required for the code to run

# Instructions
* To run the mySite web application using Docker make sure you have Docker installed https://docs.docker.com/get-docker/
* In the commands.txt file you will see 2 commands that you need to run
* First run "docker build -t watchnext ./". You should see the image in your docker desktop
* Second run "docker run watchnext" to create a container. You should see the container in your docker desktop now running
* Running the image will also automatically run the python file
