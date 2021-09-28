#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[4]:


from flask import Flask,render_template,request
import smtplib
summ=Flask(__name__)
@summ.route('/')
def first():
    return render_template('sum.html')
@summ.route('/sum',methods=['GET','POST'])
def send_mail():
    if(request.method=="POST"):
        val=request.form['a']
        val1=request.form['gender']
        val2=request.form['course']
        val3=request.form['mail']
        val4=request.form['phone']
        m=smtplib.SMTP_SSL('smtp.gmail.com',465)
        m.login('pythontech39@gmail.com','python@1234')
        m.sendmail('pythontech39@gmail.com',val3,'Hello {0}\n Your request has been submitted for the course {1}\n Team HR'.format(val,val2))
        m.close()
	return render_template('sum.html')
if __name__=='__main__':
    summ.run()


# In[ ]:




