#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install vectorbt


# In[35]:


pip install pandas 


# In[36]:


import pandas as pd


# In[32]:


import vectorbt as vbt 


# In[50]:


import datetime
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days =3)


# In[52]:


import vectorbt as vbt
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days =3)


# Download the data with a specified start date
btc_price = vbt.YFData.download(['BTC-USD', 'ETH-USD', 'XMR-USD', 'ADA-USD'],interval = '1m',start = start_date,end = end_date,missing_index='drop').get('Close')

# Print the data
print(btc_price)


# In[53]:


rsi = vbt.RSI.run(btc_price, window = 14)

entries = rsi.rsi_crossed_below(30)
exits = rsi.rsi_crossed_above(70)

pf = vbt.Portfolio.from_signals(btc_price, entries,exits)
#pf.plot().show()
print(pf.total_return())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




