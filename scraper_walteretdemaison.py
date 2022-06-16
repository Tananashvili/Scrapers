import requests
from bs4 import BeautifulSoup
from collections import Counter

URL = 'https://www.walteretdemaison.com/qui-sommes-nous/?fbclid=IwAR3eOtdd3ZNNkP0UEUIrUFumr_OKMGgMFwnUHpHOK7mvbSlrclNBRDE5SCQ'


def scrape_all_agents():  # returns dict
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    agents_names = []
    agents_zipcodes = []
    names_container = soup.findAll('div', attrs={'class': 'elementor-element elementor-element-474c39f elementor-widget elementor-widget-theme-post-title elementor-page-title elementor-widget-heading'})
    zipcodes_container = soup.findAll('div', attrs={'class': 'elementor-element elementor-element-67eea2b elementor-widget elementor-widget-heading'})

    for name in names_container:
        agent_name = name.find('h1', {'class': 'elementor-heading-title elementor-size-default'}).text.strip()
        agents_names.append(agent_name)
    for zipc in zipcodes_container:
        agent_zipcode = zipc.find('h2', {'class': 'elementor-heading-title elementor-size-default'}).text.strip()
        agent_zipcode = agent_zipcode[agent_zipcode.find("(") + 1:agent_zipcode.find(")")]
        agents_zipcodes.append(agent_zipcode)

    all_agents = dict(zip(agents_names, agents_zipcodes))
    return all_agents


def zip_list():  # returns number of agents on per zipcode
    all_agent = scrape_all_agents()
    zip_list = Counter(all_agent.values())
    return zip_list


if __name__ == "__main__":
    print("Start")
    all_agent = scrape_all_agents()
    zip_list = zip_list()
    print(all_agent)
    print(zip_list)
