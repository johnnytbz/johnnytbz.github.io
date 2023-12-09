import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
from dash.dependencies import Input, Output, State
from dash_extensions import ConfirmationDialog
from dash_extensions import Download
import base64
import io

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 示例用户数据集
users_data = pd.DataFrame({
    'ID': [1, 2, 3],
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 35]
})

# 定义用户列表 DataTable 组件
users_table = dash_table.DataTable(
    id='users-table',
    columns=[{"name": col, "id": col} for col in users_data.columns],
    data=users_data.to_dict('records'),
    editable=True,
    row_deletable=True,
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        }
    ]
)


# 定义导航栏
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("首页", href="/", active="exact")),
        dbc.NavItem(dbc.NavLink("用户管理", href="/users")),
        dbc.NavItem(dbc.NavLink("设置", href="/settings")),
    ],
    brand="后台管理系统",
    brand_href="/",
    sticky="top",
)

# 定义通知组件
notifications = dbc.Alert(
    "欢迎使用后台管理系统！", color="info", dismissable=True
)

# 定义首页内容
home_content = html.Div(
    [
        html.H1("首页"),
        notifications,
    ],
    className="p-5",
)

# 定义用户管理内容
users_content = html.Div(
    [
        html.H1("用户管理"),
        html.H4("用户列表"),
        users_table,
        html.Button('保存', id='save-button', n_clicks=0),
        html.Div(id='output-message')
    ],
    className="p-5",
)

# 定义设置页面内容
settings_content = html.Div(
    [
        html.H1("设置"),
        html.H4("信息更新"),
        # 在这里添加信息更新表单组件
    ],
    className="p-5",
)

# 定义整体布局
app.layout = dbc.Container(
    [
        navbar,
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("菜单", className="display-5"),
                        dbc.Nav(
                            [
                                dbc.NavLink("首页", href="/", active="exact"),
                                dbc.NavLink("用户管理", href="/users"),
                                dbc.NavLink("设置", href="/settings"),
                            ],
                            vertical=True,
                            pills=True,
                        ),
                    ],
                    width=2,
                ),
                dbc.Col(
                    [
                        dcc.Location(id="url", refresh=False),
                        html.Div(id="page-content"),
                    ],
                    width=10,
                ),
            ],
            className="mt-4",
        ),
    ],
    fluid=True,
)


# 回调函数：根据 URL 路径切换页面内容
@app.callback(
    dash.dependencies.Output("page-content", "children"),
    [dash.dependencies.Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return home_content
    elif pathname == "/users":
        return users_content
    elif pathname == "/settings":
        return settings_content
    else:
        return dbc.Alert("404 - 页面未找到", color="danger")

# 回调函数：处理保存按钮点击事件
@app.callback(
    dash.dependencies.Output('output-message', 'children'),
    [dash.dependencies.Input('save-button', 'n_clicks')],
    [dash.dependencies.State('users-table', 'data')]
)
def save_users(n_clicks, data):
    if n_clicks > 0:
        # 将更新后的用户数据保存到数据库或进行其他操作
        updated_users_data = pd.DataFrame(data)
        return html.Div("用户数据已保存！")
    else:
        return html.Div()


if __name__ == "__main__":
    app.run_server(debug=True)