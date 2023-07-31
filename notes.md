## bashrc and zshrc

`bashrc` and `zshrc` are configuration files used by the Bash and Zsh shells, respectively. These files allow users to customize the behavior of their shell environment by setting various environment variables, defining aliases, and creating shell functions.

1. `bashrc`: This is the configuration file used by the Bash shell, which is the default shell for many Unix-based systems, including Linux and macOS. When a user starts a new interactive Bash shell, the commands and settings in the `bashrc` file are executed, allowing users to customize their shell experience. It is typically located in the user's home directory and named `.bashrc`. However, if it doesn't exist, Bash will also look for `.bash_profile` and `.profile`.
   
   Users can edit the `bashrc` file to set environment variables, add directories to the `PATH`, define aliases (shortcuts for longer commands), configure the shell prompt appearance, and more. It's a handy way to tailor the shell to individual preferences and specific workflow needs.

2. `zshrc`: This is the configuration file used by the Zsh shell, which is an extended and more feature-rich shell compared to Bash. Zsh provides various improvements, such as advanced tab completion, improved globbing, and better customization options.
   
   Similar to `bashrc`, the `zshrc` file allows users to set environment variables, define aliases, modify the prompt appearance, and configure various other shell behaviors. It is also typically located in the user's home directory and named `.zshrc`.      
   
     

## source ./zshrc

The command `source ./zshrc` is used to execute (or "source") the contents of the `zshrc` file in the current shell session. When you run this command, it reads and applies the configurations specified in the `zshrc` file immediately, without the need to start a new shell session.

In Unix-based systems, when you make changes to the `zshrc` file (or any other shell configuration file) to update your shell environment settings, you typically have two options to apply those changes:

1. Close the current shell session and start a new one: When you open a new shell, it reads the updated `zshrc` file and applies the changes.
2. Use the `source` or `.` command to apply changes in the current shell: By running `source ./zshrc` or `. ./zshrc`, you effectively execute the commands within the `zshrc` file in the current shell context. This means any changes you made in the `zshrc` file will take effect immediately without needing to open a new shell.

Using `source` or `.` is particularly useful when you want to test your changes quickly without the inconvenience of restarting the shell. It's also essential when you want to set environment variables or define aliases that should be available in the current shell session.

Remember that `zshrc` is specific to the Zsh shell, and if you are using Bash, the equivalent file is `.bashrc`. When making changes to `.bashrc`, you can use the same `source` command to apply the updates in the current Bash shell session.

## history command

In Linux, the `history` command is used to view and manage the command history of the current user's shell session. It allows you to review previously executed commands, repeat them, search for specific commands, and perform other operations related to command history. Here are some common usages of the `history` command:

1. View Command History:
   To view the list of previously executed commands along with their line numbers, simply type `history` in the terminal and press Enter. The most recent commands will be displayed at the bottom of the list.

2. Repeat a Command:
   You can repeat a specific command from the history by using the exclamation mark (`!`) followed by the command's line number. For example, to repeat the command from line 10, you can use `!10`.

3. Repeat Last Command:
   To repeat the last command you executed, use `!!`. This is a quick way to re-run the previous command without having to search for its line number.

4. Search History:
   You can search for a specific command in the history by using the `Ctrl+R` keyboard shortcut. This will open an interactive search, where you can start typing the command you're looking for, and the shell will suggest the most recent match.

5. Execute Previous Command Starting with Specific Text:
   If you want to re-run the last command that starts with a particular text, you can use `!text`. For examFor example, `!ls` will execute the last command that started with "ls."

6. Execute Nth Occurrence of a Command Starting with Specific Text:
   To execute the Nth occurrence of a command that starts with specific text, you can use `!n:text`. For instance, `!2:ls` will run the second command that started with "ls."

7. Clear Command History:
   If you want to clear the command history, you can use the `history -c` command. This will remove all the entries from the history.

8. Control the SizeControl the Size of Command History:
   By default, most Linux distributions save a certain number of commands in the history. You can set or change the number of commands saved using the `HISTSIZE` environment variable. For example, to save the last 1000 commands in the history, you can add `export HISTSIZE=1000` to your `.bashrc` or `.zshrc` file.
   
   Keep in mind that the command history is specific to each user's shell session, and it may differ for different users on the same system. The history functionality is particularly useful for recalling previously executed commands, repeating complex commands, and avoiding retyping frequently used commands.

## API

### RESP

GET and POST are two of the most commonly used HTTP methods in RESTful APIs. They serve different purposes and have distinct characteristics:

1. GET:
   
   - Purpose: The GET method is used to retrieve data from the server. It is meant for reading and fetching resources without modifying them on the server side. It is safe, meaning it should not have any side effects on the server's data.
   
   - 1. - Characteristics:
          - The data is sent as part of the URL's query parameters.
          - GET requests are visible in the browser's address bar and can be bookmarked.
          - They should not contain sensitive data, as the information is exposed in the URL.
          - Caching of GET requests is possible because they are idempotent (multiple identical requests should have the same effect as a single request).
     
     2. POST:
        
        - Purpose: The POST method is used to send data to the server to create new resources or trigger actions that modify server-side data. It is used for submitting data that may contain sensitive information.
        - Characteristics:
          - The data is sent in the request body (not visible in the URL).
          - POST requests are not visible in the browser's address bar and cannot be bookmarked.
          - They are not idempotent, meaning making the same request multiple times may result in different outcomes or create multiple resources.
          - POST requests are not cached by default.

## Basic Pandas Functions and Attributes

pd.read_csv()

The `read_csv` function is simple way to read csv (comma separated values) files, which is a commonly used file format for storing data.

```python
import pandas as pd
df = pd.read_csv('data.csv')
```

df.head()

The `head()` method returns the first n rows. If no parameter is specified, the number of rows defaults to 5.

df.describe()

The `describe()` method generates descriptive statistics.

astype()

The `astype()` method is used to cast a Pandas object to a particular data type.

to_datetime()

The `to_datetime()` function converts a Python object to datetime format.

value_counts()

The `value_counts()` method returns a Pandas Series containing the count of unique values.

drop_duplicates()

The `drop_duplicates()` method returns a Pandas DataFrame with duplicate rows removed.

groupby()

The `groupby()` method is used to group a Pandas DataFrame by 1 or more columns, and perform some mathematical operation on it.

fillna()

The `fillna()` method helps to replace all NaN values in a DataFrame or Series by imputing these missing values with more appropriate values.

merge()

The `merge()` method is used to merge two Pandas DataFrame objects or a DataFrame and a Series object on a common column (field).

sort_values()

The `sort_values()` method is used to sort columns in a Pandas DataFrame (or a Pandas Series) by values in ascending or descending order.

## change environment variables

1. vim ~/.zshrc

2. 找到位置, i

3. 修改, 退出命令模式, esc

4. :q! 退出不保存修改/ :wq退出,保存修改

5. source ~/.zshrc 生效

6. cat .zshrc 列出所有api key

7. echo $FOURSQUARE_ID 想查看哪个就echo哪个

## Pandas

### Operating on NULL Values

- `isnull()`: Generate a boolean mask indicating missing values
- `notnull()`: Opposite of `isnull()`
- `dropna()`: Return a filtered version of the data
- `fillna()`: Return a copy of the data with missing values filled or imputed



## Python's Collection Module

- [Counter](https://stackabuse.com/introduction-to-pythons-collections-module/#thecounter)
- [defaultdict](https://stackabuse.com/introduction-to-pythons-collections-module/#thedefaultdict)
- [OrderedDict](https://stackabuse.com/introduction-to-pythons-collections-module/#theordereddict)
- [deque](https://stackabuse.com/introduction-to-pythons-collections-module/#thedeque)
- [ChainMap](https://stackabuse.com/introduction-to-pythons-collections-module/#thechainmap)
- [namedtuple()](https://stackabuse.com/introduction-to-pythons-collections-module/#thenamedtuple)

### Counter

**Counter** is a subclass of dictionary object.

```python
from collections import Counter

# Create Counter Objects
cnt = Counter()

# You can pass an iterable (list) to Counter() function to create a counter object.

list = [1,2,3,4,1,2,6,7,3,8,1]
Counter(list)

# Counter({1:3,2:4})
# You can access any counter item with its key as shown below:
list = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list)
print(cnt[1])

# 3
```

Apart from that, `Counter` has three additional functions:

1. Elements
   
   You can get the items of a `Counter` object with `elements()`function. It returns a list containing all the elements in the `Counter` object.
   
   ```python
   cnt = Counter({1:3,2:4})
   print(list(cnt.elements()))
   
   # output: [1, 1, 1, 2, 2, 2, 2]
   ```
   
   
2. Most_common([n])
   
   The `Counter()` function returns a dictionary which is unordered. You can sort it according to the number of counts in each element using `most_common()` function of the `Counter`object.
   
   ```python
   list = [1,2,3,4,1,2,6,7,3,8,1]
   cnt = Counter(list)
   print(cnt.most_common())
   
   # output: [(1, 3), (2, 2), (3, 2), (4, 1), (6, 1), (7, 1), (8, 1)]
   ```
   
   
3. Subtract([interable-or-mapping])
   
   The `subtract()` takes iterable (list) or a mapping (dictionary) as an argument and deducts elements count using that argument. Check the following example:
   
   ```python
   cnt = Counter({1:3,2:4})
   deduct = {1:1, 2:2}
   cnt.subtract(deduct)
   print(cnt)
   
   # output: Counter({1: 2, 2: 2})
   ```
   
   

### The Defaultdict

The `defaultdict` works exactly like a python dictionary, except for it does not throw `KeyError` when you try to access a non-existent key.

```python
from collections import defaultdict
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
print(nums['three'])
# output: 0

# example: name list: 

count = defaultdict(int)
names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
for names in names_list:
    count[names] +=1
print(count)

output: defaultdict(<class 'int'>, {'Mike': 5, 'Britney': 1, 'John': 3, 'Smith': 2, 'Anna': 2})
```



### The OrderedDict

`OrderedDict` is a dictionary where keys maintain the order in which they are inserted, which means if you change the value of a key later, it will not change the position of the key.

```python
from collections import OrderedDict

# create a OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)
# output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
for key, value in od.items():
    print(key, value)


list = ["a","c","c","a","b","a","a","b","c"]
cnt = Counter(list)
od = OrderedDict(cnt.most_common())
for key, value in od.items():
    print(key, value)

```

### The deque

The `deque` is a list optimized for inserting and removing items.

```python
from collections import deque
list = ["a","b","c"]
deq = deque(list)
print(deq)
# output: deque(['a', 'b', 'c'])

# insert element
deq.append("d")
deq.appendleft("e")
print(deq)deque
# output: deque(['e', 'a', 'b', 'c', 'd'])

# remove element
deq.pop()
deq.popleft()
print(deq)
#output: deque(['a', 'b', 'c'])

# clearing a deque
list = ["a","b","c"]
deq = deque(list)
print(deq)
print(deq.clear())
# output: 
# deque(['a', 'b', 'c'])
# None


# counting elements in a deque
list = ["a","b","c"]
deq = deque(list)
print(deq.count("a"))
```



### The ChainMap

`ChainMap` is used to combine several dictionaries or mappings. It returns a list of dictionaries.

```python
from collections import ChainMap
# create a ChainMap
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print(chain_map.maps)

# output: [{'b': 2, 'a': 1}, {'c': 3, 'b': 4}]

# access values by key
print(chain_map['a']) # 1

# updates values
dict2['c'] = 5
print(chain_map.maps)

# [{'a': 1, 'b': 2}, {'c': 5, 'b': 4}]

# getting keys and values from ChainMap
dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'c' : 3, 'b' : 4 }
chain_map = ChainMap(dict1, dict2)
print (list(chain_map.keys()))
print (list(chain_map.values()))

# output:
# ['b', 'a', 'c']
# [2, 1, 3]


# adding a new dictionary to ChainMap
dict3 = {'e' : 5, 'f' : 6}
new_chain_map = chain_map.new_child(dict3)
print(new_chain_map)

output: ChainMap({'f': 6, 'e': 5}, {'a': 1, 'b': 2}, {'b': 4, 'c': 3})

```



### The namedtuple()

The `namedtuple()` returns a tuple with names for each position in the tuple.One of the biggest problems with ordinary tuples is that you have to remember the index of each field of a tuple object. This is obviously difficult. The `namedtuple` was introduced to solve this problem.

```python
from collections import namedtuple
# create a namedtuple
Student = namedtuple('Student', 'fname, lname, age')
s1 = Student('John', 'Clarke', '13')
print(s1.fname)
# output: Student(fname='John', lname='Clarke', age='13')

# changing a namedtuple using list
s2 = Student._make(['Adam','joe','18'])
print(s2)
# output: Student(fname='Adam', lname='joe', age='18')


# creating a new instance using existing instance
# The _asdict() function can be used to create an OrderedDict instance 
# from an existing instance
s2 = s1._asdict()
print(s2)
# output: OrderedDict([('fname', 'John'), ('lname', 'Clarke'), ('age', '13')])


# changing field values with _replace() function
# _replace() function creates a new instance. It does not change the value of existing instance.
s2 = s1._replace(age='14')
print(s1)
print(s2)
# output:
Student(fname='John', lname='Clarke', age='13')
Student(fname='John', lname='Clarke', age='14')
```



## How to Perform Exploratory Data Analysis or (EDA)

### 1. Importing the required libraries for EDA

```python
import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation
%matplotlib inline     
sns.set(color_codes=True)
```

### 2. Loading the data into the data frame.

```python
df = pd.read_csv("data.csv") # sep=';'
df.head(5)   # To display the top 5 rows   
df.tail(5)   # To display the bottom 5 rows       
```

### 3. Checking the types of data

```python
df.dtypes
```

### 4. Dropping irrelevant columns

```python
df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis=1)
df.head(5)
```

### 5. Renaming the columns

```python
df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price" })
df.head(5)
```

### 6. Dropping the duplicate rows

```python
df.shape


duplicate_rows_df = df[df.duplicated()]
duplicate_rows_df.shape

df.count()      # Used to count the number of rows

df = df.drop_duplicates() # after remove duplicates
df.head(5)
df.count()
```

### 7. Dropping the missing or null values

If the amount of missing values are many, replace the missing values with the mean or the average of that column, otherwise, drop them.

```python
print(df.isnull().sum())
```

```python
df = df.dropna()    # Dropping the missing values.
df.count()
print(df.isnull().sum())   # After dropping the values
```

### 8. Detecting outliers

```python
sns.boxplot(x=df['Price'])
```

### 9. Plot different features against one another(scatter), against frequency(histogram)

#### Histogram

Histogram refers to the frequency of occurrence of variables in an interval.

```python
df.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("Number of cars by make")
plt.ylabel('Number of cars')
plt.xlabel('Make');
```

#### Heat Maps

Heat Maps is a type of plot which is necessary when we need to find the dependent variables. One of the best way to find the relationship between the features can be done using heat maps.

```python
plt.figure(figsize=(10,5))
c= df.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
c
```

#### Scatterplot

We generally use scatter plots to find the correlation between two variables.

```python
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['HP'], df['Price'])
ax.set_xlabel('HP')
ax.set_ylabel('Price')
plt.show()
```



## # 7 Must-Know Data Wrangling Operations with Python Pandas

1. Handling dates
   
   ```python
   melb.Date.dtypes
   dtype('o')
   
   
   # Before converting
   melb.Date[:2]
   0    3/12/2016 
   1    4/02/2016 
   Name: Date, dtype: object
   melb['Date'] = pd.to_datetime(melb['Date'])
   # After converting
   melb.Date[:2]
   0   2016-03-12 
   1   2016-04-02 
   Name: Date, dtype: datetime64[ns]
   ```
   
   

2. Changing data type
   
   ```python
   # Before converting
   melb['Propertycount'][:2]
   0    4019.0 
   1    4019.0 
   Name: Propertycount, dtype: float64
   melb['Propertycount'] = melb['Propertycount'].astype('int')
   # After converting
   melb['Propertycount'][:2]
   0    4019 
   1    4019 
   Name: Propertycount, dtype: int64
   ```
   
   

3. Replacing values
   
   ```python
   # Before converting
   melb.Type.unique()
   array(['h', 'u', 't'], dtype=object)
   melb.Type.replace({
      'h': 'house', 'u': 'unit', 't': 'town_house'
   }, inplace=True)
   # After converting
   melb.Type.unique()
   array(['house', 'unit', 'town_house'], dtype=object)
   ```
   
   

4. Category data type
   
   ```python
   melb.Type.memory_usage()
   108768 # in bytes
   
   melb['Type'] = melb['Type'].astype('category')
   melb['Type'].memory_usage()
   13812
   ```
   
   

5. Extrating information from dates
   
   ```python
   # Extract month
   melb['Month'] = melb['Date'].dt.month
   melb['Month'][:5]
   0    3 
   1    4 
   2    4 
   3.   4 
   4    4 
   Name: Month, dtype: int64
   # Extract weekday
   melb['Date'].dt.weekday[:5]
   0    5 
   1    5 
   2    0 
   3.   0 
   4    2 
   Name: Date, dtype: int64
   ```
   
   

6. Extracting information from text
   
   ```python
   melb.Address[:5]
   0        85 Turner St 
   1     25 Bloomburg St 
   2        5 Charles St 
   3    40 Federation La 
   4         55a Park St 
   Name: Address, dtype: object
   
   
   melb['Address'].str.split(' ').str[-1]
   0    St 
   1    St 
   2    St 
   3    La 
   4    St 
   Name: Address, dtype: object
   ```
   
   

7. Standadizing the textual data
   
   ```python
   melb.Address.str.upper()[:5]
   0        85 TURNER ST 
   1     25 BLOOMBURG ST 
   2        5 CHARLES ST 
   3    40 FEDERATION LA 
   4         55A PARK ST 
   Name: Address, dtype: object
   
   
   melb.Suburb.str.capitalize()[:5]
   0    Abbotsford 
   1    Abbotsford 
   2    Abbotsford 
   3    Abbotsford 
   4    Abbotsford 
   Name: Suburb, dtype: object
   ```



## Relative path VS Absolute path in Linux

In Linux, both relative paths and absolute paths are used to specify the location of files and directories in the file system. The main difference between them lies in how they reference the location:

1. Relative Path:
   A relative path specifies the location of a file or directory relative to the current working directory (CWD). It does not start from the root directory but references the file or directory in relation to the current position in the file system hierarchy.

For example, if your CWD is `/home/user`, and you have a file named "data.txt" in the subdirectory "documents," the relative path to "data.txt" would be `documents/data.txt`.

Relative paths use special symbols to indicate the position in the file system hierarchy:

- `.` (dot) refers to the current directory.

- `..` (double dots) refers to the parent directory.
2. Absolute Path:
   An absolute path specifies the complete location of a file or directory in the file system, starting from the root directory (`/`). It provides the full path, starting from the root, to the desired file or directory.
   
   

For example, an absolute path to the same "data.txt" file mentioned earlier might be `/home/user/documents/data.txt`.

Absolute paths are complete and do not rely on the current working directory. They specify the precise location of the file or directory, regardless of where you are currently working in the file system.

When to Use Each:

- Relative paths are convenient when navigating within the same directory or its subdirectories. They are shorter and more readable. Use relative paths when you want to reference files or directories relative to your current position.
- Absolute paths are necessary when you need to reference files or directories unambiguously, regardless of your current working directory. Use absolute paths when you want to specify the exact location of a file or directory in the file system.

In general, it is good practice to use relative paths whenever possible, as they make your code more portable and easier to manage. However, some situations, such as system administration tasks or specifying files for scripts that may be run from different locations, may require the use of absolute paths to ensure accuracy and consistency.



## Json.load()  VS Json.loads()

`json.load()` is used to read JSON data from a file-like object, while `json.loads()` is used to parse JSON data from a string.




