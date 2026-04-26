<h1 align="center">
  <img src="Tkable Logo.png" width="500">
</h1>

<p align="center">The simplest way to create tables in Tkinter for beginners :)</p>

## Installation
```bash
pip install tkable.
```
---

## 🔧 Customization Options

You can customize the table using the following parameters:

| Parameter           | Type       | Default                 | Description             |
|---------------------|------------|-------------------------|-------------------------|
| `header_bg`         | str        | `#2c3e50`               | Header background color |
| `header_fg`         | str        | `white`                 | Header text color       |
| `row_height`        | int        | `28`                    | Height of each row      |
| `font`              | tuple      | `("Segoe UI", 10)`      | Font used in the table  |
| `alternating_colors`| tuple      | `("#ffffff", "#f5f5f5")`| Row background colors   |

---

## 📦 API Reference

### 1 ) `insert_row(*values)`
Add a new row to the table.

**Example:**
```python
table.insert_row("Person Name", 20, "City")
```
### 2 ) `insert_dict(data: dict)`
Insert a row using a dictionary (keys must match column names).

**Example:**
```python
table.insert_dict({
    "Name": "Person Name",
    "Age": 22,
    "City": "City"
})
```
### 3 ) `load_data(data)`
Load multiple rows at once.

**Example:**
```python
table.load_data([
    ["Person 1", 20, "City 1"],
    ["person 2", 22, "City 2"]
])
```
### 4 ) `clear()`
Remove all rows from the table.

**Example:**
```python
table.clear()
```
### 5 ) `get_selected_row()`
Return the selected row as a dictionary.
Returns None if nothing is selected.

**Example:**
```python
selectedRow = table.get_selected_row()
```


> 💡 Tip: Use `insert_dict()` when working with forms for cleaner code.

---

## Features:
```markdown
- Easy to use
- Insert rows or dictionaries
- Column sorting
- Alternating row colors
- Scrollable table
```
---

## Example Usage

```python
from tkable import DataTable

root = tk.Tk()
root.title("Tkinter DataTable Demo")
root.geometry("600x400")

# Initialize The Table:
#                  Screen           Rows          Header Color (optional)           Row Colors (optional)
table = DataTable(root, ["Name", "Age", "City"], header_bg="#ff004c" , alternating_colors=("#ffffff", "#ffcadc"))

# --- Form --- 
form = tk.Frame(root)
form.pack(pady=10)

name_var = tk.StringVar()
age_var = tk.StringVar()
city_var = tk.StringVar()

tk.Label(form, text="Name").grid(row=0, column=0)
tk.Entry(form, textvariable=name_var).grid(row=0, column=1)

tk.Label(form, text="Age").grid(row=0, column=2)
tk.Entry(form, textvariable=age_var).grid(row=0, column=3)

tk.Label(form, text="City").grid(row=0, column=4)
tk.Entry(form, textvariable=city_var).grid(row=0, column=5)


def add_data():
    if not name_var.get():
        messagebox.showwarning("Input Error", "Name is required!")
        return
    elif not age_var.get():
        messagebox.showwarning("Input Error", "Age is required!")
        return
    elif not city_var.get():
        messagebox.showwarning("Input Error", "City is required!")
        return

    table.insert_dict(
        {
            "Name": name_var.get(),
            "Age": age_var.get(),
            "City": city_var.get()
        }
    )

    # Clear inputs
    name_var.set("")
    age_var.set("")
    city_var.set("")


tk.Button(root, text="Add Data", command=add_data).pack(pady=5)

# Sample data
table.load_data([
    ["Person 1", 20, "City 1"],
    ["Person 2", 22, "City 2"]
])

root.mainloop()
```
![Result Screenshot]()
