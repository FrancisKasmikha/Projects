num_str3 = input('Input rods: ')
#Where you input the rods
float3 = float(num_str3)
print('You input', float3, 'rods.')
#the output of how many rods you entered

print('Conversions')
#telling you that these are the conversions

rods_meters = float3 * 5.0292
print('Meters:',round(rods_meters,3))
#Converting the rods to meters
rods_feet = float3 * 16.5
print('Feet:', round(rods_feet,3))
#converting the rods to feet
rods_miles = float3 * .0031250078
print('Miles:',round(rods_miles,3))
#Converting the rods to miles
rods_furlongs = float3 * .025
print('Furlongs:', round(rods_furlongs,3))
#Converting the rods to furlongs
rods_walk = float3 / 16.53329224
print('Minutes to walk',float3, 'rods:', round(rods_walk,3))
#time to walk 1 rod




