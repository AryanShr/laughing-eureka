from uagents import Agent, Context, Protocol, Bureau
from uagents.setup import fund_agent_if_low
from messages import Cab, UAgentResponse, UAgentResponseType, CabSelection
import requests
import os
import uuid
from agents.cab_booking.cabs.cab_protocol import cab_protocol

CAB_BOOKING_SEED = os.environ.get('CAB_BOOKING_SEED', 'No one can guess me :)')
# uber developers


agent = Agent('cab_booking', seed=CAB_BOOKING_SEED, endpoint=["http://127.0.0.1:8002/submit"])

fund_agent_if_low(agent.wallet.address())

@agent.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info("Cab booking agent started")
    # await ctx.send("agent1q24wv58qcmxe5t2pr5auyzzm6ahh94ck4dd00s7e0sfc4td2jtkdgtprj9f",Cab(distance_from_source=10, distance_for_travel=20))
    await ctx.send("agent1q0pnrp5ahn3stfyuf3s0ym5euuurl3w4ztu60af5v8qv6cndktynqrr99kc",Cab(distance_from_source=10, distance_for_travel=20))
    await ctx.send("agent1qgg4jvaj3a3xtde3wc2gkvqwl43mflt9awnr9za6huu44x80sx7fu2mwz2q",Cab(distance_from_source=10, distance_for_travel=20))
    await ctx.send("agent1qdax9c520nn457edq0q9meumn3ng98pra0840fdqsjpjrarm6p4qvf6ne9g",Cab(distance_from_source=10, distance_for_travel=20))

@agent.on_message(model=CabSelection)
async def cab_selection(ctx: Context, sender: str, msg: CabSelection):
    ctx.logger.info(f"Received message from {sender}, session: {ctx.session}")
    ctx.logger.info(f"{msg}")



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