import requests, json, random, time
import networkx as nx
import matplotlib.pyplot as plt

edges = []
closedges = []
url = "https://api.vk.com/method/groups.getMembers?group_id=25205856&v=5.52&access_token="
#request for all members in our group

response = requests.get(url)

dict1 = response.json()
list = dict1.get('response', {})['items'] #list of all ids from the group

newlist = random.sample(list, 500) #for 500 people, this variable can be changed if you want


for person in newlist:
    person = str(person)
    time.sleep(1) #we make pause because vk doesn't allow to make requests too often
    urll = "https://api.vk.com/method/users.get?user_id="+person+"&v=5.89&access_token="
    response = requests.get(urll)
    d = response.json()
    person = int(person)
    print(d) #print some adiitional info to be sure that this code works correctly))
    seq = d.get('response', {})[0]
    secure = seq.setdefault('is_closed')
    if (secure == True) or (secure == None): #delete accounts which were deleted and had no useful information
        newlist.remove(person)
community = newlist
print(community) #get the final (correct) list of ids which we will use further


for number in community:
    number = str(number)
    url = "https://api.vk.com/method/friends.get?user_id="+number+"&v=5.52&access_token="
    response = requests.get(url)
    #for each person in our list we get all his/her friends
    dict1 = response.json()
    seq = dict1.get('response', {})
    friends = seq.get('items')
    if friends != None:
        for idd in community:
            for person in friends:
                if person == idd:
                    person = str(person)

                    time.sleep(1)
                    namenumber = requests.get("https://api.vk.com/method/users.get?user_id="+number+"&v=5.89&access_token=")
                    time.sleep(1)
                    nameperson = requests.get("https://api.vk.com/method/users.get?user_id="+person+"&v=5.89&access_token=")
                    n = namenumber.json()
                    nn = n.get('response', {})[0]
                    print(nn) #leave some outputs for checking
                    p = nameperson.json()
                    pp = p.get('response', {})[0]
                    print(pp) #leave some outputs for checking
                    firstnumber = nn.get('first_name')
                    lastnumber = nn.get('last_name')
                    firstperson = pp.get('first_name')
                    lastperson = pp.get('last_name')

                    edges.append((firstnumber+' '+lastnumber, firstperson+' '+lastperson))
                    #get the list of pairs (two nodes) - first and last name of a person

    number = int(number)

print(edges)

#graph visualization
G = nx.Graph()
G.add_edges_from(edges)
nx.draw(G, with_labels=True, node_color='pink', edge_color='pink') #make a pink graph
plt.savefig("edge_colormap.png") #finally, get the image of the graph
plt.show()


