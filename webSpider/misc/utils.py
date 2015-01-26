import time
from datetime import date,timedelta
import datetime
class Utils:
	"""docstring for Utils"""
	
	@staticmethod
	def str_to_timestamp_by_format(date,format='%B %d, %Y'):
		return int("%d" % time.mktime(time.strptime(date, format)))
	
	@staticmethod
	def timestamp_to_str_by_format(timestamp,format='%Y-%m-%d %H:%M:%S'):
		return time.strftime(format, time.localtime(int(timestamp)))

	@staticmethod
	def timestamp_to_datetime_by_format(timestamp,format='%Y-%m-%d %H:%M:%S'):
		return datetime.datetime.fromtimestamp(timestamp)