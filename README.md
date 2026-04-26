<h1 align="center">
  <img src="Tkable Logo.png" width="500">
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/status-active-success" />
  <img src="https://img.shields.io/badge/license-MIT-blue" />
  <img src="https://img.shields.io/badge/version-1.0.0-purple" />
</p>

<p align="center">
  The simplest way to create tables in Tkinter for beginners :)
</p>

---

## ✨ Why Tkable?
* No complex setup
* No Treeview headaches
* Built for beginners
* Clean API
* Works out of the box

---

## 🧠 When should you use Tkable?

✔ Learning Tkinter

✔ Building simple apps

✔ Creating dashboards

✔ Managing data visually

---

## 📦 Installation

```bash
pip install tkable
```

---

## 🚀 Quick Example

```python
from tkable import DataTable
import tkinter as tk

root = tk.Tk()

table = DataTable(root, ["Name", "Age", "City"], header_bg="#ff004c" , alternating_colors=("#ffffff", "#ffcadc"))

table.load_data([
    ["Person 1", 20, "City 1"],
    ["Person 2", 22, "City 2"]
])

root.mainloop()
```

---

### 📸 Screenshot

![Result Screenshot](Example%20Screenshot.jpg)

---

## 🔧 Customization Options

| Parameter            | Type  | Default                  | Description             |
| -------------------- | ----- | ------------------------ | ----------------------- |
| `header_bg`          | str   | `#2c3e50`                | Header background color |
| `header_fg`          | str   | `white`                  | Header text color       |
| `row_height`         | int   | `28`                     | Height of each row      |
| `font`               | tuple | `("Segoe UI", 10)`       | Font used in the table  |
| `alternating_colors` | tuple | `("#ffffff", "#f5f5f5")` | Row background colors   |

---

## 📦 API Reference

### `insert_row(*values)`

Add a new row to the table.

```python
table.insert_row("Person Name", 20, "City")
```

---

### `insert_dict(data: dict)`

Insert a row using a dictionary.

```python
table.insert_dict({
    "Name": "Person Name",
    "Age": 22,
    "City": "City"
})
```

---

### `load_data(data)`

Load multiple rows.

```python
table.load_data([
    ["Person 1", 20, "City 1"],
    ["Person 2", 22, "City 2"]
])
```

---

### `clear()`

Remove all rows.

```python
table.clear()
```

---

### `get_selected_row()`

Return selected row as dictionary.

```python
selected = table.get_selected_row()
```

<br>
<br>

> 💡 Tip: Use `insert_dict()` when working with forms for cleaner code.

<br>

---

## 🤝 Contributing

Pull requests are welcome!

---

## ⭐ Support

If you like this project, give it a star ⭐

It helps a lot!

---

## 📄 License

MIT License © Abdullah Sameh
