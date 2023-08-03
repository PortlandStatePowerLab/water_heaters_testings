import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline

# importing csv file
df = pd.read_csv('idle_test.csv', header=None)
df = df.dropna(thresh=2) # drops lines with '0'
error_bad_lines=False

#delete unnecessary data columns. adjust these column values depending on the delivered log.csv data
df.drop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12,14], axis=1, inplace=True)

# extract time data and converts to datetime
df.insert(1, 'Time', pd.to_datetime(df[0]))
df['Time'] = df['Time'].dt.strftime('%H:%M:%S')

# delete original timestamp data
df.drop([0], axis=1, inplace=True)

# convert to numpy array

wd = np.array(df)

# create axis variables
Time = wd[:,0]
EnergyTake = wd[:,1]
Current = wd[:,2]/240 # current = power_column/voltage

# create fig and ax objects
fig, ax1 = plt.subplots(1,1,figsize=(10,8))
ax2 = ax1.twinx()


# plot the values
ax1.plot(Time, EnergyTake)
ax2.plot (Time, Current, 'r--')


# set the labels
ax1.set_title('EnergyTake and Current vs Time')
ax1.set_xlabel('Timestamp (H:M:S)')
ax1.set_ylabel('EnergyTake (Wh)')
ax2.set_ylabel('Current (A)')


# set axis ticks
ax1.xaxis.set_major_locator(plt.MaxNLocator(25)) # set number of ticks on x-axis
ax1.yaxis.set_major_locator(plt.MaxNLocator(15)) # set number of ticks on y1-axis
ax2.yaxis.set_major_locator(plt.MaxNLocator(15)) # set number of ticks on y2-axis
ax1.set_ylim(ymin=0)
ax2.set_ylim(ymin=0) # forces current axis to start from 0
fig.legend(['EnergyTake','Current'])

ax1.tick_params(axis='x', labelrotation=45)

#fig.autofmt_xdate(rotation=90) # rotate x-axis data
ax1.grid()


# display and save the plot
plt.tight_layout()
plt.savefig('wh_data.jpg', dpi=95, bbox_inches='tight') # change save file name and size of graph
plt.show()
