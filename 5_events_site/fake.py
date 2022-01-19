#%%
import boto3
import json
from fake_web_events import Simulation

#%%
client = boto3.client("firehose")

#%%
def put_record(event: dict):
    """[recebe um evento em json e retorna uma string quebrando a linha no final
    deixando cada registro em uma linha diferente]

    Args:
        event (dict): [evento gerado pelo faker]

    """

    data = json.dumps(event) + "\n"
    response = client.put_record(DeliveryStreamName="", Record={"Data": data})
    print(event)
    return response


#%%
simulation = Simulation(user_pool_size=100, sessions_per_day=100000)
events = simulation.run(duration_seconds=300)

for event in events:
    print(event)
