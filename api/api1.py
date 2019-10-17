from app import url

import requests

class api_hrm:

    def logon_api(self, session, mobile, password):
        date1 = {"mobile": mobile, "password": password}
        response = session.post(url + 'login', json=date1)
        return response

    # def add_api(self, session, token, name, phone,
    #             timeOfEntry, formOfEmployment, workNumber, departmentName, departmentId, correctionTime):
    #     date = {"username": name, "mobile": phone, "timeOfEntry": timeOfEntry, "formOfEmployment": formOfEmployment,
    #             "workNumber": workNumber,
    #             "departmentName": departmentName,
    #             "departmentId": departmentId,
    #             "correctionTime": correctionTime}
    #     head = {"Authorization": "Bearer " + token}
    #     response = session.post(url + 'user', json=date, headers=head)
    #     return response

    def add_api1(self, session, token):
        date = {"username": "勒布朗科比","mobile": "12666626665","timeOfEntry": "2019-10-01","formOfEmployment": 1,"workNumber": "13145201111","departmentName": "财务部","departmentId": "1066238836272664576","correctionTime": "2019-12-31T16:00:00.000Z"}
        head = {"Authorization": "Bearer " + token}
        response = session.post(url + 'user', json=date, headers=head)
        return response

    def select_api(self,session,id1,token):
        head = {"Authorization": "Bearer " + token}
        response = session.get(url + 'user/'+id1,headers=head)
        return response

    def update_api(self,session,id1,token):
        head = {"Authorization": "Bearer " + token}
        dete = {"username":"软件测试彭于晏"}
        response = session.put(url+'user/'+id1, headers=head,json=dete)
        return response

    def delete_api(self,session,id1,token):
        head = {"Authorization": "Bearer " + token}
        response=session.delete(url+'user/'+id1,headers=head)
        return response
