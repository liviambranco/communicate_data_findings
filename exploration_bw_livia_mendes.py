#!/usr/bin/env python
# coding: utf-8

# # Bay Wheels Jun - Jul 2020
# ## by Livia Mendes

# <a id='intro'></a>
# 
# ## Introduction
# This project will explore the data for Bay Wheels(Ford GoBike). The goal is to gain insights over this public bicycle sharing in the San Francisco Bay Area, California.
# 
# Bay Wheels is a regional public bicycle sharing system in the San Francisco Bay Area, California operated by Motivate in a partnership with the Metropolitan Transportation Commission and the Bay Area Air Quality Management District. Bay Wheels is the first regional and large-scale bicycle sharing system deployed in California and on the West Coast of the United States. It was established as Bay Area Bike Share in August 2013. As of January 2018, the Bay Wheels system had over 2,600 bicycles in 262 stations across San Francisco, East Bay and San Jose. On June 28, 2017, the system officially re-launched as Ford GoBike in a partnership with Ford Motor Company. After Motivate's acquisition by Lyft, the system was subsequently renamed to Bay Wheels in June 2019. The system is expected to expand to 7,000 bicycles around 540 stations in San Francisco, Oakland, Berkeley, Emeryville, and San Jose.
# 
# Source: Wikipedia (https://en.wikipedia.org/wiki/Bay_Wheels)

# ## Table of Contents
# <ul>
# <li><a href="#wrangling">Preliminary Wrangling</a></li>
# <li><a href="#cleaning">Data Cleaning</a></li>
# <li><a href="#univariate">Univariate Exploration</a></li>
# <li><a href="#bivariate">Bivariate Exploration</a></li>
# <li><a href="#multivariate">Multivariate Exploration</a></li>
# </ul>

# <a id='wrangling'></a>
# ## Preliminary Wrangling

# In[1]:


# import all packages and set plots to be embedded inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


trip_data = pd.read_csv('/Users/macbook/Documents/udacity/findings/202006-baywheels-tripdata.csv')


# In[3]:


trip_data.shape


# In[4]:


trip_data.info()


# In[5]:


trip_data.sample(5)


# <a id='cleaning'></a>
# ## Data Cleaning

# I will better prepare the in order to be able to answer the posed questions.
# 
# - I will handle the cleaning missing values by removing or imputing them
# 
# - Drop unnecessary columns and rows
# 
# - Change data types to better support the analysis
# 
# - Replace unwanted characters
# 
# - Create and encode columns

# In[6]:


trip_data_clean = trip_data.copy()


# In[7]:


#check null values in each data set


# In[8]:


trip_data_clean.isnull().sum()


# In[9]:


#drop rows with missing values


# In[10]:


trip_data_clean = trip_data_clean.dropna()
trip_data_clean = trip_data_clean.reset_index(drop=True)


# In[11]:


trip_data_clean.isnull().sum()


# In[12]:


#check for duplicate entries


# In[13]:


sum(trip_data_clean.duplicated())


# In[14]:


#fix data types


# In[15]:


trip_data_clean.dtypes


# In[16]:


trip_data_clean['rideable_type'] = trip_data_clean['rideable_type'].astype('category')
trip_data_clean['member_casual'] = trip_data_clean['member_casual'].astype('category')


# In[17]:


trip_data_clean['start_station_id'] = trip_data_clean['start_station_id'].astype('str')
trip_data_clean['end_station_id'] = trip_data_clean['end_station_id'].astype('str')
trip_data_clean['ride_id'] = trip_data_clean['ride_id'].astype('str')


# In[18]:


trip_data_clean.info()


# In[19]:


#Change started_at and ended_at to datetime format


# In[20]:


from datetime import datetime
import calendar
import time


# In[21]:


trip_data_clean['started_at'] = pd.to_datetime(trip_data_clean['started_at'])
trip_data_clean['ended_at'] = pd.to_datetime(trip_data_clean['ended_at'])


# In[22]:


# Extract date, hour, day of week, and month information from the started_at


# In[23]:


trip_data_clean['month'] = trip_data_clean['started_at'].dt.month
trip_data_clean['day_of_week'] = trip_data_clean['started_at'].dt.weekday_name


# In[24]:


trip_data_clean['start_at_month'] = trip_data_clean['started_at'].dt.strftime('%B')


# In[25]:


trip_data_clean['start_hour'] = trip_data_clean['started_at'].dt.hour
trip_data_clean['end_hour'] = trip_data_clean['ended_at'].dt.hour


# In[26]:


trip_data_clean.sample(5)


# In[27]:


trip_data_clean['duration'] = trip_data_clean['ended_at'] - trip_data_clean['started_at']


# In[28]:


trip_data_clean['duration_sec'] = trip_data_clean['duration'].dt.seconds


# In[29]:


trip_data_clean['duration_minutes'] = trip_data_clean['duration_sec']/60


# In[30]:


trip_data_clean.sample(5)


# In[31]:


trip_data_clean.info()


# In[32]:


#create 'ride_distance' column from latitude and longitude


# In[33]:


# source of the code: Stackoverflow 
#(https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude)
from math import sin, cos, sqrt, atan2, radians

def distance (lat1,lon1,lat2,lon2):
    R = 6373.0
    
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return np.float64(round(1000*distance))


# In[34]:


trip_data_clean['ride_distance'] = trip_data_clean.apply(lambda row: distance(row['start_lat'],row['start_lng'],row['end_lat'],row['end_lng']),axis=1)


# In[35]:


#convert distance from meters to kilometers


# In[36]:


trip_data_clean['ride_distance_km'] = trip_data_clean['ride_distance']/1000


# In[37]:


trip_data_clean.info()


# In[38]:


trip_data_clean.sample(5)


# In[39]:


trip_data_clean.shape


# ### What is the structure of your dataset?
# 
# This dataset contains information from the start of the month of June to the start of the month of July 2020.
# 
# It has 22 columns and 79900 entries with information regarding bike trips.
# 
# The columns include information regarding the bikes rented such as when and where the rental started and ended, how long the ride was and some information about the costumer. 
# 
# ### What is/are the main feature(s) of interest in your dataset?
# 
# My interest is in exploring the bike trips patterns, such as where is the most commom begining and end station, what is the average duration of rides , at what time of the day more bikes are rented, what day of the week receives more rentals, what is the prefered type of ride, and who uses more this service subscribers or casual customers.
# 
# ### What features in the dataset do you think will help support your investigation into your feature(s) of interest?
# 
# duration, start and end station, start_day, start_hour, member_casual, rideable_type, ride_distance_km

# <a id='univariate'></a>
# ## Univariate Exploration

# **Let's start exploring the categorical variables**

# In[40]:


color_base = sns.color_palette()[0]


# In[41]:


#types of rides count


# In[42]:


sns.catplot(data=trip_data_clean, x='rideable_type', kind = 'count', color = color_base);


# In[43]:


#type of user count


# In[44]:


sns.catplot(data=trip_data_clean, x='member_casual', kind = 'count', color = color_base);


# In[45]:


#Number of rides per day of the week


# In[46]:


weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

sns.catplot(data=trip_data_clean, y='day_of_week', kind = 'count', color = color_base, order = weekday);


# In[47]:


#start hour


# In[48]:


sns.catplot(data=trip_data_clean, x='start_hour', kind = 'count', color = color_base);


# **Let's look at some statistics for our categorical variables**

# In[49]:


trip_data_clean.describe(exclude=[np.number])


# In[50]:


user_types_proportion =trip_data_clean['member_casual'].value_counts(normalize=True)*100

print(user_types_proportion)


# In[51]:


popular_ride = trip_data_clean['rideable_type'].mode()[0]

print('Most Popular Ride:', popular_ride)


# In[52]:


popular_day = trip_data_clean['day_of_week'].mode()[0]

print('Most Popular Start Day:', popular_day)


# In[53]:


popular_hour = trip_data_clean['start_hour'].mode()[0]

print('Most Popular Start Hour:', popular_hour)


# In[54]:


popular_start_station = trip_data_clean['start_station_name'].mode()[0]

print('Most Popular Start Station:', popular_start_station)


# In[55]:


popular_start_station = trip_data_clean['end_station_name'].mode()[0]

print('Most Popular End Station:', popular_start_station)


# In[56]:


#most frequent combination of start station and end station trip

trip_data_clean['Start and End Sations'] = trip_data_clean['start_station_name'] + ' ' + 'to' + ' ' + trip_data_clean['end_station_name']
popular_route = trip_data_clean ['Start and End Sations'].mode()[0]

print('The most popular route station is:', popular_route)


# ## FINDINGS
# 
# 
# **rideable_type**
# 
# There are 2 unique rideable types. The most commom is the docked bike. 
# 
# **start_station_name**
# 
# There are 426 start stations, which makes it very difficult to plot. The most frequently used start station is Market St at 10th St.
# 
# **end_station_name**
# 
# There are 431 end stations, which also makes it very difficult to plot. The most frequently used end station is also Market St at 10th St.
# 
# 
# However, the most popular route station is from El Embarcadero at Grand Ave to El Embarcadero at Grand Ave.
# 
# **member_casual**
# 
# Most customers are casual, they use the service as needed withou subscribing to a membership. There are 43470 casual customers. They represent almost 55% of users.
# 
# **start_hour**
# 
# The peak hours for the service are between 17:00 and 18:00. The most commom start hour is 17:00.
# 
# **day_of_week**
# 
# The most popular day for renting a bike is Saturday.

# **Now let's explore our numeric variables**

# In[57]:


trip_data_clean[['duration_minutes', 'ride_distance_km']].describe()


# In[58]:


average_distance = trip_data_clean['ride_distance_km'].mean()

print('The average distance (km) of a bike ride is:', average_distance)


# In[59]:


mean_travel_time = trip_data_clean['duration_minutes'].mean()
print('The mean travel time in minutes was:', round(mean_travel_time))


# In[60]:


plt.figure(figsize=[8, 5])
plt.hist(data = trip_data_clean, x = 'ride_distance_km')
plt.title('Distribution of Rides Distances')
plt.xlabel('Distance (KM)')
plt.ylabel('Number of Trips')
plt.show()


# In[61]:


plt.figure(figsize=[8, 5])
plt.hist(data = trip_data_clean, x = 'duration_minutes')
plt.title('Distribution of Ride Duration in Minutes')
plt.xlabel('Duration')
plt.ylabel('Number of Trips')
plt.show()


# Let's check the top precentile.

# In[62]:


trip_data_clean['duration_minutes'].describe(percentiles=[.95])


# In[63]:


bins = np.arange(1, 100, 1)
ticks = np.arange(0, 100, 10)
plt.hist(data=trip_data_clean, x='duration_minutes', bins=bins);
plt.xticks(ticks, ticks);
plt.xlabel('Trip Duration in Minute');


# From the graph it seems that most rides are short.

# In[64]:


#keep this data for further analysis


# In[65]:


trip_data_clean = trip_data_clean.query('duration_minutes <= 100')
trip_data_clean.info(null_counts=True)


# ## FINDINGS
# 
# **ride_distance_km**
# 
# Most customers ride a short distance. The average ridings distance is nearly 2km.
# 
# **duration_minutes**
# 
# There are outliers in this set. An user apperently rode for an entire day (24 hours).
# But after removing this outlier it is possible to see that most rides are short in terms of time too.

# ### Discuss the distribution(s) of your variable(s) of interest. Were there any unusual points? Did you need to perform any transformations?
# 
# > Most of the data was prepared for the analysis during the cleaning part, so no modifications were needed at this stage.
# 
# ### Of the features you investigated, were there any unusual distributions? Did you perform any operations on the data to tidy, adjust, or change the form of the data? If so, why did you do this?
# 
# > Most variables were within the expected distributions. The duration in minutes and even the distance had some outliers. The duration in minutes outlier was removed from our second plot so that we could see better the distribution of time per ride.

# In[66]:


# save the clean data to a .csv file


# In[67]:


trip_data_clean.to_csv('trip_data_clean.csv', index=False)


# <a id='bivariate'></a>
# ## Bivariate Exploration

# **In this section I will explore the behaviour of user types and compare them across our other variables of interest.**

# In[68]:


sns.countplot(data=trip_data_clean, x='member_casual', hue='rideable_type', color=color_base);
plt.xlabel('Bike Type');
plt.ylabel('Count');


# It seems that both casual and members have a preference for docked bike.

# In[69]:


sns.boxplot(data=trip_data_clean, x='rideable_type', y='ride_distance_km', color=color_base);
plt.xlabel('Bike Type');
plt.ylabel('Trip Distance in Kilometers');


# It appears that the average distance for a ride on an eletric bike is longer than a docked bike.

# In[70]:


sns.barplot(data=trip_data_clean, x='rideable_type', y='duration_minutes', color=color_base);
plt.xlabel('Bike Type');
plt.ylabel('Trip Duration in Minutes per Bike Type');


# It seems that docked bikes trips runs a little longer than eletric bikes.

# In[71]:


weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

graph = sns.catplot(data=trip_data_clean, x='day_of_week', col='member_casual', kind='count', sharey = True, color = color_base, order = weekday);

graph.set_axis_labels('Day of the Week', 'Number of Bike Trips');
graph.set_titles('{col_name}')
graph.set_xticklabels(rotation=45);


# Casual and members seems to have a balanced usage of the system during the week days, while on weekends casual user seems to use the system more frequently.

# In[72]:


sns.countplot(data=trip_data_clean, x='start_hour', hue='member_casual', color = color_base);
plt.xlabel('Hour of the Day');
plt.ylabel('Count');


# It seems that in the most early hours of the day, members are most active, probably going to work or school. While after 10 o'clock it seems that casual users become more active.

# In[73]:


sns.violinplot(data=trip_data_clean, x='member_casual', y='duration_minutes', color=color_base, inner='quartile');
plt.xlabel('Rider Type');
plt.ylabel('Trip Duration in Minutes');


# Casual riders seem to rent the bikes for longer periods of time then members. While members has a shorter, narrower trip distribution than the others.

# In[74]:


sns.boxplot(data=trip_data_clean, x='member_casual', y='ride_distance_km', color=color_base);
plt.xlabel('User Type');
plt.ylabel('Trip Distance in Kilometers');


# It seems that there is little difference between the average distance a casual user rides, compared to the distance ridden by a member. 

# In[75]:


plt.scatter(trip_data_clean['duration_minutes'], trip_data_clean['ride_distance_km'], alpha = 0.25, marker = '.' )
plt.title('Trip Distance and Duration')
plt.xlabel('Duration in Minutes')
plt.ylabel('Distance in Kilometers')
plt.show()


# In[76]:


samples = np.random.choice(trip_data_clean.shape[0], 10000, replace = False)
samp = trip_data_clean.loc[samples,:]

g = sns.PairGrid(data = samp, vars = trip_data_clean[['duration_minutes', 'ride_distance_km']], height = 4, aspect = 1.5)
g = g.map_diag(plt.hist, bins = 20);
g.map_offdiag(plt.scatter);


# This does not look like a linear relationship. Distance does not go much further than 8 km while trip times continue to go on.

# ### Talk about some of the relationships you observed in this part of the investigation. How did the feature(s) of interest vary with other features in the dataset?
# 
# > The analysis of user behavior between casual and member users, revealed that casual riders are most likely tourists or just people on a day off, since this type o user usually takes longer trips in terms of minutes and of distance, also their peak usage is during the weekends. On the other hand member users seem to use the bike service to commute to work or school and their rides are mostly for shorter periods of time and distances. They rent the bikes mainly on week days at times that match those of start of school and work and the end of those activities.
# 
# > When it comes to bike types, it seems that both casual and members have a preference for docked bike. Also, eletric bikes go for longer distances, while docked bikes run for longer periods of time. This could be explained by the fact that eletric bikes may go faster, so the go farther in less time then the docked bikes.
# 
# ### Did you observe any interesting relationships between the other features (not the main feature(s) of interest)?
# 
# > I would expect that the time of the ride and the distance has a more linear relationship. But it seems this is not the case here.

# <a id='mulivariate'></a>
# ## Multivariate Exploration
# 
# > In this section I will continue to examine user type behaviour across other variables.

# In[77]:


f, ax = plt.subplots(figsize=(10, 8))
corr = trip_data_clean.corr()
sns.heatmap(corr, cbar = True, annot=True, square = True, fmt = '.2f', xticklabels=corr.columns.values, yticklabels=corr.columns.values);


# The correlation map above does not indicate any interesting relationship between the numeric variables in our dataset.

# In[78]:


weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

sns.pointplot(data=trip_data_clean, x='day_of_week', y='ride_distance_km', hue='member_casual', dodge=0.3, linestyles='', color=color_base, order = weekday);
plt.xlabel('Day of Week');
plt.ylabel('Avg. Trip Distance in Kilometers');
plt.xticks(rotation=45);


# Here we see again that casual users tend to ride for longer distances than subscribers. Saturday is the day in which longer distances are achieved.

# In[79]:


weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

sns.pointplot(data=trip_data_clean, x='day_of_week', y='duration_minutes', hue='member_casual', dodge=0.3, linestyles='', color=color_base, order = weekday);
plt.xlabel('Day of Week');
plt.ylabel('Avg. Trip Duration in Minutes')
plt.xticks(rotation=45);


# This graph confirms that members usually ride for shorter periods of time and that on the Saturday the trip duration increases.

# In[80]:


weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

sns.pointplot(data=trip_data_clean, x='day_of_week', y='duration_minutes', hue='rideable_type', dodge=0.3, linestyles='', color=color_base, order = weekday);
plt.xlabel('Day of Week');
plt.ylabel('Avg. Trip Duration in Minutes')
plt.xticks(rotation=45);


# Docked bikes are ridden by longer periods of time every day of the week.

# In[81]:


weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

sns.pointplot(data=trip_data_clean, x='day_of_week', y='ride_distance_km', hue='rideable_type', dodge=0.3, linestyles='', color=color_base, order = weekday);
plt.xlabel('Day of Week');
plt.ylabel('Avg. Trip Distance in Kilometers')
plt.xticks(rotation=45);


# Eletric bikes are ridden by longer distances every day of the week.

# In[82]:


sns.pointplot(data=trip_data_clean, x='start_hour', y='ride_distance_km', hue='member_casual', linestyles='', color=color_base);
plt.xlabel('Hour of the Day');
plt.ylabel('Avg. Trip Distance in Kilometers');


# Members ride longer distances in the very early hours of the day only.

# In[83]:


sns.pointplot(data=trip_data_clean, x='start_hour', y='duration_minutes', hue='member_casual', linestyles='', color=color_base);
plt.xlabel('Hour of the Day');
plt.ylabel('Avg. Trip Duration in Minutes');


# Members ride less minutes in all hours of the day.

# ### Talk about some of the relationships you observed in this part of the investigation. Were there features that strengthened each other in terms of looking at your feature(s) of interest?
# 
# > The multivariate exploration strengthened the behavior patterns uncovered in both univariate and bivariate exploration. Members tend to use more the service on week days and during rush hours. Their trips are likely to be commuting to work or school and are shorter in both time and distance. On the other hand, the casual user seems to use the bike more for leisure purposes. They start to ride more after 10 am and ride all day long ride for longer distances and for longer periods of time.
# 
# ### Were there any interesting or surprising interactions between features?
# 
# >  There was no big surprise in the data gathered. Perhaps an interesting fact is that casual and Member users seem to prefer non-electric bike. Although it is not clear from this data if this is a choice or if there are less electric bikes available for use. Even so, from this data it was possible to gather that electric bikes seem to be the bikes of choice for longer distances.
