import pytest

from pages.flight_result_page import FlightResult
from pages.home_page import HomePage
from pages.search_flight_page import SearchFlight
from pages.traveller_details_page import TravellerDetails


@pytest.mark.usefixtures("setUp")
class TestFlight:
    @pytest.fixture(autouse=True)
    def __setFlight__(self):
        self.click = HomePage(self.driver, self.wait)
        self.search_from = SearchFlight(self.driver, self.wait)
        self.travel = TravellerDetails(self.driver, self.wait)
        self.result = FlightResult(self.driver, self.wait)

    def test_click_flight(self):
        print("CLick Flight")
        self.click.click_flight()

    def test_search_flight(self):
        # self.search_from.enter_from("chandigarh")
        # self.search_from.enter_to("Delhi")
        # self.search_from.enter_date("30", "2022")
        # self.search_from.enter_pax()
        self.search_from.click_search_flight()

    @pytest.mark.parametrize("stop_filter", ["Non Stop", "1 stops"])
    def test_filter(self, stop_filter):
        self.result.filters(stop_filter)

    # def test_traveller_details(self):
    #     self.travel.enter_traveller_details()
    #     self.travel.info()
    #     self.travel.login()
