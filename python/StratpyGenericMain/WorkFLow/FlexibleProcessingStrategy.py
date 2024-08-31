from WorkFLow.ProcessingStrategy import ProcessingStrategy
import pandas as pd


class FlexibleProcessingStrategy(ProcessingStrategy):
    def process(self, data_tables, operations):
        temp_tables = {}  # Used to store temporary tables

        for operation in operations:
            op_type = operation['type']
            params = operation.get('params', {})

            if op_type == "join":
                left_table = temp_tables.get(params['left_table'], data_tables[params['left_table']])
                right_table = temp_tables.get(params['right_table'], data_tables[params['right_table']])

                left_table[params['on']] = left_table[params['on']].astype(str)
                right_table[params['on']] = right_table[params['on']].astype(str)

                result = left_table.merge(right_table, on=params['on'], how=params.get('how', 'inner'))
                temp_tables[params['output_table']] = result
                # {
                #     "type": "join",
                #     "params": {
                #         "left_table": "table1",
                #         "right_table": "table2",
                #         "on": ["id"],
                #         "how": "inner",
                #         "output_table": "temp1"
                #     }
                # }

            elif op_type == "filter":
                table = get_table(params['table'], temp_tables, data_tables)
                result = table.query(params['condition'])
                temp_tables[params['output_table']] = result
                # {
                #     "type": "filter",
                #     "params": {
                #         "table": "temp1",
                #         "condition": "amount > 1000",
                #         "output_table": "filtered_temp"
                #     }
                # }

            elif op_type == "group_by":
                table = get_table(params['table'], temp_tables, data_tables)
                result = table.groupby(params['columns']).apply(lambda x: x)

                temp_tables[params['output_table']] = result
                # {
                #     "type": "group_by",
                #     "params": {
                #         "table": "filtered_temp",
                #         "columns": ["category"],
                #         "output_table": "final_table"
                #     }
                # }

            elif op_type == "sum":
                table = get_table(params['table'], temp_tables, data_tables)
                result = table.sum()
                temp_tables['result'] = result
                # {
                #     "type": "sum",
                #     "params": {
                #         "table": "final_table",
                #         "columns": ["amount"]
                #     }
                # }

            elif op_type == "sort":
                table = get_table(params['table'], temp_tables, data_tables)
                result = table.sort_values(by=params['columns'], ascending=params.get('ascending', True))
                temp_tables[params['output_table']] = result
                # {
                #     "type": "sort",
                #     "params": {
                #         "table": "temp1",
                #         "columns": ["date"],
                #         "ascending": false,
                #         "output_table": "sorted_table"
                #     }
                # }

            elif op_type == "drop_duplicates":
                table = get_table(params['table'], temp_tables, data_tables)
                result = table.drop_duplicates(subset=params.get('subset', None))
                temp_tables[params['output_table']] = result
                # {
                #     "type": "drop_duplicates",
                #     "params": {
                #         "table": "table1",
                #         "subset": ["id", "date"],
                #         "output_table": "unique_table"
                #     }
                # }

            elif op_type == "select_columns":
                table = get_table(params['table'], temp_tables, data_tables)
                result = table[params['columns']]
                temp_tables[params['output_table']] = result
                # {
                #     "type": "select_columns",
                #     "params": {
                #         "table": "table1",
                #         "columns": ["id", "name", "amount"],
                #         "output_table": "selected_columns_table"
                #     }
                # }

            elif op_type == "add_column":
                table = get_table(params['table'], temp_tables, data_tables)
                table[params['new_column_name']] = eval(params['calculation'])
                temp_tables[params['output_table']] = table
                # {
                #     "type": "add_column",
                #     "params": {
                #         "table": "table1",
                #         "new_column_name": "discounted_amount",
                #         "calculation": "table['amount'] * 0.9",
                #         "output_table": "table_with_new_column"
                #     }
                # }

            elif op_type == "concat_columns":
                table = get_table(params['table'], temp_tables, data_tables)
                table[params['new_column_name']] = table[params['columns']].apply(
                    lambda row: params['separator'].join(row.values.astype(str)), axis=1)
                temp_tables[params['output_table']] = table
                # {
                #     "type": "concat_columns",
                #     "params": {
                #         "table": "table1",
                #         "columns": ["first_name", "last_name"],
                #         "separator": " ",
                #         "new_column_name": "full_name",
                #         "output_table": "table_with_full_name"
                #     }
                # }

            elif op_type == "fillna":
                table = get_table(params['table'], temp_tables, data_tables)
                table[params['columns']] = table[params['columns']].fillna(params['value'])
                temp_tables[params['output_table']] = table
                # {
                #     "type": "fillna",
                #     "params": {
                #         "table": "table1",
                #         "columns": ["amount"],
                #         "value": 0,
                #         "output_table": "filled_table"
                #     }
                # }

            elif op_type == "calculate":
                table = get_table(params['table'], temp_tables, data_tables)
                table[params['new_column']] = eval(params['expression'])
                temp_tables[params['output_table']] = table
                # {
                #     "type": "calculate",
                #     "params": {
                #         "table": "table1",
                #         "new_column": "total_price",
                #         "expression": "table['quantity'] * table['unit_price']",
                #         "output_table": "calculated_table"
                #     }
                # }

            elif op_type == "rename_columns":
                table = get_table(params['table'], temp_tables, data_tables)
                result = table.rename(columns=params['columns_map'])
                temp_tables[params['output_table']] = result
                # {
                #     "type": "rename_columns",
                #     "params": {
                #         "table": "table1",
                #         "columns_map": {"old_name": "new_name", "amount": "total_amount"},
                #         "output_table": "renamed_table"
                #     }
                # }

            elif op_type == "pivot":
                table = get_table(params['table'], temp_tables, data_tables)
                result = table.pivot(index=params['index'], columns=params['columns'], values=params['values'])
                temp_tables[params['output_table']] = result
                # {
                #     "type": "pivot",
                #     "params": {
                #         "table": "table1",
                #         "index": "date",
                #         "columns": "category",
                #         "values": "amount",
                #         "output_table": "pivot_table"
                #     }
                # }

            elif op_type == "pivot_table":
                table = get_table(params['table'], temp_tables, data_tables)
                result = pd.pivot_table(table, index=params['index'], columns=params['columns'],
                                        values=params['values'], aggfunc=params.get('aggfunc', 'sum'))
                temp_tables[params['output_table']] = result
                # {
                #     "type": "pivot_table",
                #     "params": {
                #         "table": "table1",
                #         "index": ["category"],
                #         "columns": ["date"],
                #         "values": "amount",
                #         "aggfunc": "sum",
                #         "output_table": "pivot_table"
                #     }
                # }

            elif op_type == "split_column":
                table = get_table(params['table'], temp_tables, data_tables)
                split_cols = table[params['column']].str.split(params['separator'], expand=True)
                for i, new_col in enumerate(params['new_columns']):
                    table[new_col] = split_cols[i]
                temp_tables[params['output_table']] = table
                # {
                #     "type": "split_column",
                #     "params": {
                #         "table": "table1",
                #         "column": "full_name",
                #         "separator": " ",
                #         "new_columns": ["first_name", "last_name"],
                #         "output_table": "split_table"
                #     }
                # }


            # Other operation types...

            else:
                raise ValueError(f"Unsupported operation type: {op_type}")

        return temp_tables['result']


def get_table(table_name, temp_tables, data_tables):
    if table_name in temp_tables:
        table = temp_tables[table_name]
    else:
        table = data_tables.get(table_name)
    return table
