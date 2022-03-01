from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests
import pyodbc

#connecting to database
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=10.150.72.22;'
                      'Database=ARMS;'
                      'UID=dmdbobjects.prod;'
                      'PWD=spice@123;'
                      'Trusted_Connection=Yes;'
                    )


application = Flask(__name__)
api = Api(application)

# Getting the whole data of
class Data(Resource):
    def get(self):
        cursor = conn.cursor()
        data=cursor.execute("select TRY_CAST(EmployeeID as Varchar) as EmployeeID,TRY_CAST(StaffID as Varchar) as StaffID,CAST(EmployeeName as Varchar) as EmpName,CAST(EmployeeCategory as Varchar) as EmployeeCategory,CAST(EmployeeStatus as Varchar) as EmployeeStatus,CAST(ResignedDate as Varchar) as ResignedDate,TRY_CAST(RepositoryShortName as Varchar) as Rank from com.Employee e left join com.REPOSITORY r on CAST(e.RankID as varchar)=cast(r.RepositoryID as varchar)")
        newlist=[]
        for i in data:
            newdict={"EmployeeID":i[0],"StaffID":i[1],"EmployeeName":i[2],"EmployeeCategory":i[3],"EmployeeStatus":i[4],"ResignedDate":i[5],"Rank":i[6]}
            newlist.append(newdict)
        return newlist


#  Getting data by specifying Id,Name
class Id(Resource):
    def get(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('Id', required=True)  # add args
        #parser.add_argument('Name', required=True)
        #parser.add_argument('userId', required=True)  # add args
        args = parser.parse_args()
        ID=args['Id']
        #NAME=args['Name']
        cursor = conn.cursor()
        data=cursor.execute("select TRY_CAST(EmployeeID as Varchar) as EmployeeID,TRY_CAST(StaffID as Varchar) as StaffID,CAST(EmployeeName as Varchar) as EmpName,CAST(EmployeeCategory as Varchar) as EmployeeCategory,CAST(EmployeeStatus as Varchar) as EmployeeStatus,CAST(ResignedDate as Varchar) as ResignedDate,TRY_CAST(RepositoryShortName as Varchar) as Rank from com.Employee e left join com.REPOSITORY r on CAST(e.RankID as varchar)=cast(r.RepositoryID as varchar) where e.EmployeeId=?",ID)
        newlist=[]
        for i in data:
            newdict={"EmployeeID":i[0],"StaffID":i[1],"EmployeeName":i[2],"EmployeeCategory":i[3],"EmployeeStatus":i[4],"ResignedDate":i[5],"Rank":i[6]}
            newlist.append(newdict)
        return newlist

        

#adding endpoints for API
api.add_resource(Data, '/data')  # add endpoints
api.add_resource(Id, '/data/Id')  # add endpoints



    
#calling the main and runnning the whole code 
if __name__ == '__main__':
    application.run()  # run our Flask app
