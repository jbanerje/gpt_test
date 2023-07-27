from flask import Flask, render_template, request, jsonify
from infer_user_query import *
import os

app = Flask(__name__)
print(os.getcwd())
@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=['GET', 'POST'])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_chat_response(input)

def get_chat_response(text):
    
    user_query          = text
    chain               = create_chain_from_embedding()
    
    if text:
        response        = get_response_from_gpt(chain, user_query)
    else:
        response        = "Ask me anything!"
    
    return response
            
if __name__ == '__main__':
   app.run()