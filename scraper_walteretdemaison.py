import requests
from bs4 import BeautifulSoup

URL = 'https://www.walteretdemaison.com/qui-sommes-nous/?fbclid=IwAR3eOtdd3ZNNkP0UEUIrUFumr_OKMGgMFwnUHpHOK7mvbSlrclNBRDE5SCQ'


def scrape_all_agents():  # returns dict
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_agents = []
    agents = soup.findAll('div', attrs={'elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-2cc6236'})

    for agent in agents:
        agent_name = agent.find('h1', {'class': 'elementor-heading-title elementor-size-default'}).text.strip()
        agent_zipcode = agent.find('h2', {'class': 'elementor-heading-title elementor-size-default'}).text.strip()
        agent_zipcode = agent_zipcode[agent_zipcode.find("(") + 1:agent_zipcode.find(")")]
        current_agent = {'name': agent_name, 'zip': agent_zipcode}
        all_agents.append(current_agent)
    return all_agents


def zip_list():  # returns number of agents on per zipcode
    zip_list = []
    all_agents = scrape_all_agents()

    for i in range(len(all_agents)):
        zipc = all_agents[i].get('zip')
        count = sum(x.get('zip') == zipc for x in all_agents)
        zip_counter = {zipc: count}
        if zip_counter not in zip_list:
            zip_list.append(zip_counter)
        else:
            pass
    return zip_list


if __name__ == "__main__":
    print("Start")
    all_agents = scrape_all_agents()
    zip_list = zip_list()
    print(all_agents)
    print(zip_list)