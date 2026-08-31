import streamlit as st
import requests
import pandas as pd

@st.cache_data(ttl=3600, show_spinner="Please wait, downloadin data...", show_time=True)
def get_data():
	return pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQzygCvwtLMntovyqRVjgZUmRPrl4Buo8j9x2j9XecRrSGM7erBu3003UfZenbdwkOjEPgeozJ7ZRbf/pub?output=csv")


def page_intro():
	st.markdown("# Research Insights")
	st.write("_Last updated: August 31, 2026._")
	st.write(
	"""
	This data is collected and analyzed by the Research Lifecycle Department in the Library. It is source primarily from [OpenAlex](https://openalex.org/) and yearly information is presented by acadmic year, IE. July 1, to June 30.
	
	Check out our [getting your research out](https://researchguides.library.brocku.ca/getting-your-research-out/) guide for more details about how to get the best reach for your publications. For further breakdown by year please see our _State of Scholarly Publishing_ Reports.
	- [2025](https://elibtronic.github.io/2025_state_of_scholarly_communication/)
	- [2026](https://elibtronic.github.io/2026_state_of_scholarly_communication/)
	
	""")
	
	st.download_button(
	label = "Download data use for this project",
	data = df.to_csv().encode("utf-8"),
	file_name = "brock_research_insights",
	mime = "text/csv",
	icon = ":material/download:"
	)

def page_total():
	st.markdown("## Total Publications")
	st.bar_chart(df,\
					x="year",\
					x_label="Year",\
					y_label="Total Journal Publications",\
					y=["total_pubs_closed","total_pubs_oa"]
					)
	st.write("""
	The total number of journal articles published by Brock Researchers is shown in the chart above. This is presented along the academic year, and only for journal articles that have a DOI.
	
	You can see that in 2026 the proportion of _open access_ articles has grown by quite a bit.
	""")
	
def page_apc():
	st.markdown("## Article Processing Charges")

	st.write("""
	
	Article Processing Charges (APC) are fees that you pay to make your work _open access_. As you can see from these charts, these cost quite a bit.
	
	""")

	st.write("### Total APC spend for the year")
	st.bar_chart(df,\
					x="year",
					x_label="Year",
					y_label="Total APC ($)",
					y="apc_total",
					)	

	st.write("### Average APC cost")
	st.bar_chart(df,
					x="year",
					x_label="Year", 
					y="apc_avg",
					y_label="Average APC ($)",
					)

	st.write("""
	### APC Support?
	The Library now has an app that will help you determine if your publication is eligible for a discount to these fees, or to have them waived entirely. You can search both by publisher and journal title.
	
	[APC Discount Finder](https://brock-apc-info.streamlit.app/)
	
	""")



def page_green_pathways():
	st.markdown("## Green Open Access Pathways")
	st.bar_chart(df,\
					x="year",
					x_label="Year",
					y="free_green_pathways",
					y_label="Free Pathways")
					
					
	st.write("""
	
	Often when you publish an article there is a way to create an _open access_ version of your publication **without paying a fee**! The only catch is that you might need to share the _Preprint_ or _Postprint_ version of your paper to accomplish this. Our [Depositing an Open Access Version of Your Publications](https://researchguides.library.brocku.ca/getting-your-research-out/depositing-open-access) guide can explain how this works. 
	
	""")
		
df = get_data()

st.image("images/logo.png")
pg = st.navigation([
	st.Page(page_intro, title="Brock Research Insights"),
	st.Page(page_total,title="Total Publications",icon="📘"),
	st.Page(page_apc,title="Article Processing Charges",icon="💲"),
	st.Page(page_green_pathways,title="Green Pathways", icon="📗")
])

pg.run()

