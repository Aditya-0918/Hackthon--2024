
import google.generativeai as genai
#ximport os
api_key ='AIzaSyBsG4xJpT0CGAgnCb9-rLYdERyAzRUG3gE'
if api_key:
    genai.configure(api_key=api_key)
else:
    print("API_KEY environment variable is not set.")
    
    



