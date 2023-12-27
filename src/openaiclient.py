from messages.general import InputPrompt, Response
from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
import os
 
OPEN_AI_SEED_CLIENT = os.getenv("OPEN_AI_SEED", "Totally Clueless ;_;")

open_ai_client = Agent(
    name="OpenAI Client",
    seed=OPEN_AI_SEED_CLIENT,
    port = 8008,
    endpoint = ["http://127.0.0.1:8008/submit"]
)

fund_agent_if_low(open_ai_client.wallet.address())

open_ai_req = InputPrompt(travelQuery="I am new to Delhi, suggest me a travel plan this weekend")

@open_ai_client.on_event("startup")
async def say_hello(ctx:Context):
    ctx.logger.info(f"Hello from OpenAI Client! {ctx.name}")
    await ctx.send("agent1qw28qf58k3w0uaap5cwg0el75rr65j55qcfkace4hx4ltdpsctkkz8qtvv2", open_ai_req)

@open_ai_client.on_message(model=Response)
async def respond_to_prompt(ctx:Context, sender: str, msg: Response):
    ctx.logger.info(f"Received response from {sender}: {msg}")
    
    ctx.logger.info(f"Generated output: {msg.output}")

if __name__ == "__main__":
    open_ai_client.run()
