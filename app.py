from flask import Flask, render_template,request
app = Flask(__name__) 
from gensim.summarization import keywords
import pandas as pd
import re

@app.route('/ho')   
def home():
    return render_template('index.html')  
@app.route('/') 
def index():
    return render_template('inde.html')  

@app.route('/final',methods=['POST','GET'])
def final():
    v=request.form["speechToText"]
    t=request.form["cta"]
    text=v
    keys=keywords(text, words=3)
    keys=re.split(" ", keys)
    print(keys)
    li=pd.read_csv(r"C:\Users\Dell\aditi\anaconda-jupyter-notebooks\MHSCC#Hackathon\ifp.csv")
    cta=t
    keyword = keys
    print(keyword)
    l=[list(li["CTA"]),list(li["Keywords"]),list(li["Statements"])]
    result=[]
    for i in range(len(li["CTA"])):
        if(l[0][i]==cta.lower()):
            temp=l[1][i].split(",")
            t1=set(keyword)
            t2=set(temp)
            if(t1.intersection(t2)):
                result.append(l[2][i])
    for i in result:
        print(i)

    return render_template('inde.html',v=result)   

if __name__ =='__main__':  
    app.run(debug = True)  