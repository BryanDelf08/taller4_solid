from abc import ABC, abstractmethod

class OrderSystem:
    def __init__(self, items, apply_discount:ApplyDiscount):
        self.items = items
        self.apply_discount = apply_discount
        

    def calculate_total(self):
        total = sum(self.items)
        total_with_discount = self.apply_discount.apply(total)
        final_total = ApplyTaxes().apply_taxes(total_with_discount)
        return final_total
    
class OrderProcessor:
    def __init__(self, db:Database):
        self.db = db
        pass
    def processing(self, order:OrderSystem, payment:ProcessPayment, report:GenerateReport):
        total = order.calculate_total()
        print(report.generate_report(total))
        payment.process_payment()
        self.db.save(order_id=2304)
    
class ApplyDiscount(ABC):
    @abstractmethod
    def apply(self, total):
        pass

class ApplyTaxes:
    def apply_taxes(self, total):
        return total*1.19

class RegularDiscount(ApplyDiscount):
    def apply(self, total):
        return total*0.9  
      
class VIPDiscount(ApplyDiscount):
    def apply(self, total):
        return total*0.8
    
class EmployeeDiscount(ApplyDiscount):
    def apply(self, total):
        return total*0.5   
    
class ProcessPayment(ABC):
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

class Database(ABC):
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
    def generate_report(self, total):
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
    