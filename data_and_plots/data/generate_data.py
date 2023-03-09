# DATA GENERATOR
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# DATA GENERATION
t = np.linspace(0., 10., 1000)
a = np.exp(-t /5) * np.cos(2. * np.pi * t)

# PLOT
fig = plt.figure()
plt.plot(t, a)
plt.grid()
plt.xlabel("Time, $t$ [s]")
plt.ylabel("Amplitude, $a$ [m/s$^2$]")
plt.savefig("data_plot.pdf")

# DATA EXPORT
data = pd.DataFrame()
data["t"] = t
data["a"] = a
data.to_csv("data_full.csv", index=False)

# LATEX TABULAR EXPORT
data_short = data.iloc[:10]
#data_out = data_short.to_latex(float_format="%.4e")
formatters = {"t":lambda t: "{0:.3f} s".format(t),
             "a":lambda a: "{0:.3e}".format(a)} 
data_out = data_short.to_latex(formatters=formatters)
with open("data_table.tex", "w") as f:
    f.write(data_out)