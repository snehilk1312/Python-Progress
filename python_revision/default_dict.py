from collections import defaultdict
state_capitals=defaultdict(lambda:'Delhi')
def capitals(state,capital):
	state_capitals[state]=capital
capitals('Bihar','Patne')
capitals('kerela','Tiruananthpuram')
capitals('Goa','Panji')
capitals('Himachal','Shimla')


print(state_capitals['Bihar'],state_capitals['Jharkhand'],sep='\n')

