from uagents import Bureau

from agents.cab_booking.cabs.cab_agent1 import agent as cab_agent1
from agents.cab_booking.cabs.cab_agent2 import agent as cab_agent2
from agents.cab_booking.cabs.cab_agent3 import agent as cab_agent3
 
if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8003/submit", port=8003)
    print(f"Adding cab agent to Bureau: {cab_agent1.address}")
    bureau.add(cab_agent1)
    print(f"Adding cab agent to Bureau: {cab_agent2.address}")
    bureau.add(cab_agent2)
    print(f"Adding cab agent to Bureau: {cab_agent3.address}")
    bureau.add(cab_agent3)
    bureau.run()