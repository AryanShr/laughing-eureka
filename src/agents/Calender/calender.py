from typing import List
from uagents import Agent, Context, Model, Protocol
from uagents.setup import fund_agent_if_low
import agents.Calender.calenderFunctions.calender as c

SUCCESS = 1
FAILURE = -1

class BookEventRequest(Model):
    title: str
    location: str
    start_date_time: str
    end_date_time: str

class BookEventResponse(Model):
    success: bool


calender_proto  = Protocol()

@calender_proto.on_message(model=BookEventRequest, replies=BookEventResponse)
async def handle_query_request(ctx: Context, sender: str, msg: BookEventRequest):
    print("starting the request")
    title = msg.title
    location = msg.location
    start_date_time = msg.start_date_time
    end_date_time = msg.end_date_time
    response = c.create_event(start_date_time, end_date_time, title, location)
    print("this is ",response)
    await ctx.send(sender,BookEventResponse(success=response))


@calender_proto.on_message(model=BookEventResponse)
async def message_handler(ctx: Context, _: str, msg: BookEventResponse):
    print("i reached")
    ctx.logger.info("Event is a",msg.success)


agent = Agent(
    name="User Calender Agent",
    seed="This is some simple stuff",
    port = 8000,
    endpoint = ["http://127.0.0.1:8000/submit"]
)

agent.include(calender_proto)


# @agent.on_event("startup")
# async def book_event(ctx: Context):

#     start_date_time = '2023-12-28T09:13:00+05:30'
#     end_date_time = '2023-12-28T10:14:00+05:30'
#     title = 'Fetch AI winning celeberation'
#     location = 'Mumbai IIT Bombay'
#     print('starting')
#     await ctx.send(agent.address,BookEventRequest(
#         title=title,
#         start_date_time=start_date_time,
#         end_date_time=end_date_time,
#         location=location
#     ))



fund_agent_if_low(agent.wallet.address())

if __name__ == "__main__":
    agent.run()