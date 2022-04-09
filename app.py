#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template
import joblib


# In[2]:


app = Flask(__name__)


# In[3]:


@app.route("/", methods = ["GET", "POST"])
def i():
    if request.method == "POST":
        inc = float(request.form.get("income"))
        print(inc)
        aged = float(request.form.get("age"))
        print(aged)
        loa = float(request.form.get("loan"))
        print(aged)
        cart_model = joblib.load("tree")
        rf_model = joblib.load("forest")        
        xgb_model = joblib.load("CRE")
        
        cart_pred = cart_model.predict([[inc,aged,loa]])
        rf_pred = rf_model.predict([[inc,aged,loa]])
        xgb_pred = xgb_model.predict([[inc,aged,loa]])

        return(render_template("index.html",result1 = cart_pred, result2 = rf_pred, result3 = xgb_pred))
    else:
        return render_template("index.html", result ="GET METHOD")


# In[ ]:


if __name__=="__main__":
  app.run()


# In[ ]:




