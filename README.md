# Dynamically create HTML table from .csv file.

### 1. Create virtual environment:
$ python -m venv venv
$ . venv/bin/activate

### 2. Install Flask & Pandas:
$ pip install Flask
$ pip install pandas

### 3. Clone repo:
$ git clone [url]

# Headers and rows created via loop:

```
<thead>
    <tr>
      {% for col in colnames %}
      <th>{{ col }}</th>
      {% endfor %}
    </tr>
  </thead>
  <tbody>
    {% for record in records %}
    <tr>
      {% for col in colnames %}
      <td>{{ record[col] }}</td>
      {% endfor %}
    </tr>
    {% endfor %}
  </tbody>
```
