import requests
import json
import os
import glob
from tabulate import tabulate

apiKey = os.environ["API_KEY"]
region = "ap-southeast-2"
# path = "plan/**"
path = ""

files = [f for f in glob.glob(path + "plan.json", recursive=True)]

endpoint = "https://" + region + "-api.cloudconformity.com"
url = endpoint + "/v1/template-scanner/scan"

headers = {
    "Content-Type": "application/vnd.api+json",
    "Authorization": "ApiKey " + apiKey,
}
table_array = []
if files:
    for file in files:
        with open(file) as fp:
            for line in fp:
                payload = {
                    "data": {
                        "attributes": {"type": "terraform-template", "contents": line}
                    }
                }
                resp = requests.post(url, headers=headers, data=json.dumps(payload))
                resp_json = resp.json()
                if "data" in resp_json:
                    for d in resp_json["data"]:
                        if (
                            "attributes" in d
                            and "status" in d["attributes"]
                            and d["attributes"]["status"] == "FAILURE"
                        ):
                            column_array = []
                            column_array.append(d["attributes"]["message"])
                            column_array.append(d["attributes"]["risk-level"])
                            table_array.append(column_array)
    print(tabulate(table_array, headers=["Type", "Risk Level"], tablefmt="orgtbl"))
else:
    print("No plan json to process")
