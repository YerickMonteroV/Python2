from api import *
from ids import elem
import time

user_ids = elem

star_time=time.time()
for user_id in user_ids:
    
    result = getOneUser(user_id)
    print(result)

duration=time.time()-star_time
print(duration)