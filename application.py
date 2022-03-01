from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests
import pyodbc

#connecting to database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NISH-PC\SQLEXPRESS;'
                      'Database=Practice;'
                      'Trusted_Connection=No;'
)
                      #'UID=sa;'
                      #'PWD=Bidya321@;')


application=Flask(__name__)
api = Api(application)

# Getting the whole data of
class Data(Resource):
    def get(self):
        cursor = conn.cursor()
        data=cursor.execute("SELECT  CAST([EmpID] as Varchar) as ID,CAST([SALARY] as VARCHAR(max)) as SALARY,CAST(DeptID as varchar) as DeptID,CAST(EmpName as varchar) as NAME FROM [PRACTICE].[dbo].[Employee_Details]")
        newlist=[]
        for i in data:
            newdict={"ID":i[0],"Salary":i[1],"Date":i[2],"Name":i[3]}
            newlist.append(newdict)
        return newlist


#  Getting data by specifying Id,Name
class Id_Name(Resource):
    def get(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('Id', required=True)  # add args
        parser.add_argument('Name', required=True)
        #parser.add_argument('userId', required=True)  # add args
        args = parser.parse_args()
        ID=args['Id']
        NAME=args['Name']
        cursor = conn.cursor()
        data=cursor.execute("SELECT  CAST([EmpID] as Varchar) as ID,CAST([SALARY] as VARCHAR(max)) as SALARY,CAST(DeptID as varchar) as DeptID,CAST(EmpName as varchar) as NAME FROM [PRACTICE].[dbo].[Employee_Details]",ID,NAME)
        newlist=[]
        for i in data:
            newdict={"ID":i[0],"Salary":i[1],"Date":i[2],"Name":i[3]}
            newlist.append(newdict)
        return newlist


# Getting data by specifying Id,Name,Salary         
class Id_Name_Salary(Resource):
    def get(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('Id')  # add args
        parser.add_argument('Name')  # add args
        parser.add_argument('Salary')  # add args
        #parser.add_argument('userId', required=True)  # add args
        args = parser.parse_args()
        ID=args['Id']
        NAME=args['Name']
        SALARY=args['Salary']
        cursor = conn.cursor()
        data=cursor.execute("SELECT  CAST([EmpID] as Varchar) as ID,CAST([SALARY] as VARCHAR(max)) as SALARY,CAST(DeptID as varchar) as DeptID,CAST(EmpName as varchar) as NAME FROM [PRACTICE].[dbo].[Employee_Details]",ID,NAME,SALARY)
        newlist=[]
        for i in data:
            newdict={"ID":i[0],"Salary":i[1],"Date":i[2],"Name":i[3]}
            newlist.append(newdict)
        return newlist
        

#adding endpoints for API
api.add_resource(Data, '/data')  # add endpoints
api.add_resource(Id_Name, '/data/ID/Name')  # add endpoints
api.add_resource(Id_Name_Salary, '/data/ID/Name/Salary')  # add endpoints


    
#calling the main and running the whole code 
if __name__ == '__main__':
    application.run()  # run our Flask app