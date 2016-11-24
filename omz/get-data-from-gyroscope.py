# coding: utf-8

# @omz

# @Gyroscope Raw Data

# https://forum.omz-software.com/topic/3030/get-data-from-objc_util-__structure/3

# Structure classes that are auto-generated by objc_util use the lowercase alphabet for their field names, i.e. the first field is named a, the second b, etc.

# If you want to access the fields with their original names, you have to define a subclass of ctypes.Structure and pass that as the optional restype keyword argument of an ObjC method call. Here's an example of that:

from objc_util import *
from ctypes import Structure, c_double
import time

class CMRotationRate (Structure):
	_fields_ = [('x', c_double), ('y', c_double), ('z', c_double)]
	
CMMotionManager = ObjCClass('CMMotionManager')
mgr = CMMotionManager.alloc().init()
try:
	mgr.startGyroUpdates()
	for i in range(10):
		time.sleep(1)
		gyro_data = mgr.gyroData()
		if not gyro_data:
			print('data not available (yet?)')
			continue
		# Using the custom struct here:
		rate = gyro_data.rotationRate(argtypes=[], restype=CMRotationRate)
		# You can now access the struct's fields as x, y, z:
		print(rate.x, rate.y, rate.z)
finally:
	mgr.stopGyroUpdates()
	mgr.release()
	
# --------------------
