#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install pyspellchecker')


# In[6]:


get_ipython().system('pip install pattern')
get_ipython().system('pip install autocorrect')
get_ipython().system('pip install textblob')
get_ipython().system('pip install textdistance')


# In[7]:


from spellchecker import SpellChecker
spell=SpellChecker()
misspell_word=input("enter the word")
correct_word=spell.correction(misspell_word)
print(f"correct word for '{misspell_word}' is '{correct_word}' is:")
misspell_word="outo"
suggestions=spell.candidates(misspell_word)
print(f"the suggest words are {suggestions}:")

