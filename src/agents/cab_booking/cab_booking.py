from uagents import Agent, Context, Protocol
from uagents.setup import fund_agent_if_low
import requests
import os
import uuid

CAB_BOOKING_SEED = os.environ.get('CAB_BOOKING_SEED', 'No one can guess me :)')


agent = Agent('cab_booking', seed=CAB_BOOKING_SEED)

fund_agent_if_low(agent.wallet.address())

@agent.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info("Cab booking agent started")




if __name__ == "__main__":
    agent.run()