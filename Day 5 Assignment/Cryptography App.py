#!/usr/bin/env python
# coding: utf-8

# In[1]:


from cryptography.fernet import Fernet


# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:


get_ipython().system('pip install cryptography')


# In[2]:


from cryptography.fernet import Fernet


# In[19]:


def genratingpasskey():
    key= Fernet.generate_key()
    print(key)
    print(type(key))
    someone= open("Importantthing.key", 'wb')
    someone.write(key)
    someone.close()


# In[ ]:





# In[21]:


def getmypaskey():
    someone= open("Importantthing.key",'rb')
    return someone.read()
    


# In[ ]:





# In[23]:


def getContentFromUser():
    return input("Enter the data that you want to Encrypt in your python Script:")


# In[ ]:





# In[ ]:





# In[41]:


def encryptMessage(message_normal):
    key = getmypaskey()
    k = Fernet(key)
    encrypted_Message = k.encrypt(message_normal)
    return encrypted_Message


# In[42]:


def decryptMessage(message_secret):
    key = getmypaskey()
    k = Fernet(key)
    decrypted_Message = k.decrypt(message_secret)
    return decrypted_Message


# In[43]:


genratingpasskey()


# In[44]:


data = getContentFromUser()
encryptedcode= encryptMessage(data.encode('utf-8'))


# In[45]:


encryptedcode


# In[46]:


decryptMessage(encryptedcode)


# In[ ]:





# In[ ]:




