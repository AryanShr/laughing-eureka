from uagents import Bureau, Agent, Protocol, Context
from uagents.setup import fund_agent_if_low
from messages import Cab, CabSelection,CabDetails
from agents.Calender.calender import BookEventRequest

agent = Agent('core', seed="core's seceret seed")

fund_agent_if_low(agent.wallet.address())

@agent.on_message(model=CabDetails)
async def receive_cab_details(ctx: Context, sender: str, msg: CabDetails):
    ctx.logger.info(f"Received message from {sender} in core, session: {ctx.session}")
    ctx.logger.info(f"{msg}")
    await ctx.send("agent1qttrpd7ngt8q4pf2htrf52ms5jqtslmch3cv4h5u9g8z8kyh4ddh6ned3q9", BookEventRequest(title="Cab booked", location="XYZ", start_date_time="2023-12-28T09:13:00+05:30",end_date_time="2023-12-28T10:14:00+05:30"))

if __name__ == "__main__":
    bureau = Bureau(endpoint=["http://127.0.0.1:8005/submit"], port=8005)
    print(f"Adding core agent to Bureau: {agent.address}")
    bureau.add(agent)
    bureau.run()