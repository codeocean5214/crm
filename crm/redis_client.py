#making the redis client for the global crm services 
import redis.asyncio as redis  
import os  
#created a insance of the class  
class ReidsClient : 
    def __init__(self):
        self.client = redis.Redis(
        host = os.getenv("REDIS_HOST","localhost"),
        port = 6379, 
        decode_responses= True , 
        password=os.getenv("REDIS_PASSWORD",None), 
        socket_timeout = 10, 
        retry_on_timeout=True, 
        retry_on_error=True 
    )

    #testing the connection before intiation  
    async def test(self) : 
        try : 
            return await self.client.ping() #pining to the test the connection 

        except Exception as e : 
            print(f"Error in the redis connection {e}")
    async def close(self) : 
        self.client.close()
        
redis_client = ReidsClient()

