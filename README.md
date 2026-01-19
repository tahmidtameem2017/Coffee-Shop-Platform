# ☕ Coffee Shop CLI  ☕

Welcome to my personal project: a **C**ommand **L**ine **I**nterface (CLI) application designed to make managing a coffee shop's operations a breeze! From keeping track of loyal customers to brewing up new products and fulfilling orders, this tool is crafted with love (and code) to help streamline your coffee empire. ✨

## ✨ Features - What's Brewing? ✨

Here's what you can currently do with the Coffee Shop CLI:
*   **👥 Customer Management**:
    *   View all your amazing customers. 👀
    *   Add new coffee lovers to your list! ➕
    *   Say goodbye to customers (but hopefully not too often!). 🗑️

**🔜 Coming Soon :**
*   **☕ Product Management**
*   **📝 Order Management**

## 🛠️ Technologies Used 🛠️

This project is built using a blend of cool Python libraries:

*   **Python** 🐍: The main language powering this CLI.
*   **[InquirerPy](https://github.com/kazhala/InquirerPy)** 💬: For crafting those smooth, interactive command-line prompts.
*   **[Rich](https://github.com/Textualize/rich)** 🌟: Makes the terminal output look absolutely stunning and readable.
*   **[PyFiglet](https://github.com/pwaller/pyfiglet)** 🅰️: To generate awesome ASCII art banners, adding a touch of retro charm.
*   **[mysql-connector-python](https://pypi.org/project/mysql-connector-python/)** 🗄️: For robust interaction with our MySQL database.

## 🚀 Setup and Installation 🚀

### 📋 Prerequisites

Before you can run this amazing CLI, make sure you have these ingredients ready:

*   **Python 3.7+** 🐍
*   **MySQL Server** 🗄️

### ⚙️ Installation Steps

1.  **Clone this sweet repository:**
    ```bash
    git clone <your-repository-url> # Replace with your actual repo URL!
    cd CODES
    ```

2.  **Install the Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 🗃️ Database Setup 

1.  **Create a `db.json` file** in the root directory of your project. This file will hold your secret recipe (database connection details!):

    ```json
    {
        "host": "localhost",
        "port": 3306,
        "user": "your_mysql_user",
        "password": "your_mysql_password",
        "database": "coffee_shop"
    }
    ```

2.  **Whip up the `coffee_shop` database** in your MySQL server. Then, create the necessary tables with this schema:

    ```sql
    CREATE DATABASE IF NOT EXISTS coffee_shop;
    USE coffee_shop;

    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Email VARCHAR(255) UNIQUE,
        Phone VARCHAR(20)
    );

    CREATE TABLE IF NOT EXISTS Products (
        ProductID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Price DECIMAL(10, 2) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Employees (
        EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Position VARCHAR(255)
    );

    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INT AUTO_INCREMENT PRIMARY KEY,
        CustomerID INT,
        EmployeeID INT,
        OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,
        OrderStatus VARCHAR(50),
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
        FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
    );
    ```

## 🏃‍♀️ Usage 🏃‍♂️

Ready to manage your coffee shop? Just run the `main.py` file:

```bash
python main.py
```

Follow the interactive prompts (thanks, InquirerPy!) to navigate through the CLI and start managing your operations. It's super intuitive! ✨

## 🎬 Demo  🎥

<!-- Placeholder for image/gif/video demonstrating the CLI in action -->
<!-- Example: ![CLI Demo](path/to/your/demo.gif) -->
<!-- Example: <video src="path/to/your/demo.mp4" controls title="CLI Demo"></video> -->


## 📁 Project Structure  📁

*   `main.py`: The main entry point of the application, handling the CLI menu and user interaction.
*   `database.py`: Contains functions for interacting with the MySQL database, such as viewing, adding, and deleting customers, products, and orders.
*   `db.py`: Handles the connection to the MySQL database, reading credentials from `db.json`.
*   `db.json`: Configuration file for MySQL database connection details.
*   `requirements.txt`: Lists all Python dependencies required for the project.
*   `pyfigletfonts.txt`: Contains fonts used by `pyfiglet`.
