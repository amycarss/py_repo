
import requests
import json
NYT_KEY ="9a9e735727d34d8687de1862420929bf"
# What's the base url?

# Build your parameters dictionary.
baseurl="https://api.nytimes.com/svc/search/v2/articlesearch.json"
params_d={}
params_d['api-key'] =NYT_KEY
params_d["q"]='query'
#can compare to code examples to see how to handle the way album is nested beneath entity, can do some trial and error, stick in in a borwser and see if it outputs anything
# Input the parameters to the get function in requests
resp_obj=requests.get(baseurl, params=params_d)#response object
# Access the text attribute of the response object
text_str=resp_obj.text
# Load the string into a Python list or dictionary
py_diction=json.loads(text_str)#walked through this much in class, what's below may not be correct
## Part 2:
# Dump the Python object to a JSON-formatted string
jsn_str=json.dumps(py_diction)
# Open a file for writing
f=open('monae_data.json','w')
# Write the JSON-formatted string to the file
f.write(jsn_str)
f.close()
# Close the file
print(py_diction)
