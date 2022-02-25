from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import requests
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NISHANT-BLRIT;'
                      'Database=PRACTICE;'
                      'Trusted_Connection=yes;')


app = Flask(__name__)
api = Api(app)

class Data(Resource):
    def get(self):
        cursor = conn.cursor()
        data=cursor.execute("SELECT  [EID],CAST([ESALARY] as VARCHAR(max)) as SALARY,CAST([EDATE] as VARCHAR(max)) as DATE ,CAST([ENAME]  as VARCHAR(max)) as NAME FROM [PRACTICE].[dbo].[Employee]")
        newlist=[]
        for i in data:
            newdict={"ID":i[0],"Salary":i[1],"Date":i[2],"Name":i[3]}
            newlist.append(newdict)
        return newlist
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
        data=cursor.execute("SELECT  [EID],CAST([ESALARY] as VARCHAR(max)) as SALARY,CAST([EDATE] as VARCHAR(max)) as DATE ,CAST([ENAME]  as VARCHAR(max)) as NAME FROM [PRACTICE].[dbo].[Employee] WHERE [EID]=? AND ENAME=?",ID,NAME)
        newlist=[]
        for i in data:
            newdict={"ID":i[0],"Salary":i[1],"Date":i[2],"Name":i[3]}
            newlist.append(newdict)
        return newlist
        
class Id_Name_Salary(Resource):
    def get(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('Id', required=True)  # add args
        parser.add_argument('Name', required=True)  # add args
        parser.add_argument('Salary', required=True)  # add args
        #parser.add_argument('userId', required=True)  # add args
        args = parser.parse_args()
        ID=args['Id']
        NAME=args['Name']
        SALARY=args['Salary']
        cursor = conn.cursor()
        data=cursor.execute("SELECT  [EID],CAST([ESALARY] as VARCHAR(max)) as SALARY,CAST([EDATE] as VARCHAR(max)) as DATE ,CAST([ENAME]  as VARCHAR(max)) as NAME FROM [PRACTICE].[dbo].[Employee] WHERE [EID]=? AND ENAME=? and ESALARY=?",ID,NAME,SALARY)
        newlist=[]
        for i in data:
            newdict={"ID":i[0],"Salary":i[1],"Date":i[2],"Name":i[3]}
            newlist.append(newdict)
        return newlist
        
api.add_resource(Data, '/data')  # add endpoints
api.add_resource(Id_Name, '/ID/Name')  # add endpoints
api.add_resource(Id_Name_Salary, '/ID/Name/Salary')  # add endpoints


    

if __name__ == '__main__':
    app.run()  # run our Flask app