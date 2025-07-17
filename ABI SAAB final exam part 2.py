# PART 2

import pandas as pd 

# load excel file
##df = pd.read_excel("ABI SAAB Stephanie-2.xlsx")
df = pd.read_excel("/Users/stephanie/Downloads/ABI SAAB Stephanie-2.xlsx")


# show all column names
print("All columns:")
print(df.columns)

#im deleting the useless columns and keeping only useful ones that help for the analysis
df = df[[
    "Deal ID", #to count how many deals there are
    "Deal Type", #to see what type of deals are there, if its new or exisitng businness
    "Original Source Data 1", #to know where the deals are coming from
    "Create Date", #to know when the deals were created, analyse by year
    "Amount in company currency", #to calculate money from deals
    "Closed Date" #could be used for time analusys if needed
]]

#rename columns to make them easier to use
df = df.rename(columns={
    "Deal ID": "DealID",
    "Deal Type": "DealType",
    "Original Source Data 1": "Source",
    "Create Date": "CreateDate",
    "Amount in company currency": "Amount",
    "Closed Date": "ClosedDate"
})

# convert dates to real datetime values so python can understand them
df["CreateDate"] = pd.to_datetime(df["CreateDate"], errors="coerce")
df["ClosedDate"] = pd.to_datetime(df["ClosedDate"], errors="coerce")

# convert everything to numeric values and remove the wrong ones
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

#remove rows with no amount
df = df.dropna(subset=["Amount"])

#add a Year column from CreateDate to help analyse how deals changed over time per year
df["Year"] = df["CreateDate"].dt.year
#
#save cleaned data to a new excel file
df.to_excel("cleaned_ABI_SAAB.xlsx", index=False)

# here I want to count how many deals were made per year
deals_per_year = df["Year"].value_counts().sort_index()
print("Deals per year:")
print(deals_per_year)

import matplotlib.pyplot as plt #for plotting the data

# to see which sources (like SALES or CONTACTS) brought the most deals
source_counts = df["Source"].value_counts()
print("Deals by source:")
print(source_counts)


# to see how much money we make on average from each source
avg_amount_by_source = df.groupby("Source")["Amount"].mean().sort_values(ascending=False)
print("Average amount per source:")
print(avg_amount_by_source)

# CHART 1  REVENUE PER YEAR
#group by year and sum up the amounts to get total money made per year
revenue_per_year = df.groupby("Year")["Amount"].sum()

# plot the result as a bar chart
plt.figure()
revenue_per_year.plot(kind="bar")
plt.title("Total Revenue per Year")
plt.xlabel("Year")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("scheme1_revenue_per_year.png")

#Insight chart 1
print("Insight Chart 1 : Revenue was significantly higher in 2020 compared to other years, indicating a strong performance that year.")

# CHART 2 Number of Deals by Deal Type
# count how many deals there are of each deal type (new vs existing business)
deal_type_counts = df["DealType"].value_counts()

# plot this as a bar chart
plt.figure()
deal_type_counts.plot(kind="bar")
plt.title("Number of Deals by Deal Type")
plt.xlabel("Deal Type")
plt.ylabel("Number of Deals")
plt.tight_layout()
plt.savefig("scheme2_deals_by_type.png")

#Insight chart 2
print("Insight Chart 2: New business deals are more common than existing business deals")

# CHART 3 Revenue by Deal Type
# for each deal type, calculate the total amount of money earned
revenue_by_type = df.groupby("DealType")["Amount"].sum()

# plot the result
plt.figure()
revenue_by_type.plot(kind="bar")
plt.title("Total Revenue by Deal Type")
plt.xlabel("Deal Type")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("scheme3_revenue_by_type.png")

#Insight chart 3
print("Insight Chart 3: Even though New business has more deals, Existing business brings in more revenue")

# CHART 4: Number of Deals by Source
# count how many deals came from each source (like sales, contacts, etc.)
source_counts = df["Source"].value_counts()

# using a horizontal bar chart easy to read
plt.figure()
source_counts.plot(kind="barh")
plt.title("Number of Deals by Source")
plt.xlabel("Count")
plt.ylabel("Source")
plt.tight_layout()
plt.savefig("scheme4_deals_by_source.png")

# CHART 5 Average Deal Amount per Year 
# group by year and get the average amount per deal
avg_deal_by_year = df.groupby("Year")["Amount"].mean()

# plot it as a line chart
plt.figure()
avg_deal_by_year.plot(marker='o')  # the dots show the value for each year
plt.title("Average Deal Amount per Year")
plt.xlabel("Year")
plt.ylabel("Average Amount")
plt.tight_layout()
plt.savefig("scheme5_avg_amount_per_year.png")

#Insight chart 5
print("Insight Chart 5: The average deal amount increased over the years, especially in 2020, indicating higher value deals were made, compared to 2021.")

# CHART 6: Average Duration per Year
# calculate how many days each deal took to close
df["Duration"] = (df["ClosedDate"] - df["CreateDate"]).dt.days
# remove rows where duration couldn't be calculated
df = df.dropna(subset=["Duration"])
# calculate average duration overall
avg_duration = df["Duration"].mean()
print("Average deal closing time:", round(avg_duration, 2), "days")
# group by year and calculate average time it took to close deals
avg_duration_by_year = df.groupby("Year")["Duration"].mean()

# plot the result
plt.figure()
avg_duration_by_year.plot(marker='o', color="orange")
plt.title("Average Deal Closing Duration per Year")
plt.xlabel("Year")
plt.ylabel("Average Duration (days)")
plt.tight_layout()
plt.savefig("scheme6_avg_duration_per_year.png")

#Insight chart 6
print("Insight Chart 6: The average time to close deals has been decreasing over the years")

plt.show()

## /opt/anaconda3/bin/python "/Users/stephanie/Downloads/ABI SAAB final exam part 2.py"