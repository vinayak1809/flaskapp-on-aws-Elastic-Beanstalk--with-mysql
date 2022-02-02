
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


