# Hotel Management System

## Overview
This project implements a simple command-line-based Hotel Management System using Python and MySQL. It allows for the management of customer data, room bookings, and calculation of various bills (room, restaurant, laundry, games). The system aims to streamline basic hotel operations and provide a clear record-keeping mechanism.

## Features
- **Customer Management:** Add, view, search, update, and delete customer records.
- **Room Booking:** Book rooms for customers, assign random room numbers, and calculate room rent based on stay duration and room type.
- **Billing System:** Calculate bills for:
  - Room charges
  - Restaurant services
  - Laundry services
  - Game activities
- **Data Persistence:** All customer and booking data is stored in a MySQL database.
- **User-Friendly Interface:** Simple command-line interface for easy interaction.

## Technologies Used
- **Python 3.x:** The primary programming language.
- **MySQL:** Relational database management system for storing hotel data.
- **`mysql-connector-python`:** Python library to connect and interact with MySQL database.

## Setup Instructions
To get this project up and running on your local machine, follow these steps:

### 1. Prerequisites
- **Python 3.x:** Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).
- **MySQL Server:** Install and run a MySQL server. You can download it from [mysql.com](https://dev.mysql.com/downloads/mysql/).
- **MySQL Connector for Python:** Install the Python MySQL connector library:
  ```bash
  pip install mysql-connector-python
  ```

### 2. Database Setup
This project requires a MySQL database named `HOTEL_MANAGEMENT`. You can create it and set up the necessary tables by running the `database_setup.py` script.

**Important:** Before running, open `database_setup.py` and replace `'your_password'` with your actual MySQL root password.

```bash
python database_setup.py
```
This script will:
- Create the `HOTEL_MANAGEMENT` database (if it doesn't exist).
- Create `hoteldata`, `customer`, and `Room` tables.
- Insert some initial sample data into these tables.

### 3. Configure the Main Application
Open `hotel_management.py` and replace `'your_password'` with your actual MySQL root password. This ensures the application can connect to your database.

## How to Run
After completing the setup, you can run the main application:

```bash
python hotel_management.py
```

## Usage
Upon running `hotel_management.py`, you will be presented with a main menu:

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Speciality of your Hotel
2. Customer Management
3. Booking for Private Party
4. EXIT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

- **Speciality of your Hotel:** Displays information about the hotel, room types, services, and facilities.
- **Customer Management:** Leads to a sub-menu for managing customer records (booking rooms, showing, searching, deleting, and updating customer data).
- **Booking for Private Party:** (Currently not implemented in the provided code, displays a placeholder message).
- **EXIT:** Exits the application.

Follow the on-screen prompts to navigate through the system and perform various operations.

## Project Structure
```
.gitignore
hotel_management.py
database_setup.py
README.md
```

## Contributing
Feel free to fork this repository, open issues, and submit pull requests. Any contributions are welcome!

## License
This project is open-source and available under the MIT License. See the `LICENSE` file for more details. (Note: A `LICENSE` file is not included in the provided code, but it's good practice to add one.)


