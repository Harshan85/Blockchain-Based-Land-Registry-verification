import hashlib
import time
import json


class Block:
    def __init__(self, index, timestamp, land_records, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.land_records = land_records
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'land_records': self.land_records,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"✅ Block mined: {self.hash}")


class LandRegistryBlockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 3
        self.pending_records = []

        # Authorized registrars (like Govt. offices)
        self.authorized_registrars = {
            "R001": "Chennai Registrar Office",
            "R002": "Mumbai Registrar Office",
            "R003": "Delhi Registrar Office"
        }

    def create_genesis_block(self):
        return Block(0, time.time(), ["Genesis Block: Land Registry"], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_land_record(self, registrar_id, property_id, owner, location, area):
        if registrar_id not in self.authorized_registrars:
            print("⛔ Unauthorized Registrar. Cannot add land record.")
            return

        office = self.authorized_registrars[registrar_id]
        self.pending_records.append({
            "property_id": property_id,
            "owner": owner,
            "location": location,
            "area_sqft": area,
            "registered_by": office
        })
        print(f"✅ Land record added by {office}")

    def mine_pending_records(self, registrar_id):
        if registrar_id not in self.authorized_registrars:
            print("⛔ Unauthorized mining attempt!")
            self.pending_records = []
            return

        block = Block(len(self.chain), time.time(), self.pending_records, self.get_latest_block().hash)
        block.mine_block(self.difficulty)
        self.chain.append(block)
        print(f"📜 Block validated by {self.authorized_registrars[registrar_id]}")
        self.pending_records = []

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.calculate_hash():
                return False
            if curr.previous_hash != prev.hash:
                return False
        return True

    def print_chain(self):
        for block in self.chain:
            print(json.dumps({
                "index": block.index,
                "timestamp": block.timestamp,
                "land_records": block.land_records,
                "hash": block.hash,
                "previous_hash": block.previous_hash
            }, indent=4))
            print("-" * 50)

    # Search land ownership
    def verify_land(self, property_id):
        for block in self.chain:
            for rec in block.land_records:
                if isinstance(rec, dict) and rec.get("property_id") == property_id:
                    print(f"✅ Verified Record for Property {property_id}:")
                    print(json.dumps(rec, indent=4))
                    return
        print(f"⚠️ No land record found for Property {property_id}")


# --- CLI Demo ---
if __name__ == "__main__":
    land_chain = LandRegistryBlockchain()

    while True:
        print("\n=== Blockchain Land Registry ===")
        print("1. Add land record (Registrar only)")
        print("2. Mine block (validate land records)")
        print("3. Show blockchain")
        print("4. Validate blockchain")
        print("5. Verify land ownership by Property ID")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            rid = input("Enter Registrar ID: ")
            pid = input("Property ID: ")
            owner = input("Owner Name: ")
            location = input("Location: ")
            area = input("Area in sqft: ")
            land_chain.add_land_record(rid, pid, owner, location, area)

        elif choice == "2":
            rid = input("Enter Registrar ID for validation: ")
            land_chain.mine_pending_records(rid)

        elif choice == "3":
            land_chain.print_chain()

        elif choice == "4":
            print("Blockchain valid?", land_chain.is_chain_valid())

        elif choice == "5":
            pid = input("Enter Property ID to verify: ")
            land_chain.verify_land(pid)

        elif choice == "6":
            break

        else:
            print("Invalid choice, try again.")
