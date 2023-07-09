import pandas as pd  # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import matplotlib.pyplot as plt
from PIL import Image
import os
from pathlib import Path
import csv

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard",
                   page_icon=":bar_chart:", layout="wide")

@st.cache_data
def get_data_from_excel():
    df = pd.read_csv('bharatpur_lsti.csv')

    return df


df = get_data_from_excel()

@st.cache_data
def image_open(filename):
    image_path=f'{Path(__file__).parent}/maps/{filename}.png'
    image1 = Image.open(image_path)

    st.image(image1, use_column_width='always',caption=f'Map for {filename}')
# st.dataframe(df)

# ----------------------------------------------------------------
st.sidebar.header('Please Filter here')



# customer_type = st.sidebar.multiselect(
#     "Select the Customer Type:",
#     options=df["Customer_type"].unique(),
#     default=df["Customer_type"].unique(),
# )

# gender = st.sidebar.multiselect(
#     "Select the Gender:",
#     options=df["Gender"].unique(),
#     default=df["Gender"].unique()
# )

# df_selection = df.query(
#     "Class_2021 == @class_2021 & Customer_type ==@customer_type & Gender == @gender"
# )

@st.cache_data
def plot_box(Lst,Lulc):
    a = df[Lst].groupby(by=df[Lulc]).describe()
    fig, ax = plt.subplots(1, 1, figsize=(12, 7))
    box_colors = ['green', 'cyan', 'red', 'yellow', 'brown']
    bp = ax.boxplot(a.drop(columns=['count', 'std']).transpose(), showfliers=False, patch_artist=True, whis=1.5, showmeans=True, meanline=True, meanprops={
                    'color': 'black'}, medianprops={'color': 'black'}, whiskerprops={'color': 'black'}, labels=['Forest', 'Water', 'Builtup', 'Agriculture', 'Uncultivated'])
    for patch, color in zip(bp['boxes'], box_colors):
        patch.set_facecolor(color)

    ax.grid(True, color='gray', linestyle='--', linewidth=0.5)
    plt.style.use('seaborn')
    plt.xlabel("Land Cover Classes")
    plt.ylabel("Land Surface Temperature")
    plt.title("Box plot showing LST for several Land Cover Classes")
#   Add a border to the plot
    ax.set_frame_on(True)
    ax.spines['top'].set_visible(True)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)
    ax.spines['right'].set_visible(True)

    
    # Customize the border linewidth
    ax.spines['top'].set_linewidth(1)
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['left'].set_linewidth(1)
    ax.spines['right'].set_linewidth(1)
    st.pyplot(fig)

st.title(":bar_chart: Analyzing Urban Growth Patterns and Urban Heat Islands")

st.markdown("## A Case Study of Bharatpur Metropolitan City,Nepal")
st.markdown("### Master Thesis, Geoinformatics, University of Münster")
st.markdown("-----------")
# ---- MAINPAGE ----
st.markdown('<h3>Abstract:</h3><p align="justify"> Determination of spatial extent of the earth’s features, spectral coverage, and temporal analysis of geographic features has been used to delineate the ecological degradation and distortions in the earth’s landscape with high precision using the advanced image processing sensor of satellites. Rapid population growth, urban growth, deforestation, and deterioration of the natural resources has been occurring at a very high rate causing unnatural climate changes like drought and rapid increase in the surface temperature of the earth’s surface and hence producing highly heated zones called Urban Heat Island. Urban Heat Island deteriorates the ecological process, biological habitats, soil composition, climate structure, environmental cycles, and resident health. The focus of this study project is to perform spatiotemporal analysis of the land cover categories, statistical analysis of densely accumulated Land Surface Temperature (LST), determination of the Urban Heat Island (UHI) effect, and comparative analysis of Land Cover Categories (LCC) and Urban Heat Island (UHI) effects occurring across the various regions of Bharatpur metropolitan city. Landsat 8 images were acquired from the USGS portal and then preprocessed using the GIS tool. A supervised classification algorithm was performed to derive land cover classes, while a single window algorithm and LST thresholding was used to generate different urban heat island zones. Correlation between remote sensing indices and land surface temperature was estimated to check the driving factors for Urban Heat Island. Effect in different time. It was verified by determining the land surface temperature distribution for different land cover categories. The results show that Builtup and uncultivated areas were increasing rapidly in the compensation of forest and agriculture areas. High moisture coverage in water bodies, forests, and agriculture contributed to nonUHI. Low UHI was found in sparsely distributed Builtup and uncultivated areas, while clustered Builtup and uncultivated areas were in dense UHI zones. This project will serve as a reference for spatiotemporal and statistical analysis for detecting land cover trends, Urban Heat Island occurrence and, surface temperature distribution across different land surface features.</p>',unsafe_allow_html=True)
st.markdown("-----------")
st.markdown('### Area of Interest')
image_open("Bharatpur")
st.markdown("-----------")
st.markdown('### Land Cover Map,Land Surface Temperature Map and Urban Heat Islands Map')
lulc_map = st.sidebar.selectbox(
    "Select LULC map",
    options=["21lulc", "19lulc",
             "17lulc", "15lulc", "13lulc"]
)

uhi = st.sidebar.selectbox(
    "Select UHI map",
    options=["21uhi", "19uhi",
             "17uhi", "15uhi", "13uhi"]
)

lsti = st.sidebar.selectbox(
    "Select LST map",
    options=["21lst", "19lst",
             "17lst", "15lst", "13lst"]
)

all_maps = st.sidebar.selectbox(
    "Select map or plot type",
    options=["all_ndmi", "all_ndvi",
             "all_urban", "uhi_all", "all_lst"]
)

profile = st.sidebar.selectbox(
    "Select map or plot type",
    options=["LULC_profile", "LST_profile"]
)


m1,m2,m3,m4,m5 = st.columns([0.4,0.04,0.4,0.04,0.4])
with m1:
    image_open(lulc_map)

with m3:
    image_open(uhi)

with m5:
    image_open(lsti)

st.markdown('----')
st.markdown(f"### Maps ({all_maps}) in one frame")
image_open(all_maps)

st.markdown('----')
st.markdown(f"### {profile} plot in one frame")
image_open(profile)
st.markdown('----')
Lulc= st.sidebar.selectbox(
    "Select a class",
    options=["class_2021", "class_2019",
             "class_2017", "class_2015", "class_2013"]
)

Lst = st.sidebar.selectbox(
    "Select LST",
    options=["LST_2021", "LST_2019",
             "LST_2017", "LST_2015", "LST_2013"]
)
c1,c3,c2=st.columns([0.4,0.1,0.4])


with c1:
    plot_box(Lst,Lulc)
  


pie = st.sidebar.selectbox(
    "Select UHI pie chart",
    options=["UHI_pie_2013", "UHI_pie_2015",
             "UHI_pie_2017", "UHI_pie_2019", "UHI_pie_2021"]
)
with c2:
    image_open(pie)
st.markdown('----')
st.markdown('### Statistical plots')
g1,g2,g3=st.columns([0.4,0.1,0.4])
bars = st.sidebar.selectbox(
    "Select bar plots",
    options=["class_plot","Lanc_cover_change"]
)
with g1:
    image_open(bars)

with g3:
    image_open("indices_lst_correlation")


st.markdown('----')

# ---- READ EXCEL ----
# Initialize like and comment counts

def load_data():
    try:
        data = pd.read_csv("comments_like.csv")
    except FileNotFoundError:
        data = pd.DataFrame({'Likes': [0], 'Comments': [None], 'Comments_count': 0})
    return data


def save_comment(data, comment):
    comment_df = pd.DataFrame({'Comments': [comment]})
    data = pd.concat([data, comment_df], ignore_index=True)
    data['Comments_count'] = len(data)-1
    return data


def save_data(data):
    data.to_csv("comments_like.csv", index=False)


data = load_data()
# Display the like button
if 'Likes' not in data.columns:
    data['Likes'] = 0
#st.button("Like")
if st.button("Like"):
    data.loc[0, 'Likes'] += 1


# Display the comment input
comment = st.text_input("Add a comment:")
if st.button("Save Comment"):
    data = save_comment(data, comment)


# Display the likes count, comment count, and comments
st.write(f"Likes: {int(data.loc[0, 'Likes'])}")
st.write(f"Comment count: {len(data) - 1}")
if data["Comments"].empty or data["Comments"] is None:
    st.write("Comments:")
else:
    for index,value in enumerate(data['Comments'].dropna()):
            st.write(f'Comments {index+1}: {value}')

# Save data to CSV
save_data(data)

# File path for storing the view count
VIEW_COUNT_FILE = "view_count.csv"

@st.cache_data
def increment_view_count():
    # Check if the file exists
    if not os.path.isfile(VIEW_COUNT_FILE):
        # Create the file and initialize the count to 0
        with open(VIEW_COUNT_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["count", 0])

    # Read the current count
    with open(VIEW_COUNT_FILE, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if not rows or len(rows[0]) < 2:
        # Handle empty file or missing count value
        count = 0
    else:
        count = int(rows[0][1])

    # Increment the count
    count += 1

    # Update the count in the file
    with open(VIEW_COUNT_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["count", count])

    return count


# Get the current view count
view_count = increment_view_count()


st.write("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/bootstrap-icons.min.css" rel="stylesheet">    
""", unsafe_allow_html=True)
# st.write(f"Likes: <i class='bi bi-eye-fill'></i>{like_count}",unsafe_allow_html=True)
# st.write(f"Comments: <i class='bi bi-pen-fill'></i>{comment_count}",unsafe_allow_html=True)
st.write(f"Views: <i class='bi bi-eye-fill'></i>{view_count}",unsafe_allow_html=True)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.write('© 2023 Surendra Shiwakoti. All rights reserved.')
