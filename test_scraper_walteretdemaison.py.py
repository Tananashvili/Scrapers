from scraper_walteretdemaison import scrape_all_agents, zip_list


def test_scrape_all_agents():
    agents = scrape_all_agents()

    assert isinstance(agents, list)
    assert len(agents) > 5
    

def test_zip_list():
    zipcodes = zip_list()

    assert isinstance(zipcodes, list)
    assert len(zipcodes) > 5