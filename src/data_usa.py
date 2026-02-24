from requests import Session

class DataUsa:
	def __init__(self) -> None:
		self.api = "https://datausa.io/api"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_data(
			self,
			drill_downs: str,
			measures: str,
			year: str = "latest") -> dict:
		return self.session.get(
			f"{self.api}/data?drilldowns={drill_downs}&measures={measures}&year={year}").json()
