from uagents import Agent, Context, Protocol
from uagents.setup import fund_agent_if_low
from messages import Cab, UAgentResponse, UAgentResponseType
import requests
import os
import uuid

CAB_DRIVER_SEED = os.environ.get('CAB_DRIVER_SEED', 'No one can guess me:)')
is_available = False
# uber developers
agent = Agent('cab_booking', seed=CAB_DRIVER_SEED)

def faretimeCalc(Travel_distance,User_Distance):
    fare = 0.45*Travel_distance
    time =  40*User_Distance
    return fare,time 

fund_agent_if_low(agent.wallet.address())

@agent.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info("Cab Agent Started")

cab_protocol = Protocol("CabAgent")

@cab_protocol.on_message(model=Cab)
async def send_state(ctx: Context, sender: str, msg: Cab):
    ctx.logger.info(f"Received message from {sender}, session: {ctx.session}")
    fare,time = faretimeCalc(msg.distance_from_source,msg.distance_for_travel)
    await ctx.send(sender,CabSelection(is_available=is_available,fare=fare,arrival_time=time))
    # This is just example for 5 cab options\
agent.include(cab_protocol)

if __name__ == "__main__":
    agent.run()