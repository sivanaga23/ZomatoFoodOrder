
***

# Zomato Food Ordering System

This project is a simple **Python console-based food ordering system** that simulates an ordering experience similar to **Zomato**. Users can select a restaurant, view its menu, place orders for multiple items, and receive a detailed bill with the total amount.

***

### 📘 Features

- Displays a list of available restaurants  
- Shows menu items with prices for the selected restaurant  
- Allows users to order multiple items with quantity input  
- Calculates individual and total costs automatically  
- Generates a simple order bill with clear formatting  

***

### 🛠️ Technologies Used

- **Programming Language:** Python 3  
- **Modules:** No external libraries required (uses built-in Python functions)

***

### 📂 Project Structure

```
Zomato_Food_Ordering_System/
│
├── zomato_ordering_system.py   # Main Python program
└── README.md                   # Project documentation
```

***

### 🚀 How to Run the Project

1. Make sure you have **Python 3** installed on your system.  
2. Download or clone this project folder.  
3. Open a terminal or command prompt in the project directory.  
4. Run the script using:  
   ```
   python zomato_ordering_system.py
   ```
5. Follow the on-screen instructions:
   - Choose a restaurant  
   - View menu items  
   - Enter items and quantities to order  
   - Type `'done'` to finish ordering and view the bill  

***

### 💡 Sample Interaction

```
Available Restaurants:
1. Spice Villa
2. Pizza Hub
3. Burger World

Select a restaurant (1-3): 1

Menu - Spice Villa:
Paneer Butter Masala - ₹180
Roti - ₹20
Biryani - ₹200

Enter item to order (or 'done' to finish): Biryani
Enter quantity: 2
Enter item to order (or 'done' to finish): Roti
Enter quantity: 4
Enter item to order (or 'done' to finish): done

----- BILL -----
Biryani x2 = ₹400
Roti x4 = ₹80
Total Amount: ₹480
----------------
```

***

### 🧩 Code Overview

- **restaurants**: Dictionary holding restaurant names, their dishes, and prices.  
- **show_restaurants()**: Displays all restaurant options.  
- **show_menu(restaurant)**: Lists dishes and prices for the chosen restaurant.  
- **take_order(restaurant)**: Takes user order input and calculates item cost.  
- **print_bill(order, total)**: Prints a summary bill of the order.  
- **main()**: Main function that manages program flow.

***

### 📜 License

This project is open-source and free to use for learning or modification purposes.  

***
