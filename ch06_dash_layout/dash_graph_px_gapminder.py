import dash
import dash_core_components as dcc
import plotly.express as px

gapminder = px.data.gapminder()
gapminder = gapminder[gapminder["year"] == 2007]

app = dash.Dash(__name__)

app.layout = dcc.Graph(
    # ➊ figureに直接figureを渡す
    figure=px.scatter(
        gapminder,  # 利用するデータフレームの設定
        x="gdpPercap",  # x軸
        y="pop",  # y軸
        size="lifeExp",  # マーカサイズ
        hover_name="country",
        color="continent",  # マーカ色
        log_x=True,  # x軸をlogスケールに設定
        log_y=True,  # y軸をlogスケールに設定
        title="Gapminder",  # タイトル
    )
)

if __name__ == "__main__":
    app.run_server(debug=True)