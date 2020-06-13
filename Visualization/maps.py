import chart_studio.plotly.plotly as py
import plotly.express as px
import country_converter as coco

def add_countries_codes(data_frame):
        data_frame['country_code'] = coco.convert(names=list(data_frame['country']),to='ISO3')
        return data_frame



def plot_choropleth_map(data_frame, output_path):
    data_frame = add_countries_codes(data_frame)
    fig = px.choropleth(data_frame, locations="country_code", color="cluster", hover_name="country",
                        color_continuous_scale=px.colors.sequential.Plasma)
    # fig.show()
    save_choropleth_map(fig, output_path)


def save_choropleth_map(choromap, output_path):
    py.sign_in('yiftachs', '8mssebobkc9QbLebePeP')

    py.image.save_as(choromap, filename=output_path+'/name.png')
