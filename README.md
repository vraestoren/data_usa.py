<div align="center">
  <img src="https://datausa.io/images/home/logo-shadow.png" width="200" />

# data_usa.py

> Web-API for [Data USA](https://datausa.io) a free, open platform for public US data covering population, economy, education, health, and more.

</div>

## Quick Start

```python
from data_usa import DataUsa

data_usa = DataUsa()

# Get the latest US population by state
print(data_usa.get_data(drill_downs="State", measures="Population"))

# Get population by nation for a specific year
print(data_usa.get_data(drill_downs="Nation", measures="Population", year="2020"))
```

---

<div align="center">

## Data

| Method | Description |
|--------|-------------|
| `get_data(drill_downs, measures, year)` | Query US public data by dimension and metric |

## Parameters

| Parameter | Description |
|-----------|-------------|
| `drill_downs` | Geographic or categorical dimension — e.g. `Nation`, `State`, `County`, `MSA` |
| `measures` | Metric to retrieve — e.g. `Population`, `Average Wage`, `Total Employment` |
| `year` | Year to filter by — e.g. `2020`. Defaults to `latest` |

</div>
