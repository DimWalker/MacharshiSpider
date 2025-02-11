import tkinter as tk
from tkinter import ttk
import pandas as pd

class EditableTableApp:
    def __init__(self, root, dataframe):
        self.root = root
        self.root.title("Editable Table")

        self.dataframe = dataframe
        self.tree = ttk.Treeview(root, columns=list(dataframe.columns), show="headings")

        # 设置表头
        for col in dataframe.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # 插入数据
        for index, row in dataframe.iterrows():
            self.tree.insert("", "end", values=list(row))

        self.tree.pack(fill=tk.BOTH, expand=True)

        # 绑定双击事件以编辑单元格
        self.tree.bind("<Double-1>", self.on_double_click)

        # 保存按钮
        self.save_button = tk.Button(root, text="Save", command=self.save_data)
        self.save_button.pack()

    def on_double_click(self, event):
        # 获取选中的行和列
        region = self.tree.identify_region(event.x, event.y)
        if region == "cell":
            column = self.tree.identify_column(event.x)
            row_id = self.tree.identify_row(event.y)

            # 获取单元格的坐标
            column_index = int(column[1:]) - 1
            cell_value = self.tree.item(row_id, "values")[column_index]

            # 创建编辑框
            self.entry = tk.Entry(self.root)
            self.entry.insert(0, cell_value)
            self.entry.place(x=event.x, y=event.y, anchor="w")

            # 绑定回车键以保存编辑内容
            self.entry.bind("<Return>", lambda e: self.save_edit(row_id, column_index))

    def save_edit(self, row_id, column_index):
        # 获取编辑框的内容
        new_value = self.entry.get()
        self.entry.destroy()

        # 更新Treeview中的数据
        values = list(self.tree.item(row_id, "values"))
        values[column_index] = new_value
        self.tree.item(row_id, values=values)

    def save_data(self):
        # 从Treeview中获取数据并更新DataFrame
        updated_data = []
        for row_id in self.tree.get_children():
            values = self.tree.item(row_id, "values")
            updated_data.append(values)

        self.dataframe = pd.DataFrame(updated_data, columns=self.dataframe.columns)
        print("Data saved:")
        print(self.dataframe)

if __name__ == "__main__":
    # 示例数据
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"]
    }
    df = pd.DataFrame(data)

    root = tk.Tk()
    app = EditableTableApp(root, df)
    root.mainloop()