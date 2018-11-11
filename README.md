# project 1- Logs Analysis


## whats the project all about ? 

In this project we have been asked to act like we got hired to work with a newspaper site team to bulid internal reporting tool that prints reports -in normal english- based on a givin database. we also have been asked to write the program in python and to use psycopg2 module to connect to the database.


## What is the givin database contains ? 
you have database called news whish contains 3 tables; log table that contains the log info , authors table which contains information about the writes and the articles table which contains info about the articles those writers wrote. 


## what the internal reporting program should report ? 

1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors?


## pr-project required steps: 

for this project we used virtual machine to run the program, so here is some steps you need to follow to install the virtual machine and other needed files:

1- Install the VirtualMachine from this link : https://www.virtualbox.org/wiki/Downloads
2- Install the  Vagrant from this link :  https://www.vagrantup.com/downloads.html
3- Download  a  FSND virtual machine  which contains vagrant setup files that configure the virtual machine and all other needed files from this link :  https://github.com/udacity/fullstack-nanodegree-vmand 

After you done with all the above installations, in the terminal go to your directory where you download the  FSND virtual machine ( for example for me its in project directory) and do the following: 
cd project/FSND-Virtual-Machin
cd vagrant
vagrant up 
vagrant shh
cd /vagrant 
mkdir log-analysis-project
cd log-analysis-project


## install the database to be work with:

1- to install the needed database which calles new.sql from here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zipb.Move

after you installed the database make sure you place it in your log-analysis-project folder and then write in your terminal : 
psql -d news -f newsdata.sql 

and then psql -d news 

you can go exploring the database using \dt and \d table name (ie.  authors , log , articles )

## install the python code for the reporting program :

from this repo install the log_analysis.py file and place it also in the log-analysis-project folder then run it as following :

python log_analysis.py 




## views that have been used for this program: 

In  this program I created 3 views to help me working with database and to achive the desired result as following : 

create view request_error as select cast(log.time as date) as date ,  count(log.status) as error_re from log where log.status !='200 OK' group by date order by date;

create view all_request as select cast(log.time as date) as date ,  count(*) as all_re  from log  group by date order by date ;

create view error_precentage as select all_request.date , (100.0*  request_error.error_re/  all_request.all_re ) as error  from request_error , all_request where all_request.date = request_error.date;



