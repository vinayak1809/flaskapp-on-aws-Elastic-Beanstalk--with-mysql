## flaskapp-on-aws-Elastic-Beanstalk--with-mysql
# First create an account on aws and login
Deploying Flask app on aws with mysql

# Step1 : Create a Database

  1. Search **RDS** and click on **Create Database**.
  2. Choose Database creation method as **Standard Create** and Engine options as **MySQL**
  3. Select Edition as **MySQL Community** and Version as per your choice Version **MySQL 8.0.27**
  4. Select Templates as **Free tier** if you are not using any paying to aws to host a database.
  5. Give Database **instance name,username** and **password**.
  6. leave other settings as it is just give public access **YES**
  7. then click on **create Database**.
  8. Wait for some minutes unit database gets created.
  9. Then Click on **Database** -> Click on **Configuaration** -> **Inbound rules** -> Edit **inbound rules** and edit as below .
  

 # Step 2 : Create Application 
  
   1. Search for **Elastic Beanstalk**
   2. Click on Application -> **Create new Application**
   3. Give **Application Name** and **Description** and click on **create**.
 
 # Step 3 : Create Environment
 
  1. Click on Environment -> **Create new Environment**
  2. Select **Web server Environment**.
  3. Select application name that you gave before.
  4. Give **Enviroment name**. 
  5. Select Platform as **Managed platform**
  6. Select upload your code and upload your zip file of your code.
  7. Click on Create Environment(it will take few minutes too create enviroment).
  8. How zip file should be.
    
  
