#!/usr/bin/env python
# coding: utf-8

# In[68]:


import csv


# In[59]:


class Astronaut:
    def __init__(self, name, space_flight_hrs, status):
        self.__name = name
        self.__space_flight_hrs = int(space_flight_hrs)
        self.__status = status
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
        
    @property
    def space_flight_hrs(self):
        return self.__space_flight_hrs
    @space_flight_hrs.setter
    def space_flight_hrs(self, new_hrs):
        self.__space_flight_hrs = new_hrs
    
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, new_status):
        self.__status = new_status
        
    def __str__(self):
        return f"{self.__name}, {self.__status}"
    
    def __gt__(self, other):
        print(f"Self: {self.__name}, Other: {other.__name}")
        if self.__space_flight_hrs > other.__space_flight_hrs:
            print(f"{self.__name} > {other.__name}")
            return True
        else:
            print(f"{self.__name} < {other.__name}")
            return False
        
    def __ge__(self, other):
        print(f"Self: {self.__name}, Other: {other.__name}")
        if self.__space_flight_hrs >= other.__space_flight_hrs:
            print(f"{self.__name} >= {other.__name}")
            return True
        else:
            print(f"{self.__name} <= {other.__name}")
            return False
        
    def __eq__(self, other):
        print(f"Self: {self.__name}, Other: {other.__name}")
        if self.__space_flight_hrs == other.__space_flight_hrs:
                print(f"{self.__name} == {other.__name}")
                return True
        else:
            print(f"{self.__name} != {other.__name}")
            return False
        


# In[64]:


astro1 = Astronaut('Buzz Aldrin', 8000, 'Retired')
astro2 = Astronaut('Buzz Lightyear', 8000, 'Active')


# In[65]:


print(astro1)


# In[66]:


astro2 < astro1


# In[67]:


astro1 == astro2


# In[70]:


with open('astronauts.csv', 'r')as file:
    rd = [{x: y for x, y in row.items()} for row in csv.DictReader(file, skipinitialspace = True)]
    file.close()


# In[74]:


filtered_list = [{'name': x['Name'], 'flight_time_hrs': x["Space Flight (hr)"], 'status': x['Status']} for x in rd]


# In[76]:


astronaut_list = []
for astro in filtered_list:
    astronaut_list.append(Astronaut(astro['name'], astro['flight_time_hrs'], astro['status']))


# In[78]:


vars(astronaut_list[0])


# In[79]:


astronaut_list[4] > astronaut_list[9]


# In[80]:


for x in astronaut_list:
    print(x)

