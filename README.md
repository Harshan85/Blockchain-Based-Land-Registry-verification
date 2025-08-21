# 🏡 Blockchain-Based Land Registry

A simple Python implementation of a **Blockchain system for Real Estate & Land Registry**.
This project demonstrates how blockchain can be applied to **prevent fraud in property ownership** by maintaining **tamper-proof land records**.

---

## 🚀 Features

* ✅ Add new land/property records (Registrar authorized only)
* ✅ Secure & immutable records stored in a blockchain ledger
* ✅ Proof-of-Work mining for validation
* ✅ View full blockchain with all blocks and hashes
* ✅ Validate the integrity of the blockchain
* ✅ Verify land ownership by **Property ID**
* ⚡ Future Scope: Support for **ownership transfer**, **smart contracts**, and **multi-node network**

---

## 📂 Project Structure

```
├── land_registry_blockchain.py   # Main Python script
├── README.md                     # Project documentation
```

---

## ⚙️ Installation & Usage

### 1. Clone this repo

```bash
git clone https://github.com/your-username/land-registry-blockchain.git
cd land-registry-blockchain
```

### 2. Run the script

```bash
python land_registry_blockchain.py
```

### 3. Menu Options

When you run the script, you’ll see an interactive menu:

```
=== Blockchain Land Registry ===
1. Add land record (Registrar only)
2. Mine block (validate land records)
3. Show blockchain
4. Validate blockchain
5. Verify land ownership by Property ID
6. Exit
```

---

## 🖥️ Sample Run

```
Enter Registrar ID: R001
Property ID: PLOT-001
Owner Name: Alice
Location: Chennai
Area in sqft: 1200
✅ Land record added by Chennai Registrar Office

✅ Block mined: 000e93f43c2c5e1f3a92f7e8fbcdf2d998a7d9f743fd28d75c48d372f5f21577
📜 Block validated by Chennai Registrar Office

✅ Verified Record for Property PLOT-001:
{
    "property_id": "PLOT-001",
    "owner": "Alice",
    "location": "Chennai",
    "area_sqft": "1200",
    "registered_by": "Chennai Registrar Office"
}


## 🛠️ Tech Stack

* **Language**: Python 3
* **Core Concepts**: Blockchain, Proof of Work, Hashing (SHA-256), Immutable Ledger



## 🌍 Real-World Inspiration

* **Republic of Georgia**: Using blockchain for national land registry
* **Propy**: A blockchain platform for global real estate deals



## 📌 Future Improvements

* 🔄 Ownership transfer (property re-sale on blockchain)
* 🌐 Multi-node P2P blockchain network simulation
* 📜 Smart contracts for automated property transactions
* 🔐 Integration with government ID systems



## 🤝 Contributing

Pull requests are welcome! If you’d like to add features (like ownership transfer or P2P), feel free to fork and enhance this project.



## 📜 License

This project is licensed under the **MIT License** – feel free to use, modify, and distribute.


