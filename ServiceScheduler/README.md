# Mailchimp Service Scheduler

# A Walkin Service Scheduler


## Introduction

A service scheduler for an in-person customer service center

checkin: A micro-service to persist new checkin into database while validating customer details.

scheduler: A service layer which polls mysql db for new checkins and priortize the service availing queue.

Mysql: A Relational database which holds customers and in-person appointment data.

## Directory Structure
     checkin         : A Python based microservices
     scheduler       : A Python based microservices
     mysql           : A MySQL schema and test data


## System Design

<img width="932" alt="<img width="912" alt="Screen Shot 2023-02-05 at 1 20 05 AM" src="https://user-images.githubusercontent.com/54916661/216804903-a8b68055-1a07-4825-825a-4f7ed2fa4d94.png">
Screen Shot 2023-02-05 at 1 17 06 AM" src="https://user-images.githubusercontent.com/54916661/216804814-8732aa0e-bee0-46df-afba-bf44023a398e.png">



## System Requirements:

1. Docker version 20.10.21
2. Python version > 3.8
3. Preferred IDE (VS CODE, PyCharm)
4. Postman

To install Docker, go to Docker official page (https://docs.docker.com/engine/install/), Download the executable based on your machine platform and run the executable on the machine.

To run the project on your machine, please follow the steps mentioned below:

## Setup:

Step-1. Open terminal. 

Step-2. Clone the repository by using the below command in the terminal

```git clone https://github.com/srinivaskollipoti/Scheduler.git``` 

Step-3. Open the terminal and run the following command

```docker --version``` . This command should result in docker version verifying successful installation of docker.

NOTE: In mac docker compose is installed with docker, but you may need to install it separately for other operating systems. Please refer: https://docs.docker.com/compose/install/

Step-4. Run the following command from the project home directory ```docker-compose build``` (This might take a while to build the images locally.) 

NOTE: There are variations to docker compose command. If ```docker-compose build``` does not work for you, try ```docker compose build```.

Step-5. Verify successful docker image build using command ```docker images``` . (This command will list images)

Step-6. Run ```docker-compose up -d``` to run the containers (i.e our micro-services).

Step-7. Run ```docker ps``` to list the containers of the application. ( i.e checkin, scheduler, mysql).

Step-8. Now the micro-services are up and running, launch Postman to Test Services. 

Note: Please refer to port details in docker-compose.yml file and make sure used ports are available. 


## Design Decisions:

     Create Appointment:
          1. Assuming customer details in the customer table. 
          2. A Customer if checkin by any mode i.e any device allowed to checkin
     
     Customer:
          1. Assuming about type of customer regular or vip is pre-determined and having customer details
          2. A valid Customer payload is provided as request body upon validation inserted to APPOINTMENT table in MySQL Db.
          Note: /mysql/data.sql & /mysql/test-data.sql embodies the tabular structure for CUSTOMER and APPOINTMENT.
     

## Test Services:

1. Make a New appointment
Use the endpoint ```POST - http://localhost:5000/v1/appointment``` to process new appointment. 

A sample payload :
          {
          "firstName":"John",
          "lastName":"Doe",
          "phoneNumber":"555-555-1212",
          "is_vip":true
          }

        
2. GetNextCustomer as scheduler  prioritizes
   Use the endpoint  ```GET - http://localhost:5001/v1/appointment/next```.

 MySQL database constitutes sample test  data and a snapshot of the CUSTOMER & APPOINTMENT table :
 
 
![Uploading Screen Shot 2023-02-05 at 1.20.05 AM.png…]()
<img width="1000" alt="Screen Shot 2023-02-05 at 1 19 37 AM" src="https://user-images.githubusercontent.com/54916661/216804905-44db9e30-1a79-4bda-99ac-12a181ad4c32.png">


       
## Next Steps: 

1) Design Front-End component to checkin through mobile/web based UI.
2) Add Authentication for the API's currently exposed.
3) Deploy checkin service to push messages to queue to attain horizontal scalability.
4) Deploy a auxiallary service to poll DB with new checkins constantly, and employ workers as required to make horizontally scalable
5) Host the docker images of application to AWS-ECR or equivalent cloud service and run multiple instances of micoservices through AWS-ECS or equivalent cloud services.



## Design & Development Standards:
- Coding styles, coding standards were followed throughout the project development. All the modules, classes and functions are inline documented.

- Test cases and development  
     1. The project is being built in stages, with the overall functionality being broken down into smaller modules and milestones. Throughout the project's development, a test-driven development approach is used.
     2. Multiple Testcases were added to validate different functions that were written during code development with usecases.
- Technical documentation is shared providing all the required information about each python module.   

## Test Suite:

   To run the test_suite of checkin, navigate to checkin folder and run : 

        python3 -m pytest tests/

   To run the test_suite of scheduler, navigate to scheduler folder and run:

        python3 -m pytest tests/
