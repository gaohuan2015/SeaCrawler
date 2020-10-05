import netCDF4
from netCDF4 import Dataset
nc_obj=Dataset('Data/25_5_99_100_1992-12-31.nc')
print(nc_obj)
print('---------------------------------------')

#查看nc文件中的变量
print(nc_obj.variables.keys())
for i in nc_obj.variables.keys():
    print(i)
print('---------------------------------------')

print(nc_obj.variables['lat'])
print(nc_obj.variables['lon'])
print(nc_obj.variables['depth'])
print('---------------------------------------')