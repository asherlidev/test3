from glob import glob
import imp
import requests
import aiohttp
import asyncio
from decouple import config
from extern import retr_web_soc
ADDRESS=config('ADDRESS')
prefix = 'https://apilist.tronscan.org/api/transaction?sort=-timestamp&count=true'
import time
start_time_stamp=""
end_time_stamp=""
start = False
def get_time_stamp():
    time_stamp = int(round(time.time() * 1000))
    return time_stamp
async def transaction(page_index,limit_count,call_back_resp):
    global ADDRESS
    start_number=(page_index-1)*limit_count
    url=f'{prefix}&limit='+str(limit_count)
    url+=f'&start='+str(start_number)
    url+=f'&address='+ADDRESS
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp :
            res = await resp.json()
            call_back_resp(res)
def run_async_func():
    asyncio.run(recent_transaction())
async def recent_transaction():
    global ADDRESS
    global start_time_stamp
    global end_time_stamp
    global start
    if not start:
        start_time_stamp=get_time_stamp()
        start=True
    else:
        end_time_stamp=get_time_stamp()
        url=f'{prefix}&limit=50'
        url+="&start=0"
        url+="&start_timestamp="+str(start_time_stamp)
        url+="&end_timestamp="+str(end_time_stamp)
        url+=f'&address={ADDRESS}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp :
                print(url)
                res = await resp.json()
                start_time_stamp=end_time_stamp
                retr_web_soc().emit("new_send_data",res)