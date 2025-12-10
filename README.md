# PyShopSystem

A robust, CLI-based Shop Management System built with **Python** and **MySQL**. This application handles full-cycle retail operations including inventory management, customer profiling, sales processing, and automated invoice generation.

## Key Features
* **Inventory Management:** Add, update, view, and delete products (CRUD).
* **Sales Processing:** Real-time stock updates when sales are processed.
* **Billing System:** Automated invoice generation with discount calculations.
* **Customer Database:** Profile management for recurring customers.
* **Admin Authentication:** Secure login system using User IDs.
* **Reporting:** Generate sales reports for all or specific customers.

## System Requirements
* **Python:** 3.x or higher
* **Database:** MySQL Server **8.0** or above (Tested on MySQL Workbench)
* **Libraries:** `mysql-connector-python`

---

## Configuration & Setup (Read Before Running!)
** IMPORTANT:** You must configure the source code and database before the first execution to prevent connection errors.

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/raghavshivhare/PyShopSystem.git](https://github.com/raghavshivhare/PyShopSystem.git)
    cd PyShopSystem
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration (Read Before Running!)

Before executing the application, you must configure your local database settings:

1.  **Database Password:**
    * Open `main.py`.
    * Locate line 2 (or wherever your connection object is).
    * Replace `<ENTER_YOUR_SQL_PASSWORD>` with your actual MySQL root password.

2.  **Setup the Database (SQL):**
    * Open `db_setup.sql` in MySQL Workbench or Command Line.
    * Domain Change (Optional): If you wish to change the default admin credentials, edit the `insert into domain` line before running the script.
    * Recommended: To prevent "No Record Found" ambiguities during your first test, it is advised to add at least one dummy entry to the profiles, sales and billdesk table manually in the script.
    * *Security Note: It is highly recommended to change these credentials or create a new admin user immediately after your first test login by using `UPDATE`.*
    * Execute the Script: Run the entire db_setup.sql file, this will - Create the `pracdb` database, Create all 5 required tables, Pre-load 20 sample products, Create the default Admin User.

3.  **Default Login Credentials:**
    * If there is no change in MySQL `db_setup.sql` file, these steps are to be followed for first login into the tool
    * **Enter Choice:** 1
    * **User ID:** 1
    * **Password:** 1_eshop@domain
    * *NOTE: The login system asks for the user ID (e.g., 1), failing to which causes program to break abruptly.
    * Role of the user is Administrator (admin) by default. Role can be changed via MySQL for now using `UPDATE` query.

## Usage Guide
1.  **View Products:** Select option 1 to see the pre-loaded inventory (Samsung, Apple, Dell, etc.).
2.  **Make a Sale:** You must Add a Customer (Option 6) before you can process a sale for them.
3.  **Empty Tables:** If you did not add sample data to the sales or profiles tables in Step 4, options like "View Sales Report" may show no output initially. This is normal. Please use Option 6 (Add Customer) and Option 7 (Process Sale) to populate data.

## Project Structure
* `main.py`: The core application logic.
* `db_setup.sql`: SQL script to initialize the database schema.
* `requirements.txt`: List of Python dependencies.

---
*Created by **Raghav Shivhare** *