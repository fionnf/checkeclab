from galvani import BioLogic
import pandas as pd

mpr_file = BioLogic.MPRfile('FF054BioLgic_C06.mpr')
df = pd.DataFrame(mpr_file.data)
print(df)
