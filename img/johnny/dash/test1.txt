import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MATERIA])

# 示例用户数据集
users_data = pd.DataFrame({
    'ID': [1, 2, 3],
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 35]
})

# 定义用户列表 DataTable 组件
users_table = dash_table.DataTable(
    id='users-table',
    columns=[{"name": col, "id": col, 'deletable': True, 'renamable': True} for col in users_data.columns],
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

# 定义修改弹出框
edit_modal = dbc.Modal(
    [
        dbc.ModalHeader("编辑用户"),
        dbc.ModalBody(
            [
                dbc.Input(id='edit-id', type='text', style={'display': 'none'}),
                dbc.CardGroup(
                    [
                        dbc.Label("姓名"),
                        dbc.Input(id='edit-name', type='text')
                    ],
                    className="mr-3",
                ),
                dbc.CardGroup(
                    [
                        dbc.Label("年龄"),
                        dbc.Input(id='edit-age', type='number')
                    ],
                    className="mr-3",
                )
            ]
        ),
        dbc.ModalFooter(
            [
                dbc.Button("取消", id="edit-cancel-button", className="mr-2"),
                dbc.Button("保存", id="edit-save-button", className="mr-2")
            ]
        ),
    ],
    id="edit-modal",
    centered=True,
)

# 定义删除确认框
delete_confirmation = dbc.Modal(
    [
        dbc.ModalHeader("确认删除"),
        dbc.ModalBody("您确定要删除该用户吗？"),
        dbc.ModalFooter(
            [
                dbc.Button("取消", id="delete-cancel-button", className="mr-2"),
                dbc.Button("删除", id="delete-confirm-button", className="mr-2", color="danger")
            ]
        ),
    ],
    id="delete-confirmation",
    centered=True,
)

# 定义用户管理内容
users_content = html.Div(
    [
        html.H1("用户管理"),
        html.H4("用户列表"),
        users_table,
        html.Button('新增用户', id='add-button', className='mr-2'),
        html.Div(id='output-message'),
        edit_modal,
        delete_confirmation
    ],
    className="p-5",
)

# 定义整体布局
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Location(id="url", refresh=False),
                        dbc.Nav(
                            [
                                html.H2("菜单", className="display-5"),
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
    Output("page-content", "children"),
    [Input("url", "pathname")]
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
    Output('edit-modal', 'is_open'),
    Output('edit-modal', 'data'),
    [Input('edit-save-button', 'n_clicks'), Input('edit-cancel-button', 'n_clicks')],
    [State('edit-id', 'value'), State('edit-name', 'value'), State('edit-age', 'value')]
)
def save_edit_modal(n_clicks_save, n_clicks_cancel, user_id, name, age):
    if n_clicks_save:
        # 在这里执行保存用户编辑的逻辑
        # 根据 user_id 更新用户数据
        users_data.loc[users_data['ID'] == int(user_id), '姓名'] = name
        users_data.loc[users_data['ID'] == int(user_id), '年龄'] = age

        return False, None  # 关闭编辑弹出框

    if n_clicks_cancel:
        return False, None  # 关闭编辑弹出框

    return False, None  # 默认情况下关闭编辑弹出框


# # 回调函数：处理删除按钮点击事件
# @app.callback(
#     Output('delete-confirmation', 'is_open'),
#     Output('delete-confirmation', 'data'),
#     [Input('users-table', 'active_cell')],
#     [State('users-table', 'data')]
# )
# def confirm_delete(active_cell, table_data):
#     if active_cell and active_cell['column_id'] == 'delete' and active_cell['row'] is not None:
#         user_id = table_data[active_cell['row']]['ID']
#         return True, user_id  # 打开删除确认框
#
#     return False, None  # 默认情况下关闭删除确认框


# 回调函数：处理删除确认框中的按钮点击事件
# 回调函数：处理删除按钮点击事件
@app.callback(
    Output('delete-confirmation', 'is_open'),
    Output('delete-confirmation', 'data'),
    [Input('delete-confirm-button', 'n_clicks'), Input('delete-cancel-button', 'n_clicks')],
    [State('users-table', 'selected_row_ids')]
)
def handle_delete_confirmation(n_clicks_confirm, n_clicks_cancel, selected_rows):
    if n_clicks_confirm:
        if selected_rows:
            # 删除确认按钮被点击并且有选中的行
            user_id = int(selected_rows[0])
            name = users_data.loc[users_data['ID'] == user_id, '姓名'].values[0]
            users_data = users_data.loc[users_data['ID'] != user_id]
            message = f"用户 {name} 已删除。"
        else:
            # 删除确认按钮被点击但没有选中的行
            message = "请选择要删除的用户。"
        return False, None  # 关闭确认框
    elif n_clicks_cancel:
        # 取消按钮被点击
        return False, None
    else:
        return False, None

if __name__ == '__main__':
    app.run_server(debug=True)