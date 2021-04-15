![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

# .csv file --> html table via flask

### 1. Create virtual environment:
* $ python -m venv venv
* $ . venv/bin/activate

### 2. Install Flask & Pandas:
* $ pip install Flask
* $ pip install pandas

### 3. Clone repo:
* $ git clone [url]

### 4. Headers and rows created via for loop:

```Python
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
