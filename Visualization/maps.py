import chart_studio.plotly.plotly as py
import plotly.express as px


def plot_choropleth_map(data_frame, output_path):
    fig = px.choropleth(data_frame, locations="country", color="cluster", hover_name="country",
                        color_continuous_scale=px.colors.sequential.Plasma,locationmode="country names")
    save_choropleth_map(fig, output_path)


def save_choropleth_map(choromap, output_path):
    py.sign_in('yiftachs', '8mssebobkc9QbLebePeP')

    py.image.save_as(choromap, filename=output_path + '/name.png')
