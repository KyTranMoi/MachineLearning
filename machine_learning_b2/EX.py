class CustomException(Exception):
    def __init__(self, message):
        self.message = message

def divide_numbers(a, b):
    try:
        if b == 0:
            raise CustomException("Lỗi: Chia cho số 0 không được.")
        result = a / b
        print("Kết quả: ", result)
    except CustomException as e:
        print(e.message)
    except ZeroDivisionError:
        print("Lỗi: Chia cho số 0 không được trong hàm khác.")