
# coding: utf-8

# In[1]:


# Exploring Gun Related Fatalities in the US


# In[2]:


import csv
d = open('guns.csv','r')
data = list(csv.reader(d))
headers = data[0]
print(headers)
print(data[1])
data = data[1:]


# In[3]:


## Exploring Gun Deaths by Year
### There is very little differences in gun deaths from year to year


# In[4]:


year = []
for val in data:
    year.append(val[1])
year_counts = {}
for yea in year:
    if yea in year_counts:
        year_counts[yea] += 1
    else:
        year_counts[yea] = 1
print(year_counts)


# In[5]:


## Extracting Gun Deaths by Month Regardless of Year
### The number of gun deaths per month seems to increase slightly beginning May and ending in September.


# In[6]:


import datetime
dates = [datetime.datetime(year = 1,month = int(val[2]),day = 1)for val in data]


# In[7]:


date_counts = {}
for val in dates:
    if val in date_counts:
        date_counts[val] += 1 
    else:
        date_counts[val] = 1
date_counts


# In[8]:


## Extracting Gun Deaths in Reference to Month and Year
### This breakdown of data provides additional evidence that the amount of deaths by gun increases during the summer months


# In[9]:


full_date_counts = {}
dates = [datetime.datetime(year = int(val[1]),month = int(val[2]),day = 1)for val in data]
for date in dates:
    if date in full_date_counts:
        full_date_counts[date] += 1
    else:
        full_date_counts[date] = 1
full_date_counts


# In[10]:


## Death by Guns by Gender
### We see that males are most affected when it comes to gun deaths


# In[11]:


def sex(data):
    sex_counts = {}
    for val in data:
        if val[5] in sex_counts:
            sex_counts[val[5]] += 1
        else:
            sex_counts[val[5]] = 1
    return sex_counts
sex_count = sex(data)
sex_count


# In[12]:


## Counting Gun Deaths by Race
### This breakdown is slightly skewed since the population for each race is different.
### In order to meaningfully compare these values we import census data so that we can see the 
### amount of death's per 100,000 people for a given race.
### I used the formula:  (# of Deaths for a Race/total pop for a Race) * 100,000
### Mapping counts the total population for each race group.


# In[13]:


d = open('census.csv','r')
census = list(csv.reader(d))
header = census[0]
impo_header = header[10:]
d = census[1]
census_data = d[10:]

mapping = {}
mapping['Asian/Pacific Islander'] = census_data[4]+census_data[5]
mapping['Black'] =census_data[2]
mapping['Native American/Native Alaskan']=census_data[5]
mapping['Hispanic'] = census_data[1]
mapping['White'] = census_data[0]


def race_per_hund(data):
    race_counts = {}
    for val in data:
        if val[7] in race_counts:
            race_counts[val[7]] += 1
        else:
            race_counts[val[7]] = 1
    race_per_hundredpk = {}
    for val in mapping:
        for race in race_counts:
            if val == race:
                race_per_hundredpk[val] = int(race_counts[race])/int(mapping[race])*100000
    return race_per_hundredpk
all_data = race_per_hund(data)
all_data


# In[14]:


### Counts the amount of deaths that were due to homicide by race,
### and we must once again convert these numbers to provide a better comparison.


# In[15]:


intents = [val[3]for val in data]
races = [val[7]for val in data]
def homicide_race(intents,races):
    homicide_race_counts = {}
    for idx,val in enumerate(races):
        if val not in homicide_race_counts:
            homicide_race_counts[val] = 0
        if intents[idx] == 'Homicide':
            homicide_race_counts[val]+=1
    return homicide_race_counts
homicide_race_counts = homicide_race(intents,races)
homicide_race_counts


# In[16]:


### The Homicide values represent the amount of homicides per 100,000 people for a given race.


# In[59]:


def homi_hundred(homicide_race_counts):
    homicide = {}
    for key,value in homicide_race_counts.items():
        homicide[key] = int(value)/int(mapping[key]) * 100000
    return homicide    
homicide_all = homi_hundred(homicide_race_counts)
homicide_all


# In[18]:


## Counting the Amount of Deaths by Education
### 1 = Less than High School
### 2 = Graduated High School
### 3 = Some College
### 4 = At least graduate College
### 5 = Not available 


# In[19]:


education = {}
for val in data:
    if val[10] not in education:
        education[val[10]] = 1
    else:
        education[val[10]]+=1
education


# In[20]:


## Exploring Gun Suicides by Race
### Suicides per 100,000 people by Race


# In[33]:


def suicide_race(races,intents):
    suicide_by_race = {}
    for idx,val in enumerate(races):
        if val not in suicide_by_race:
            suicide_by_race[val] = 0
        if intents[idx] == 'Suicide':
            suicide_by_race[val] +=1
    suicide_per_hunk = {}
    for key,value in suicide_by_race.items():
        suicide_per_hunk[key] = int(value)/int(mapping[key])*100000
    return suicide_per_hunk
suicide_per_hundredk = suicide_race(races,intents)


# In[22]:


## Counting Gun Deaths by Age 


# In[34]:


def age_deaths(data):
    age_count = {}
    ages = [val[6]for val in data]
    for age in ages:
        if age in age_count:
            age_count[age] += 1
        else:
            age_count[age] = 1
    age_range = {}
    age_range['0-18'] = 0
    age_range['19-29'] =0
    age_range['30-39']=0
    age_range['40-49']=0
    age_range['50-59']=0
    age_range['60-69']=0
    age_range['70-79']=0
    age_range['80-89']=0
    age_range['90+']=0
    for key,value in age_count.items():
        if key == 'NA':
            key = 0
        key = int(key)
        if key <= 18:
            age_range['0-18'] = age_range['0-18'] + value
        if key > 18 and key <= 29:
            age_range['19-29'] = age_range['19-29'] + value
        if key > 29 and key <= 39:
            age_range['30-39'] = age_range['30-39'] + value
        if key > 39 and key <= 49:
            age_range['40-49'] = age_range['40-49'] + value
        if key > 49 and key <= 59:
            age_range['50-59'] = age_range['50-59'] + value
        if key > 59 and key <=69:
            age_range['60-69'] = age_range['60-69'] + value
        if key > 69 and key <= 79:
            age_range['70-79'] = age_range['70-79'] + value
        if key > 79 and key <= 89:
            age_range['80-89'] = age_range['80-89'] + value
        if key > 89:
            age_range['90+'] = age_range['90+'] + value
    return age_range
all_age_range = age_deaths(data)


# In[24]:


## Looking at All Data for the Year 2012


# In[27]:


data_2012 = []
for val in data:
    if val[1] == '2012':
        data_2012.append(val)
intents_2012 = []
races_2012 = []
for val in data:
    if val[1] == '2012':
        intents_2012.append(val[3])
        races_2012.append(val[7])


# In[52]:


sex_2012 = sex(data_2012)
sex_2012


# In[53]:


raceperhun_2012 = race_per_hund(data_2012)
raceperhun_2012


# In[54]:


homicide_by_race_2012 = homicide_race(intents_2012,races_2012)
homicide_by_race_2012


# In[60]:


homicide_by_raceperhundk_2012 = homi_hundred(homicide_by_race_2012)
homicide_by_raceperhundk_2012


# In[61]:


suicide_by_raceperhundk_2012 = suicide_race(races_2012,intents_2012)
suicide_by_raceperhundk_2012


# In[62]:


age_group_2012 = age_deaths(data_2012)
age_group_2012


# In[63]:


## Looking at all Data for 2013


# In[64]:


data_2013 = []
for val in data:
    if val[1] == '2013':
        data_2013.append(val)
intents_2013 = []
races_2013 = []
for val in data:
    if val[1] == '2013':
        intents_2013.append(val[3])
        races_2013.append(val[7])


# In[65]:


sex_2013 = sex(data_2013)
sex_2013


# In[66]:


raceperhun_2013 = race_per_hund(data_2013)
raceperhun_2013


# In[67]:


homicide_by_race_2013 = homicide_race(intents_2013,races_2013)
homicide_by_race_2013


# In[68]:


homicide_by_raceperhundk_2013 = homi_hundred(homicide_by_race_2013)
homicide_by_raceperhundk_2013


# In[69]:


suicide_by_raceperhundk_2013 = suicide_race(races_2013,intents_2013)
suicide_by_raceperhundk_2013


# In[70]:


age_group_2013 = age_deaths(data_2013)
age_group_2013


# In[71]:


## Looking at all Data for 2014


# In[72]:


data_2014 = []
for val in data:
    if val[1] == '2014':
        data_2014.append(val)
intents_2014 = []
races_2014 = []
for val in data:
    if val[1] == '2014':
        intents_2014.append(val[3])
        races_2014.append(val[7])


# In[73]:


sex_2014 = sex(data_2014)
sex_2014


# In[74]:


raceperhun_2014 = race_per_hund(data_2014)
raceperhun_2014


# In[75]:


homicide_by_race_2014 = homicide_race(intents_2014,races_2014)
homicide_by_race_2014


# In[76]:


homicide_by_raceperhundk_2014 = homi_hundred(homicide_by_race_2014)
homicide_by_raceperhundk_2014


# In[77]:


suicide_by_raceperhundk_2014 = suicide_race(races_2014,intents_2014)
suicide_by_raceperhundk_2014


# In[78]:


age_group_2014 = age_deaths(data_2014)
age_group_2014

