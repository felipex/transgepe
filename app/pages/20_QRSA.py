import streamlit as st
import pandas as pd
import numpy as np
import sys
import os
import dados 
from servidores import Servidores


directory = os.path.abspath("../..")
sys.path.append(directory)

from app.common import header, c_css

c_css()
header()

st.markdown("### Quase um QRSA")
servidores = servidores = Servidores().efetivos()

st.dataframe(pd.DataFrame(servidores.sort_values(["CARGO"]).groupby(["CARGO"]).size()), use_container_width=True)


