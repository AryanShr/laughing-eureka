from uagents import Agent, Context, Protocol
from uagents.setup import fund_agent_if_low
from messages import Cab, UAgentResponse, UAgentResponseType
import requests
import os
import uuid

CAB_BOOKING_SEED = os.environ.get('CAB_BOOKING_SEED', 'No one can guess me :)')
# uber developers


agent = Agent('cab_booking', seed=CAB_BOOKING_SEED)

fund_agent_if_low(agent.wallet.address())

@agent.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info("Cab booking agent started")

cab_protocol = Protocol("CabBooking")

@cab_protocol.on_message(model=Cab, replies={UAgentResponse})
async def get_cab(ctx: Context, sender: str, msg: Cab):
    ctx.logger.info(f"Received message from {sender}, session: {ctx.session}")
    # This is just example for 5 cab options

    cab_options = [
        {"name": "Uber", "price": 100, "time": 10},
        {"name": "Ola", "price": 120, "time": 15},
        {"name": "Lyft", "price": 110, "time": 12},
        {"name": "Bolt", "price": 90, "time": 8},
        {"name": "Juno", "price": 95, "time": 9},
    ]

    await ctx.send(
        sender,
        UAgentResponse(
            options=cab_options,
            type=UAgentResponseType.SELECT_FROM_OPTIONS
        )
    )


agent.include(cab_protocol)

if __name__ == "__main__":
    agent.run()