#Data Visualization of Excel Data Demo-financial sample: PIE PLOT

import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = "Financial Sample.xlsx"
df = pd.read_excel(excel_file_path)
#print(df)

### 3 DIFFERENT WAYS OF PLOTTING

## Time Series: A Panda Series is similar to a column in excel


                                        # | : means "or"
                                        # & : means  "and"

### 1.CREATING A TIME SERIES PLOT:

# with CONDITIONAL INDEX we can pull out certain values within a Data Frame...
 # ...Depending on the value within that column

df_vtt_canada = df.loc[(df["Country"] == "Canada") & (df["Product"]=="VTT") &(df["Segment"] =="Government")]
df_vtt_canada = df_vtt_canada.sort_values(by=["Date"])
##df_vtt_canada.plot(x="Date",y="Profit")
##plt.show()


### 2. CREATING A BAR PLOT(bar chart):

##df_products = df.groupby(["Product"]).sum()
##df_products["Units Sold"].plot.bar()
##plt.show()

### 3. CREATING A PIE PLOT(pie chart):
df_products = df.groupby(["Product"]).sum()
df_products["Units Sold"].plot.pie()
plt.show()
