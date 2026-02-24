# data_usa.py
Web-API for [datausa.io](https://datausa.io) most comprehensive visualization of U.S. public data that provides an open, easy-to-use platform that turns data into knowledge

## Example
```python
from data_usa import DataUsa

data_usa = DataUsa()
data = data_usa.get_data(drill_downs="", measures="", year="")
print(data)
```
