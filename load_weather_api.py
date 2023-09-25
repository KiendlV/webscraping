import json
import weather_app_api as waa
import pandas as pd

#weather_call_file = waa.weather_call().json()
#print(waa.weather_call().json())

#patients_df = pd.read_json(weather_call_file)
#patients_df.head()

waa.weather_call()

print("hello")