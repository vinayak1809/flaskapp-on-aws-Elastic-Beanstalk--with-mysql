## flaskapp-on-aws-Elastic-Beanstalk--with-mysql
# First create an account on aws and login
Deploying Flask app on aws with mysql

# Step1 : Create a Database

  1. Search **RDS** and click on **Create Database**.
  2. Choose Database creation method as **Standard Create** and Engine options as **MySQL**
  
  
![Engine](https://github.com/vinayak1809/flaskapp-on-aws-Elastic-Beanstalk--with-mysql/blob/master/image/engine%201.png)


  4. Select Edition as **MySQL Community** and Version as per your choice Version **MySQL 8.0.27**
  5. Select Templates as **Free tier** if you are not using any paying to aws to host a database.
  6. Give Database **instance name,username** and **password**.


![Instance](https://github.com/vinayak1809/flaskapp-on-aws-Elastic-Beanstalk--with-mysql/blob/master/image/instance.png)


  8. Leave other settings as it is just give public access **YES**


![Public Access](https://github.com/vinayak1809/flaskapp-on-aws-Elastic-Beanstalk--with-mysql/blob/master/image/public%20access.png)


  10. Then click on **create Database**.
  11. Wait for some minutes unit database gets created.
  12. Then Click on **Database** -> Click on **Configuaration** -> **Inbound rules** -> Edit **inbound rules** and edit as below.


![Inbound Rules](https://github.com/vinayak1809/flaskapp-on-aws-Elastic-Beanstalk--with-mysql/blob/master/image/inbound.png)



  

 # Step 2 : Create Application 
  
   1. Search for **Elastic Beanstalk**
   2. Click on Application -> **Create new Application**
   3. Give **Application Name** and **Description** and click on **create**.


![Application Name](https://github.com/vinayak1809/flaskapp-on-aws-Elastic-Beanstalk--with-mysql/blob/master/image/application%20name.png)


 
 # Step 3 : Create Environment
 
  1. Click on Environment -> **Create new Environment**
  2. Select **Web server Environment**.
  3. Select application name that you gave before.
  4. Give **Enviroment name**. 
 
  6. Select Platform as **Managed platform**


![Select Platform](https://github.com/vinayak1809/flaskapp-on-aws-Elastic-Beanstalk--with-mysql/blob/master/image/selectplatform.png)


  8. Select upload your code and upload your zip file of your code.


![File Upload](https://github.com/vinayak1809/flaskapp-on-aws-Elastic-Beanstalk--with-mysql/blob/master/image/file%20upload.png)


  9. Click on Create Environment(it will take few minutes too create enviroment).
  10. If health is Ok of the app, then the project is successfully deployed on AWS.
  

![Health](https://github.com/vinayak1809/flaskapp-on-aws-Elastic-Beanstalk--with-mysql/blob/master/image/health.png)

  
  11.  How zip file should be.
    
```bash
projectt
├── application.py
├── template
│   ├── page.html
│   └── sign_up.html
└── virt
```
  
