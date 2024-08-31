从数据加载到报告生成的流程图：

**流程图说明**

***数据加载（Loader）***
~~~
输入：配置文件 (config.json)
过程：根据配置文件中定义的文件路径和加载器类型，加载数据到内存。
输出：数据表 (data_tables)
~~~

***数据处理（FlexibleProcessingStrategy）***
~~~
输入：数据表 (data_tables)，操作列表 (operations)
过程：
执行配置文件中定义的操作（如连接、添加列、分组等）。
在处理过程中，使用临时表 (temp_tables) 存储中间结果。
输出：处理后的数据表 (results)
~~~

***报告生成（ReportGenerator）***
~~~
输入：处理后的数据表 (results)，输出格式 (output_format)，自定义文件名 (custom_file_name)
过程：
根据输出格式生成最终报告（如 Excel 或 CSV）。
在 Excel 文件中调整列宽以适应内容。
输出：生成的报告文件
~~~
**流程图**
~~~
+----------------+       +---------------------------+       +-----------------+
|                |       |                           |       |                 |
|   Load Data    |       |  Flexible Processing      |       | Generate Report |
|   (Loader)     |       |      Strategy             |       | (ReportGenerator)|
|                |       |                           |       |                 |
+-------+--------+       +-------------+-------------+       +--------+--------+
        |                          |                                 |
        |                          |                                 |
        v                          v                                 v
+-------+--------+       +---------+-----------+           +--------+--------+
|                |       |                     |           |                 |
|   Data Tables  |-----> |   Operations        |---------> |   Output Format  |
|                |       |   (temp_tables)     |           |   & Custom File  |
+----------------+       +---------+-----------+           |   Name           |
                                          |                +--------+--------+
                                          v                         |
                                +---------+-----------+           v
                                |  Processed Results   |<----------+
                                +----------------------+
~~~

**详细描述**

***数据加载（Loader）：***
~~~
从配置文件 (config.json) 中读取输入文件的信息。
根据文件类型（如 .txt, .csv）和加载器类型（如 TxtLoader, CSVLoader），加载数据。
加载的数据表 (data_tables) 用于后续处理。
~~~

***数据处理（FlexibleProcessingStrategy）：***
~~~
读取数据表 (data_tables) 和操作列表 (operations)。
根据操作类型（如 join, add_column, group_by），对数据表执行相应的操作。
在处理过程中，使用临时表 (temp_tables) 存储中间结果。
最终生成的处理结果表 (results) 用于报告生成。
~~~

***报告生成（ReportGenerator）：***
~~~
读取处理后的数据表 (results)，并根据输出格式（如 excel, csv）生成报告。
在 Excel 报告中，调整列宽以适应内容。
使用自定义文件名 (custom_file_name) 创建最终的报告文件。
~~~