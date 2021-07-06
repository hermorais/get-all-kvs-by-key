import requests
import datetime
import time
import json
import sys
import csv

import sys

sys.stdout = open("search_hash.log", "w")
f = open("result.csv", "a")
inputFile = open("inputHash.txt", "r")

hash_list = inputFile.readlines()

hash_list_not_applied = []
hash_list_applied = []
hash_list_not_founded = []
hash_error = []

for hash_i in hash_list:

   print("Exec time: {}".format(datetime.datetime.now()))
   print("serching hash: {}".format(hash_i.strip()))

   url = "https://read-services-proxy.furycloud.io/applications/registration-api-go/kvs/services/shield-and-invitation-data/{}".format(hash_i.strip())

   headers = {
                "x-auth-token": "6ef00b0fc69e6ed17c12fceeab74cd73fea183a11704d577afa958c5f6dd40b0"
            }

   response = requests.get(url, headers = headers) 

   print("response.status_code: {}".format(response.status_code))
   print("response.text: {}".format(response.text))

   if response.status_code == 200:

      json_result = json.loads(response.text)
      
      if "user_id" in json_result:
         f.write("{};{}\n".format(hash_i.strip(), str(json_result["user_id"])))
         hash_list_applied.append(hash_i.strip())
      else:
         f.write("{};{}\n".format(hash_i.strip(), "NO USER"))
         hash_list_not_applied.append(hash_i.strip())
   elif response.status_code == 404:
      hash_list_not_founded.append(hash_i.strip())
   else:
      hash_error.append(hash_i.strip())

   print("----Sleeping 200 ms----")
   time.sleep(200 / 1000)
   print("-----------------------")

print("-----------------------")
print("HASH FOUNDED BUT NOT USER cantidad: {}".format(len(hash_list_not_applied)))
print("HASH FOUNDED BUT NOT USER: {}".format(str(hash_list_not_applied)))
print("-----------------------")
print("HASH FOUNDED cantidad: {}".format(len(hash_list_applied)))
print("HASH FOUNDED: {}".format(str(hash_list_applied)))
print("-----------------------")
print("HASH NOT FOUNDED cantidad: {}".format(len(hash_list_not_founded)))
print("HASH NOT FOUNDED: {}".format(str(hash_list_not_founded)))
print("-----------------------")
print("HASH ERROR cantidad: {}".format(len(hash_error)))
print("HASH ERROR: {}".format(str(hash_error)))

print("THE END!!!")
sys.stdout.close()
f.close()