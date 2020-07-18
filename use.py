from source import StreetlightsNeuroWeb
import numpy as np
streetlights = np.array( [[ 1, 0, 1 ],
                          [ 0, 1, 1 ],
                          [ 0, 0, 1 ],
                          [ 1, 1, 1 ]] )

walk_vs_stop = np.array([[ 1, 1, 0, 0]]).T                
model = StreetlightsNeuroWeb(streetlights,walk_vs_stop)
model.fit(121,alpha=0.05)
print(model.predict_light([0,0,0]))# False
print(model.predict_light([0,1,0]))# True
print(model.predict_light([0,1,1]))# True
print(model.predict_light([1,0,0]))# False
print(model.predict_light([1,0,1]))# True
print(model.predict_light([1,1,0]))# False
print(model.predict_light([1,1,1]))# True
