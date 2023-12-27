from uagents import Bureau
 
from agents.top_destinations.top_destinations import agent as top_destinations_agent
from agents.cab_booking.cab_booking import agent as cab_agent
 
if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8001/submit", port=8001)
    print(f"Adding top destinations agent to Bureau: {top_destinations_agent.address}")
    bureau.add(top_destinations_agent)
    # print(f"Adding flights agent to Bureau: {cab_agent.address}")
    # bureau.add(cab_agent)
    bureau.run()