from abc import ABC, abstractmethod

class OrderSystem:
    def __init__(self, customer_type, items, payment_method):
        self.customer_type = customer_type
        self.items = items
        self.payment_method = payment_method

    def calculate_total(self):
        total = sum(self.items)
        
        return total
    
class ApplyDiscount(OrderSystem, ABC):
    @abstractmethod
    def apply(self, total):
        pass

class ApplyTaxes:
    def apply_taxes(self, total):
        return total*1.19

class RegularDiscount(ApplyDiscount):
    def apply(self, total):
        return self.apply_taxes(total*0.9)  
      
class VIPDiscount(ApplyDiscount):
    def apply(self, total):
        return self.apply_taxes(total*0.8)
    
class EmployeeDiscount(ApplyDiscount):
    def apply(self, total):
        return self.apply_taxes(total*0.5)   
    
class ProcessPayment(OrderSystem, ABC):
    @abstractmethod
    def process_payment(self):
        pass

class CardPayment(ProcessPayment):
    def process_payment(self):
        print("Procesando pago con tarjeta")

class CashPayment(ProcessPayment):
    def process_payment(self):
        print("Procesando pago en efectivo")

class TransferPayment(ProcessPayment):
    def process_payment(self):
        print("Procesando pago por transferencia bancaria")        

class Database(OrderSystem, ABC):
    @abstractmethod
    def save(self, order_id):
        pass
    
class SaveOrderInMySQL(Database):
    def save(self, order_id):
        print(f"Guardando pedido {order_id} en MySQL...")

class SaveOrderInPostgreSQL(Database):
    def save(self, order_id):
        print(f"Guardando pedido {order_id} en PostgreSQL...")

class GenerateReport(OrderSystem, ABC):
    @abstractmethod
    def generate_report(self, format_type):
        pass

class TextReport(GenerateReport):
    def generate_report(self, total):
        
        return f"Pedido con total {total}"

class CSVReport(GenerateReport):
    def generate_report(self, total):
        
        return f"total,{total}"
    
class JSONReport(GenerateReport):
    def generate_report(self, total):
      
        return f'{{"total": {total}}}'
    
    def calculate_total(self):
        total = sum(self.items)
        if self.customer_type == "regular":
            discount = RegularDiscount(self.customer_type, self.items, self.payment_method)
            total = discount.apply(total)
        elif self.customer_type == "VIP":
            discount = VIPDiscount(self.customer_type, self.items, self.payment_method)
            total = discount.apply(total)
        elif self.customer_type == "employee":
            discount = EmployeeDiscount(self.customer_type, self.items, self.payment_method)
            total = discount.apply(total)
        return total