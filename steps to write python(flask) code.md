
#steps to write python code.
  1. open terminal and Follow this commands
```python
mkdir project
cd project
```
  2. Create virtual enviroment and download required dependencies.

```python
virtualenv virt
source virt/bin/activate
pip install flask
pip install mysql-connector-python
```
  3. create application file and template folder
```python
touch application.py
```
 
```python
mkdir template
touch application.py
```
```python
cd template
touch sign_up.html
touch page.html
```
  4. Get all your requirements into one file.

```python 
pip freeze > requirements.txt 
```

  5. Create .ebignore file and paste your environement there and save this file.
  6. Two more files should be created i.e. **.elasticbeanstalk and .gitgnore**.
(This files gets created by itself if project(python code) is deployed from terminal)

**.elasticbeanstalk** file
```python 
branch-defaults:
  default:
    environment: environment name
environment-defaults:
  environment name-env:
    branch: null
    repository: null
global:
  application_name: application name
  branch: branch name
  default_ec2_keyname: null
  default_platform: Python 3.8 running on 64bit Amazon Linux 2
  default_region: ap-south-1
  include_git_submodules: true
  instance_profile: null
  platform_name: null
  platform_version: null
  profile: eb-cli
  repository: aws-app
  sc: git
  workspace_type: Application
```

**.gitgnore** file
```python 
.elasticbeanstalk/*
!.elasticbeanstalk/*.cfg.yml
!.elasticbeanstalk/*.global.yml
```



