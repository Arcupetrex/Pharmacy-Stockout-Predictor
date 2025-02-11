

# 📊 Pharmacy Stock Prediction Project

This project predicts which drugs will run out of stock within the next two weeks based on current stock levels and weekly sales data from a pharmacy. The prediction is done using a Python script that analyzes a CSV file (`pharmacy_stock.csv`) containing drug information and sales patterns. 

---

## 🚀 Features

- Predicts when drugs will run out of stock.  
- Uses a simple algorithm to calculate the time remaining based on sales data.  
- Outputs a list of drugs that are at risk of running out in the next two weeks.  

---

## 🗂 Project Structure

```
.
├── pharmacy_stock.csv        # Sample dataset with drug stock and sales data
├── predict_stock.py          # Python script to predict stock depletion
└── README.md                 # Project documentation
```

---

## 📄 Dataset

The dataset (`pharmacy_stock.csv`) contains the following columns:  

- `drug_name`: The name of the drug (e.g., Paracetamol, Ibuprofen).  
- `stock_level`: The current stock quantity for the drug.  
- `sales_per_week`: Average weekly sales of the drug.  

Example of the dataset:  

```csv
drug_name,stock_level,sales_per_week
Paracetamol,150,30
Ibuprofen,180,35
Aspirin,120,25
```

---

## 🔧 How to Run the Script

1. Clone this repository:  
   ```
   git clone [https://github.com/Arcupetrex/Pharmacy-Stockout-Predictor.git]

   cd pharmacy-stock-prediction
   ```

2. Install Python (if not installed):  
   [Download Python](https://www.python.org/downloads/)  

3. Run the script:  
   ```
   python predict_stock.py
   ```

4. The script will read `pharmacy_stock.csv` and display a list of drugs predicted to run out of stock within the next two weeks.

---

## 📦 Sample Output

```
The following drugs are predicted to run out within the next 2 weeks:
1. Paracetamol (stock: 150, sales/week: 30)
2. Aspirin (stock: 50, sales/week: 25)
```

---

## 🛠 Future Enhancements

- Add visualization for stock trends.  
- Use machine learning for more accurate predictions.  
- Automate email alerts when stock levels are low.  

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 📧 Contact

For questions or suggestions, feel free to reach out.  
```

