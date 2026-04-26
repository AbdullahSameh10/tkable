import tkinter as tk
from tkinter import ttk

class DataTable:
    def __init__(self, parent, columns, *, header_bg="#2c3e50", header_fg="white", row_height=28, font=("Segoe UI", 10), alternating_colors=("#ffffff", "#f5f5f5"),):
        self.parent = parent
        self.columns = columns
        self.data = []

        self.header_bg = header_bg
        self.header_fg = header_fg
        self.row_height = row_height
        self.font = font
        self.alt_colors = alternating_colors

        self._build_ui()

    def _build_ui(self):
        container = tk.Frame(self.parent)
        container.pack(fill=tk.BOTH, expand=True)

        # --- Table Frame ---
        frame = tk.Frame(container)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        style = ttk.Style()
        style.theme_use("default") 

        style.configure(
            "Custom.Treeview.Heading",
            background=self.header_bg,
            foreground=self.header_fg,
            font=(self.font[0], self.font[1], "bold"),
        )

        style.configure(
            "Custom.Treeview",
            rowheight=self.row_height,
            font=self.font,
        )

        self.tree = ttk.Treeview(
            frame,
            columns=self.columns,
            show="headings",
            style="Custom.Treeview"
        )

        for col in self.columns:
            self.tree.heading(col, text=col, command=lambda c=col: self._sort_by_column(c))
            self.tree.column(col, anchor="center", width=120)

        # Scrollbars
        y_scroll = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        x_scroll = ttk.Scrollbar(frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

        # Row colors
        self.tree.tag_configure("row0", background=self.alt_colors[0])
        self.tree.tag_configure("row1", background=self.alt_colors[1])

    # ---------------- PUBLIC API ---------------- #

    def insert_row(self, *values):
        if len(values) != len(self.columns):
            raise ValueError("Invalid number of values")
        self.data.append(list(values))
        self._refresh_view()

    def insert_dict(self, data: dict):
        row = [data.get(col, "") for col in self.columns]
        self.insert_row(*row)

    def load_data(self, data):
        self.data = [list(row) for row in data]
        self._refresh_view()

    def clear(self):
        self.data.clear()
        self._refresh_view()

    def get_selected_row(self):
        selected = self.tree.selection()
        if not selected:
            return None
        return dict(zip(self.columns, self.tree.item(selected[0], "values")))

    # ---------------- INTERNAL ---------------- #

    def _refresh_view(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for i, row in enumerate(self.data):
            tag = f"row{i % 2}"
            self.tree.insert("", "end", values=row, tags=(tag,))

    def _sort_by_column(self, col):
        idx = self.columns.index(col)

        if not hasattr(self, "_sort_states"):
            self._sort_states = {}

        # Toggle per column
        self._sort_states[col] = not self._sort_states.get(col, False)

        reverse = self._sort_states[col]

        try:
            self.data.sort(
                key=lambda r: float(r[idx]),
                reverse=reverse
            )
        except:
            self.data.sort(
                key=lambda r: str(r[idx]).lower(),
                reverse=reverse
            )

        self._refresh_view()