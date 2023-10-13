# Reported Approach

In the Reported Approach folder, you will find several folders. The mains one are :
- data folder is the folder where we stored all the data we got from the performance measures. All the data in this folder have been splited by scenario case (consumer scaling, producer scaling, message size scaling, frequency of sending message [size] scaling)
- instruction folder is the folder with all the scenarios tutorials
- script folder is the folder with the parsing and mean calculation for the pre-process, plot scripts and tentative of automation (automated-testing.ps1)


## Steps of the process to plot the data
### Create container
- docker-compose -f docker-compose.yml up -d

### Pre-process data
Use the data in data folder, copy paste the file in magic.txt to calculate the mean of the file.

Then add the mean value to the corresponding plot script in the Scripts folder

### Plot
Execute the plot script in the Scripts folder