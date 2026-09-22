import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame({"month":["Jan","Feb","Mar","Apr","May","Jun"],"sales":[120,150,135,190,220,205]})
plt.plot(df["month"],df["sales"],marker="o")
plt.title("Monthly Sales"); plt.xlabel("Month"); plt.ylabel("Sales")
plt.tight_layout(); plt.savefig("sales.png"); print("Saved sales.png")
