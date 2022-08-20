import requests

def predict(external_request):
    headers = {}

    external_request = external_request.json
    data = external_request['data']

    headers = {
      'Content-Type': 'application/json',
    }

    json_data = {"columns": ["size", "fuel", "distance", "desibel", "airflow", "frequency"], "data": data}

    response = requests.post('http://your_vm_public_ip:5000/invocations', headers=headers, json=json_data)

    return str(response.text)