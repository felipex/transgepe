import streamlit as st
import pandas as pd
import numpy as np
import sys
import os
from servidores import Servidores


directory = os.path.abspath("../..")
sys.path.append(directory)

from common import header, c_css

c_css()
header()

st.markdown("### Aposentados")
#Servidores().carrega("./dw/UFCA202212.csv")
aposentados = Servidores().aposentados()[["NOME SERVIDOR", "ID SERVIDOR", "CARGO"]]

#int_index = np.array(aposentados.count())
#indexes = pd.Series(int_index, copy=False)
#aposentados.set_index(indexes)


aposentados = aposentados.reset_index(drop=True)
aposentados.insert(0, "POS", aposentados.index.values+1)
blank = [''] * len(aposentados)
aposentados.index = blank
st.dataframe(aposentados)

