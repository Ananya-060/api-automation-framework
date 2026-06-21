import requests


class APIS:
    BASE_URL="https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.header={"Content_type":"application/json"}


    def get(self,endpoint):
        url=f"{self.BASE_URL}/{endpoint}"
        response=requests.get(url,headers=self.header)
        return response

    def post(self, endpoint,new_data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url, headers=self.header,json=new_data)
        return response

    def put(self, endpoint,updated_data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.put(url, headers=self.header,json=updated_data)
        return response



    def delete(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.delete(url)
        return response








