import streamlit as st
import plotly.express as px
import requests
import pandas as pd

@st.cache_data(ttl=3600, show_spinner="Please wait, downloadin data...", show_time=True)
def get_data():
	return pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQzygCvwtLMntovyqRVjgZUmRPrl4Buo8j9x2j9XecRrSGM7erBu3003UfZenbdwkOjEPgeozJ7ZRbf/pub?output=csv")


def page_intro():
	st.markdown("# Research Insights")
	st.write("_Last updated: November 4, 2026._")
	st.write(
	"""
	
	This app shows and describes some interesting details found in the publication output of Brock University. Please use the menu on the left to navigate. 
	
	This data is collected and analyzed by the Research Lifecycle Department in the Library. It is source primarily from [OpenAlex](https://openalex.org/) and yearly information is presented by acadmic year, IE. July 1, to June 30. It only show journal articles published by Brock affiliated authors.
	
	""")
	
	st.download_button(
	label = "Download Data",
	data = df.to_csv().encode("utf-8"),
	file_name = "brock_research_insights",
	mime = "text/csv",
	icon = ":material/download:"
	)

	st.write("""
	
	_Have any questions:question: Contact Tim [:mailbox:](https://researchguides.library.brocku.ca/prf.php?id=2bbc13f2-7cd6-11ed-8528-0266e2e2286e)._

	""")

def page_total():
	st.markdown("## Total Publications")
	
	st.write("""
	The total number of journal articles published by Brock Researchers is shown here. This is presented for the academic year, and only for journal articles that have a DOI.
	
	You can see that in 2026 the proportion of _open access_ articles has grown by quite a bit.
	""")
	fig_total = px.bar(df, 
				 x="year",
				 y=["total_pubs_closed","total_pubs_oa"],
				 labels = {
				 	"year" : "Year",
				 	"value" : "Number of Publications"
				 },
				 title = "Total Publications",
				 text_auto=True,
				 )
	st.plotly_chart(fig_total)

	
def page_apc():
	st.markdown("## Article Processing Charges")

	st.write("""
	
	Article Processing Charges (APC) are fees that you pay to make your work _open access_. As you can see from these charts, these cost quite a bit.
	
	""")

	fig_apc_total = px.bar(df,\
					x="year",
					y="apc_total",
					labels = {
				 	"year" : "Year",
				 	"apc_total" : "Total $ spent on APCS (in millions)"
				 	},
				 title = "Total APC Spend",
				 text_auto = True,
				 )
					
	st.plotly_chart(fig_apc_total)


	fig_apc_avg = px.bar(df,\
					x="year",
					y="apc_avg",
					labels = {
				 	"year" : "Year",
				 	"apc_avg" : "Average $ for APC",
				 	},
				 title = "APC per year",
				 text_auto = True,
				 )
					
	st.plotly_chart(fig_apc_avg)
	
	
	st.write("""
	### APC Support?
	The Library now has an app that will help you determine if your publication is eligible for a discount to these fees, or to have them waived entirely. You can search both by publisher and journal title.
	
	[APC Discount Finder](https://brock-apc-info.streamlit.app/)
	
	""")



def page_green_pathways():
	st.markdown("## Green Open Access Pathways")
	
	st.write("""
	
	Often when you publish an article there is a way to create an _open access_ version of your publication **without paying a fee**! We can this a **Green Open Access** pathway. The only catch is that you might need to share the _Preprint_ or _Postprint_ version of your paper to accomplish this. Our [Depositing an Open Access Version of Your Publications](https://researchguides.library.brocku.ca/getting-your-research-out/depositing-open-access) guide can explain how this works. 
	
	Every year during _Open Access Week_ we ask Brock researchers to consider submitting a Green Open Access version of their paper. We only ask in cases were this can be done for free, and for when the Brock reseacher is the primarly author. This charts shows how many emails we sent for each year and how many submissions we received within one month of that ask.
	
	
	""")
					
					
	fig_green_subs = px.bar(df,\
					x="year",
					y=["green_emails_sent","green_one_month_submissions"],
					labels = {
				 	"year" : "Year",
				 	},
				 title = "Open Access asked and Submitted",
				 text_auto = True,
				 )
					
	st.plotly_chart(fig_green_subs)		
					

def page_sosp():
	
	st.write(
	"""
	For further breakdown by year please see our _State of Scholarly Publishing_ Reports.
	- [2025](https://elibtronic.github.io/2025_state_of_scholarly_communication/)
	- [2026](https://elibtronic.github.io/2026_state_of_scholarly_communication/)
	
	""")

	
	
def page_reading_list():
	st.write("""
	
	Looking at research metrics requires some nuance. There is no clear consensus on what measures to pay attention to, or which ones provide an honest assement of research output. Lots has been said on these topics. Please consult the following readings to explore these discussions:
		
	""")
	
	st.markdown("""
	
	|   | 
	|---|
	|Cantrell MH, Caldwell R, Mezick JA, Estill M, Collister LB (2026) “The system is obviously bonkers”: The APC Trap and the bind of scholarly publishing across four research intensive institutions in the U.S.. _PLOS ONE_ 21(7): e0351430. [https://doi.org/10.1371/journal.pone.0351430](https://doi.org/10.1371/journal.pone.0351430)    |
	|Ribaric, T. & Moorhead, E. (2026). Constructing a (Meaningful) Scholarly Publishing Narrative: Bootstrapping Green Open Access Submissions for Open Access Week. _Journal of Librarianship and Scholarly Communication_, 14(1), eP21406. https://doi.org/10.31274/jlsc.21406    |
	|Gingras, Y. (2016). Bibliometrics and research evaluation : uses and abuses. The MIT Press. [Catalogue Link](https://ocul-bu.primo.exlibrisgroup.com/permalink/01OCUL_BU/1355ikl/alma991009282093205152) |
	
	""")


	
		
df = get_data()

st.image("images/logo.png")
pg = st.navigation([
	st.Page(page_intro, title="Brock Research Insights"),
	st.Page(page_total,title="Total Publications",icon="📘"),
	st.Page(page_apc,title="Article Processing Charges",icon="💲"),
	st.Page(page_green_pathways,title="Green Pathways", icon="📗"),
	st.Page(page_sosp,title="State of Scholarly Publishing", icon="📙"),
	st.Page(page_reading_list, title="Reading List", icon="📑")
])

pg.run()

