### Date created
06 July 2020

### Project Title
Bay Wheels Jun - Jul 2020

by Livia Mendes

![1_citybike-artBike_v02__1_.png](https://images.ctfassets.net/q8mvene1wzq4/33jAW8nvXF2evwe2XRXBsA/ee8d023999f54ff16d95210ef4d63ff4/1_citybike-artBike_v02__1_.png?w=1000)
(source: Lift)

### Description
This project is part of Udacity's Data Analyst Nanodegree.

This project will explore the data for Bay Wheels(Ford GoBike) in the month of June 2020. The goal is to gain insights over this public bicycle sharing in the San Francisco Bay Area, California.

Bay Wheels is a regional public bicycle sharing system in the San Francisco Bay Area, California operated by Motivate in a partnership with the Metropolitan Transportation Commission and the Bay Area Air Quality Management District. Bay Wheels is the first regional and large-scale bicycle sharing system deployed in California and on the West Coast of the United States. It was established as Bay Area Bike Share in August 2013. As of January 2018, the Bay Wheels system had over 2,600 bicycles in 262 stations across San Francisco, East Bay and San Jose. On June 28, 2017, the system officially re-launched as Ford GoBike in a partnership with Ford Motor Company. After Motivate's acquisition by Lyft, the system was subsequently renamed to Bay Wheels in June 2019. The system is expected to expand to 7,000 bicycles around 540 stations in San Francisco, Oakland, Berkeley, Emeryville, and San Jose.

Source: Wikipedia (https://en.wikipedia.org/wiki/Bay_Wheels)

### File used
202006-baywheels-tripdata.csv

### Files

- readme.md
- exploration_bw_livia_mendes.ipynb
- exploration_bw_livia_mendes.py
- exploration_bw_livia_mendes.html
- slide_deck_bw_livia_mendes.ipynb
- slide_deck_bw_livia_mendes.html
- output_toggle.tpl
- trip_data_clean.csv
- 1_citybike-artBike_v02__1_.jpg

## Original Dataset information

Ride ID
Bicycle Type
Start time and date
End time and date
Starting station ID
Initial station name
Start station latitude
Starting station longitude
End station ID
End station name
Final station latitude
Final station longitude
User type

## Summary of Findings
**types of bikes**
There are 2 unique rideable types. The most commonly used by both casual and member users is the docked bike. Electric bikes are often use for going longer distances. The average distance of an electric bike is longer than a non-electric. Also, electric bikes are rented for a shorter period of time compared to a docked bike.

**start station and end stations**
There are 426 start stations, which makes it very difficult to plot. The most frequently used start station is Market St at 10th St.

There are 431 end stations, which also makes it very difficult to plot. The most frequently used end station is also Market St at 10th St.

However, the most popular route station is from El Embarcadero at Grand Ave to El Embarcadero at Grand Ave.

**type of user**
Most customers are casual, they use the service as needed without subscribing to a membership. There are 43470 casual customers. They represent almost 55% of users.

**running hours**
Casual and members seems to have a balanced usage of the system during the week days, while on weekends casual user seems to use the system more frequently. In the most early hours of the day, members are most active, probably going to work or school. While after 10 o'clock it seems that casual users become more active.The peak hours are within the rush hours (work and school times).

**days of the week**
The most popular day for renting a bike is Saturday, it is also when longer riding distances and duration are achieved.

**ride distance**
The average ridings distance is nearly 2km. On average members ride shorter distances than casuals. Only in the very early hours of day is that members ride longer distances than casuals.

**ride duration**
The mean travel time for rentals is 23 minutes. Casual riders seem to rent the bikes for longer periods of time then members. While members have a shorter, narrower trip distribution than the others.

## Key Insights for Presentation
In June, most of the users were casual representing a percentage of approx. 54% of the users.

Both groups of user often used docked bikes.

During the early hours of the day, members are most active, probably going to work or school. While after 10 o'clock casual users become more active. Casual and members have a balanced usage of the system during the weekdays, while on weekends casual users use the system more frequently.

In this month, casual users usually rode for longer periods of time and longer distances than members.

### Credits
Bikeshare information:
(https://www.lyft.com/bikes/bay-wheels/system-data)

Udacity (https://www.udacity.com/course/data-analyst-nanodegree--nd002)
