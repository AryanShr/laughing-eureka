from uagents import Agent, Context, Protocol, Bureau
from uagents.setup import fund_agent_if_low
from messages import Cab, UAgentResponse, UAgentResponseType, CabSelection, CabDetails
import requests
import os
import uuid
from agents.cab_booking.cabs.cab_protocol import cab_protocol

CAB_BOOKING_SEED = os.environ.get('CAB_BOOKING_SEED', 'No one can guess me :)')
# uber developers
def bestBook(is_available,fare,arrival_time):
    if(is_available == False):
        prio = 0.2*fare + 0.5*arrival_time
        return prio
    else:
        return 99999
    
drivers = []

agent = Agent('cab_booking', seed=CAB_BOOKING_SEED, endpoint=["http://127.0.0.1:8002/submit"])

fund_agent_if_low(agent.wallet.address())

@agent.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info("Cab booking agent started")
    # await ctx.send("agent1q24wv58qcmxe5t2pr5auyzzm6ahh94ck4dd00s7e0sfc4td2jtkdgtprj9f",Cab(distance_from_source=10, distance_for_travel=20))
    await ctx.send("agent1q0pnrp5ahn3stfyuf3s0ym5euuurl3w4ztu60af5v8qv6cndktynqrr99kc",Cab(distance_from_source=14, distance_for_travel=20,source="margao",destination="panvel"))
    await ctx.send("agent1qgg4jvaj3a3xtde3wc2gkvqwl43mflt9awnr9za6huu44x80sx7fu2mwz2q",Cab(distance_from_source=8, distance_for_travel=20,source="margao",destination="panvel"))
    await ctx.send("agent1qdax9c520nn457edq0q9meumn3ng98pra0840fdqsjpjrarm6p4qvf6ne9g",Cab(distance_from_source=12, distance_for_travel=20,source="margao",destination="panvel"))

@agent.on_message(model=CabSelection)
async def cab_selection(ctx: Context, sender: str, msg: CabSelection):
    ctx.logger.info(f"Received message from {sender}, session: {ctx.session}")
    ctx.logger.info(f"{msg}")
    drivers.append({"name":sender,"is_available":msg.is_available,"fare":msg.fare,"arrival_time":msg.arrival_time})
    drivers.sort(key=lambda x: bestBook(x["is_available"],x["fare"],x["arrival_time"]))
    best_detail = drivers[0]
    await ctx.send("agent1qwjceuqy2vufna56gh63sk45mu3uds37wy5mquxr7gvlxkusr4trgvn6qku",CabDetails(cab_name=best_detail["name"],cab_fare=best_detail["fare"],cab_arrival_time=best_detail["arrival_time"]))



# cab_protocol = Protocol("CabBooking")

# @cab_protocol.on_message(model=Cab, replies={UAgentResponse})
# async def get_cab(ctx: Context, sender: str, msg: Cab):
#     ctx.logger.info(f"Received message from {sender}, session: {ctx.session}")
#     # This is just example for 5 cab options

#     cab_options = [
#         {"name": "Uber", "price": 100, "time": 10},
#         {"name": "Ola", "price": 120, "time": 15},
#         {"name": "Lyft", "price": 110, "time": 12},
#         {"name": "Bolt", "price": 90, "time": 8},
#         {"name": "Juno", "price": 95, "time": 9},
#     ]

#     await ctx.send(
#         sender,
#         UAgentResponse(
#             options=cab_options,
#             type=UAgentResponseType.SELECT_FROM_OPTIONS
#         )
#     )


# agent.include(cab_protocol)

if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8002/submit",port=8002)
    print(f"Adding agent {agent.address} to bureau")
    bureau.add(agent)
    bureau.run()