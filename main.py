from abc import ABC, abstractmethod

class OrderSystem:
    """_Contiene la lógica para calcular el total de un pedido_
    """    

    def __init__(self, items, apply_discount:ApplyDiscount):
        """_Inicializa el sistema de pedidos_

        Args:
            items (_str_): _Productos a pedir_
            apply_discount (ApplyDiscount): _Lógica para aplicar descuentos_
        """        
        self.items = items
        self.apply_discount = apply_discount
        

    def calculate_total(self):
        """_Método que calcula el precio total del pedido_

        Returns:
            _float_: __Precio total del pedido con descuentos y impuestos aplicados__
        """        
        total = sum(self.items)
        total_with_discount = self.apply_discount.apply(total)
        final_total = ApplyTaxes().apply_taxes(total_with_discount)
        return final_total
    
class OrderProcessor:
    """_Procesa y guarda el pedido_
    """    
    def __init__(self, db:Database):
        """_Inicializa la base de datos_

        Args:
            db (Database): _Base de datos genérica_
        """        
        self.db = db
        pass
    def processing(self, order:OrderSystem, payment:ProcessPayment, report:GenerateReport):
        """_Procesa las características del pedido_

        Args:
            order (OrderSystem): _Descripción del pedido_
            payment (ProcessPayment): _Método de pago_
            report (GenerateReport): _Genera el reporte en cierto formato_
        """        
        total = order.calculate_total()
        print(report.generate_report(total))
        payment.process_payment()
        self.db.save(order_id=2304)
    
class ApplyDiscount(ABC):
    """_Clase abstracta para calcular el descuento_

    Args:
        ABC (_abstract_): _Clase abstracta_
    """    
    @abstractmethod
    def apply(self, total):
        """_Método abstracto_

        Args:
            total (_float_): _Total con descuento_
        """        
        pass

class ApplyTaxes:
    """_Aplica impuestos_
    """    
    def apply_taxes(self, total):
        """_Método que aplica impuestos_

        Args:
            total (_float_): _Total con impuestos_

        Returns:
            _float_: _Total con impuestos aplicados_
        """                
        return total*1.19

class RegularDiscount(ApplyDiscount):
    """_Aplica descuento regular_

    Args:
        ApplyDiscount (_abstract_): _esta clase hereda de esa clase abstracta_
    """    
    def apply(self, total):
        """_metodo que aplica descuento regular_

        Args:
            total (_float_): _Total con descuento_

        Returns:
            _float_: _Total con descuento aplicado_
        """        
        return total*0.9  
      
class VIPDiscount(ApplyDiscount):
    """_Aplica descuento VIP_

    Args:
        ApplyDiscount (_abstract_): _esta clase hereda de esa clase abstracta_
    """    
    def apply(self, total):
        """_metodo que aplica descuento VIP_

        Args:
            total (_float_): _Total con descuento_

        Returns:
            _float_: _Total con descuento aplicado_
        """  
        return total*0.8
    
class EmployeeDiscount(ApplyDiscount):
    """_Aplica descuento para empleados_

    Args:
        ApplyDiscount (_abstract_): _esta clase hereda de esa clase abstracta_
    """    
    def apply(self, total):
        """_metodo que aplica descuento para empleados_

        Args:
            total (_float_): _Total con descuento_

        Returns:
            _float_: _Total con descuento aplicado_
        """  
        return total*0.5   
    
class ProcessPayment(ABC):
    """_Clase abstracta para procesar pagos_

    Args:
        ABC (_abstract_): _Clase abstracta_
    """    
    @abstractmethod
    def process_payment(self):
        """_Método para sobrescribir_
        """        
        pass

class CardPayment(ProcessPayment):
    """_Pago con tarjeta_

    Args:
        ProcessPayment (_ABC_): _Clase abstracta_
    """    
    def process_payment(self):
        """_Impresión de mensaje de pago con tarjeta_
        """        
        print("Procesando pago con tarjeta")

class CashPayment(ProcessPayment):
    """_Pago con efectivo_

    Args:
        ProcessPayment (_ABC_): _Clase abstracta_
    """    
    def process_payment(self):
        """_Impresión de mensaje de pago en efectivo_
        """        
        print("Procesando pago en efectivo")

class TransferPayment(ProcessPayment):
    """_Pago por transferencia bancaria_

    Args:
        ProcessPayment (_ABC_): _Clase abstracta_
    """    
    def process_payment(self):
        """_Impresión de mensaje de pago por transferencia_
        """        
        print("Procesando pago por transferencia bancaria")        

class Database(ABC):
    """_Clase abstracta para gestionar la base de datos_

    Args:
        ABC (_abstract_): _Clase abstracta_
    """    
    @abstractmethod
    def save(self, order_id):
        """_Método para sobrescribir_
        """        
        pass
    
class SaveOrderInMySQL(Database):
    """_Guarda el pedido en MySQL_

    Args:
        Database (_abstract_): _Clase abstracta_
    """    
    def save(self, order_id):
        """_Método para guardar el pedido usando su ID_

        Args:
            order_id (_str_): _ID del pedido_
        """        
        print(f"Guardando pedido {order_id} en MySQL...")

class SaveOrderInPostgreSQL(Database):
    """_Guarda el pedido en PostgreSQL_

    Args:
        Database (_abstract_): _Clase abstracta_
    """    
    def save(self, order_id):
        """_Método para guardar el pedido usando su ID_

        Args:
            order_id (_str_): _ID del pedido_
        """             
        print(f"Guardando pedido {order_id} en PostgreSQL...")

class GenerateReport(ABC):
    """_Clase abstracta para generar reportes_

    Args:
        ABC (_abstract_): _Clase abstracta_
    """    
    @abstractmethod
    def generate_report(self, total):
        """_Método para sobrescribir_

        Args:
            total (_float_): _Total del pedido, valor que será mostrado en consola_
        """        
        pass

class TextReport(GenerateReport):
    """_Generar reporte en formato de texto_

    Args:
        GenerateReport (_abstract_): _Clase abstracta_
    """    
    def generate_report(self, total):
        """_Método que imprime el reporte en formato de texto_

        Args:
            total (_float_): _Valor total del pedido el cual será mostrado en consola_

        Returns:
            _str_: _Impresión del reporte_
        """        
        return f"Pedido con total {total}"

class CSVReport(GenerateReport):
    """_Generar reporte en formato CSV_

    Args:
        GenerateReport (_abstract_): _Clase abstracta_
    """    
    def generate_report(self, total):
        """_Método que imprime el reporte en formato CSV_

        Args:
            total (_float_): _Valor total del pedido el cual será mostrado en consola_

        Returns:
            _str_: _Impresión del reporte_
        """

        return f"total,{total}"
    
class JSONReport(GenerateReport):
    """_Generar reporte en formato JSON_

    Args:
        GenerateReport (_abstract_): _Clase abstracta_
    """    
    def generate_report(self, total):
        """_Método que imprime el reporte en formato JSON_

        Args:
            total (_float_): _Valor total del pedido el cual será mostrado en consola_

        Returns:
            _str_: _Impresión del reporte_
        """
        
        return f'{{"total": {total}}}'
    