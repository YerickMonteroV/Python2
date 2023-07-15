from concurrent.futures import ThreadPoolExecutor
from api import *
from ids import elem
import time

user_ids = elem

start_time = time.time()

with ThreadPoolExecutor() as executor:
    results = executor.map(getOneUser, user_ids)
    for result in results:
        print(result)

duration = time.time() - start_time
print(duration)
