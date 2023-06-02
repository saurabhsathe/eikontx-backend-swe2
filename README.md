
## Submission
The current submission has the Dockerfile and requirements.txt required to run this project. 
The code has been developed as per my understanding of the questions. I had a lot of questions regarding the assignment given which I would love to ask if the opportunity given


## Technical Requirements
In order to run this project the host machine needs the Docker system to allow Docker container to be deployed and run

## Add PostgresSQL db connection string
There is a folder called database_ops in the home directory of the project. In this folder there is a connection.py file. This connection.py file has a connection_string variable. We need to assign the connection string in this variable



## Docker commands to build and run this applcation
sudo docker build --tag eikon-app .
sudo docker run -dp 4000:4000 eikon-app


## Triggering the ETL
The api developed is a post api which runs the ETL pipeline. Its running on the 4000 port of the host machine. It returns the derived features as response. An example would be the following POST request
http://3.21.236.252:4000/trigger_etl







